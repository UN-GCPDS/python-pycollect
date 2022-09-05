"""
=========
GE Decode
=========

Synchronize in decoder with a buffer reference, decoder `GEDecode` will attempt
to process new data added to the buffer.

.. code:: ipython3

    decoder = GEDecode(device.BUFFER)
    decoder.process(True)


There are a set of methods for clear correctly the stored buffer and recollected data.

.. code:: ipython3

    device.clear_buffer()  # clear input buffer.
    decoder.clear_buffer()  # clear decoded data, breaks the synchrony.
    decoder.clear_data()  # clear recollected data.

"""

import os
import time
import struct
import json
from threading import Thread
from datetime import datetime, timedelta, date

from .dataconstants import CONST
from .edfwriter import EDF, EDFChannel
from .headers import DatexHeaderResponse, PhysiologicalData, HeaderHandler
from .measures import WAVEFORMS_DICT, LABEL_TO_DICT, GROUPS_DICT

from pandas import DataFrame, np


########################################################################
class GEDecode:
    """Decode raw data into Pandas DataFrames.

    There are two main objects:

      * `DATA_SUBRECORD`: Pandas DataFrame with the subrecords data.
      * `DATA_WAVE`: Dictionary with waveform name as key with the
         Pandas DataFrame with the waveform data.
    """

    #----------------------------------------------------------------------
    def __init__(self, buffer, filter_subrecords=None, filter_waveforms=None):
        """
        Parameters
        ----------
        buffer: array reference
           Reference with raw data, the processer will attempt to decoded new
           data added to this object.
        filter_subrecords: array, optional
           Sublist with desired subrecords, if empty then will process all available measures.
        filter_waveforms: array, optional
           List of desired waveforms, if emty then will process all requested waveforms.
        """

        self.m_list = []
        self.record_list = []
        self.frame_list = []

        if filter_subrecords is None:
            filter_subrecords = []

        if filter_waveforms is None:
            filter_waveforms = []

        # Display user data
        self.DATA_SUBRECORD = DataFrame()
        self.DATA_WAVE = {}

        # Read and write intern data
        self.__DATA_SUBRECORD__ = DataFrame()
        self.__DATA_WAVE__ = {}

        # Modules, groups and measures availables
        self.MODULES = []
        self.MODULES_ACTIVE = []
        self.MEANSURES_AVAILABLE = []

        # Sublist with measures
        self.FILTER_SUBRECORDS = filter_subrecords
        self.FILTER_WAVEFORMS = filter_waveforms

        # Temporal and permanent buffers
        self.BUFFER = buffer
        self.PROCCESED_BUFFER = []
        self.PROCESSING = False

        self.m_fstart = True
        self.m_storestart = False
        self.m_storeend = False
        self.m_bitshiftnext = False
        self.m_transmissionstart = True

        # Default header can be empty
        self.edf_header = {}

        # First process in initialization
        self.__processing__()


    #----------------------------------------------------------------------
    def clear_buffer(self):
        """Clear the processed buffer.

        This action brake the synchrony with GEDevice.
        """

        self.BUFFER = []
        self.PROCCESED_BUFFER = []


    #----------------------------------------------------------------------
    def clear_data(self):
        """Clear the processed data."""

        self.DATA_SUBRECORD = DataFrame()
        self.DATA_WAVE = {}
        self.__DATA_SUBRECORD__ = DataFrame()
        self.__DATA_WAVE__ = {}
        # self.DATA_TREND_10S = DataFrame()


    #----------------------------------------------------------------------
    def process(self, flag=True, delay=1):
        """Enable or disable the continuous data processing.

        Parameters
        ----------
        flag: bool, True
           Enable or disable the continuous data processing.
        delay: integer in seconds
           Delay in seconds between each process attempt.
        """

        self.PROCESSING = flag

        if self.PROCESSING:
            self.thr_process = Thread(target=self.__continuous_processing__, args=(delay, ))
            self.thr_process.start()


    #----------------------------------------------------------------------
    def __continuous_processing__(self, delay=1/4):
        """Continuous processing.

        Parameters
        ----------
        delay: integer in seconds
           Delay in seconds between each attempted processing.
        """

        while self.PROCESSING:
            time.sleep(delay)
            self.__processing__()


    #----------------------------------------------------------------------
    def __processing__(self):
        """Process the input buffer one byte at a time.

        Process the input buffer until a header is completed.
        """

        bytes_ = self.BUFFER[len(self.PROCCESED_BUFFER):]
        self.PROCCESED_BUFFER = self.BUFFER[:]

        for byte in bytes_:

            self.__create_framelist__(byte)

            if self.frame_list:
                record_list = self.__create_recordlist__()

                self.read_subrecords(record_list[:])
                self.read_waveforms(record_list[:])

                self.frame_list = []


    #----------------------------------------------------------------------
    def save_as_csv(self, filename):
        """Save the decoded data into a set of CSV files.

        Parameters
        ----------
        filename : str
            Absolute or realtive path for CSV file.

        Returns
        -------
        list
            A list with filenames generated.
        """

        if os.path.exists(os.path.dirname(os.path.abspath(filename))):
            os.makedirs(os.path.dirname(os.path.abspath(filename)), exist_ok=True)

        if not '.csv' in filename:
            filename = filename + '.csv'

        filenames = []

        if not self.__DATA_SUBRECORD__.empty:
            self.__DATA_SUBRECORD__.to_csv(filename)
            filenames.append(filename)

        if self.__DATA_WAVE__:
            for df in self.__DATA_WAVE__:
                self.__DATA_WAVE__[df].to_csv(filename.replace('.csv', '.{}.csv'.format(df)))
                filenames.append(filename.replace('.csv', '.{}.csv'.format(df)))

        return filenames


    #----------------------------------------------------------------------
    def set_edf_header(self, **header):
        """Set the EDF+ patient header.

        Parameters
        ----------
        admincode : str
            Sets the admincode.

        birthdate : date object from datetime
            Sets the birthdate.

        equipment : str
            Describes the measurement equpipment.

        gender : int
            Sets the gender, 1 is male, 0 is female.

        patientcode : str
            Sets the patient code.

        patientname : str
            Sets the patient name.

        patient_additional : str
            Sets the additional patient info.

        recording_additional : str
            Sets the additional recordinginfo.

        startdate : datetime object
            Sets the recording start Time.

        technician : str
            Sets the technicians name.
        """

        self.edf_header = header


    #----------------------------------------------------------------------
    def save_as_raw(self, filename):
        """Save the decoded data into a RAW file.

        Parameters
        ----------
        filename : str
            Absolute or realtive path for RAW file.

        Returns
        -------
        list
            A list with filenames generated.
        """

        if os.path.exists(os.path.dirname(os.path.abspath(filename))):
            os.makedirs(os.path.dirname(os.path.abspath(filename)), exist_ok=True)

        if not '.raw' in filename:
            filename = filename + '.raw'

        if self.BUFFER:
            file = open(filename, 'wb')
            file.write(bytes(self.BUFFER))
            file.close()
            return [filename]
        return []


    #----------------------------------------------------------------------
    def save_as_edf(self, filename, edf_header=None, annotations=None):
        """Save the decoded data into a set of EDF+ files.

        Parameters
        ----------
        filename : str
            Absolute or realtive path for EDF+ file.

        edf_header: dict
            Declare the EDF+ patient header.

        Returns
        -------
        list
            A list with filenames genrated.
        """

        if edf_header:
            pass
        else:
            edf_header = self.edf_header

        if annotations is None:
            annotations = []

        if edf_header is None:
            edf_header = {}


        #set birthdate in datetime python format
        if edf_header.get('birthdate', None):
            edf_header['birthdate'] = datetime.fromtimestamp(edf_header.get('birthdate', 0))
        else:
            edf_header['birthdate'] = date(1900, 1, 1)



        # Differents EDF because will have different startdate
        l1 = self.save_waves_as_edf(filename, edf_header, annotations)
        l2 = self.save_disp_as_edf(filename, edf_header, annotations)

        return l1 + l2


    #----------------------------------------------------------------------
    def save_waves_as_edf(self, filename, edf_header, annotations):
        """"""

        if os.path.exists(os.path.dirname(os.path.abspath(filename))):
            os.makedirs(os.path.dirname(os.path.abspath(filename)), exist_ok=True)

        if not self.__DATA_WAVE__:
            return []

        if not '.edf' in filename:
            filename = filename + '.edf'

        filename = filename.replace('.edf', '.waves.edf')

        if os.path.exists(filename):
            os.remove(filename)

        # edf_header['birthdate'] = datetime.fromtimestamp(edf_header['birthdate'])

        edf = EDF(filename)
        edf.set_header(**edf_header)

        # NOTE: ``first_datetime`` is already a python datetime, so do not need ``fromtimestamp``.
        first_datetime = self.__DATA_WAVE__[list(self.__DATA_WAVE__.keys())[0]]['datetime'][0]
        # edf.header.update({'startdate': datetime.fromtimestamp(first_datetime),})
        edf.header.update({'startdate': first_datetime})

        for df in self.__DATA_WAVE__:
            wave = self.__DATA_WAVE__[df]
            data = np.nan_to_num(np.array(wave['values'].tolist(), dtype=np.float))
            channel = EDFChannel(data)
            channel['label'] = df
            channel['dimension'] = WAVEFORMS_DICT[df]['unit']
            channel['sample_rate'] = WAVEFORMS_DICT[df]['samps']

            if not WAVEFORMS_DICT[df].get('physical_min', None) is None:
                channel['physical_min'] = WAVEFORMS_DICT[df]['physical_min']
            else:
                channel['physical_min'] = np.floor(min(data))

            if not WAVEFORMS_DICT[df].get('physical_max', None) is None:
                channel['physical_max'] = WAVEFORMS_DICT[df]['physical_max']
            else:
                channel['physical_max'] = np.ceil(max(data))

            channel['digital_min'] = -2 ** 15
            channel['digital_max'] = 2 ** 15
            channel['transducer'] = WAVEFORMS_DICT[df]['transducer']
            channel['prefilter'] = WAVEFORMS_DICT[df]['prefilter']
            edf.add_channel(channel)

        for annotation in annotations:
            edf.write_annotation(**annotation)

        edf.save()
        return [filename]


    #----------------------------------------------------------------------
    def save_disp_as_edf(self, filename, edf_header, annotations):
        """"""

        if os.path.exists(os.path.dirname(os.path.abspath(filename))):
            os.makedirs(os.path.dirname(os.path.abspath(filename)), exist_ok=True)

        if self.__DATA_SUBRECORD__.empty:
            return []

        if not '.edf' in filename:
            filename = filename + '.edf'

        filename = filename.replace('.edf', '.disp.edf')

        # edf_header['birthdate'] = datetime.fromtimestamp(edf_header['birthdate'])

        if os.path.exists(filename):
            os.remove(filename)

        edf = EDF(filename)
        edf.set_header(**edf_header)

        # NOTE: ``first_datetime`` will be of type int/float, so need ``fromtimestamp`` to become in a python datetime object.
        first_datetime = json.loads(self.__DATA_SUBRECORD__.iloc[0].to_json()).pop('datetime') / 1e3
        # edf.header.update({'startdate': datetime.fromtimestamp(first_datetime),})
        edf.header.update({'startdate': datetime.fromtimestamp(first_datetime),})


        keys = list(self.__DATA_SUBRECORD__.columns)

        for key in keys:
            if key == 'datetime':
                continue

            data = self.__DATA_SUBRECORD__[key].tolist()
            # If the first data is not a number, then the array conains labels
            if not isinstance(data[0], (int, float)):
                continue

            # If the first data is a number, but there are a label somewhere
            if list(filter(lambda n: isinstance(n, (str, bytes)), data)):
                continue

            # After eliminate labels, now data contain only numbers,
            np_data = np.array(data, dtype=np.float)

            channel = EDFChannel(np.nan_to_num(np_data))
            channel['label'] = key
            channel['dimension'] = LABEL_TO_DICT[key].get('unit', '')
            channel['sample_rate'] = 1

            # if WAVEFORMS_DICT[df]['physical_min']:
                # channel['physical_min'] = 0
            # else:

            # if WAVEFORMS_DICT[df]['physical_max']:
                # channel['physical_max'] = 1
            # else:
                # channel['physical_max'] = np.ceil(max(data))

            # channel['physical_min'] = -5
            # channel['physical_max'] = 5

            if not LABEL_TO_DICT[key].get('physical_min', None) is None:
                channel['physical_min'] = LABEL_TO_DICT[key]['physical_min']
            else:
                channel['physical_min'] = np.floor(min(data))

            if not LABEL_TO_DICT[key].get('physical_max', None) is None:
                channel['physical_max'] = LABEL_TO_DICT[key]['physical_max']
            else:
                channel['physical_max'] = np.ceil(max(data))


            channel['digital_min'] = -2 ** 15
            channel['digital_max'] = 2 ** 15
            channel['transducer'] = ''
            channel['prefilter'] = ''
            edf.add_channel(channel)

        for annotation in annotations:
            edf.write_annotation(**annotation)

        # edf.
        edf.save()
        return [filename]






    #----------------------------------------------------------------------
    def __create_framelist__(self, byte):
        """Search for a complete and validated header.

        Parameters
        ----------
        byte : byte
            Byte readed from serial raw data.
        """

        if byte == CONST.FRAMECHAR and self.m_fstart:
            self.m_fstart = False
            self.m_storestart = True

        elif byte == CONST.FRAMECHAR and not self.m_fstart:

            self.m_fstart = False
            self.m_storeend = True
            self.m_storestart = False


            if byte != CONST.FRAMECHAR:
                self.m_list.append(byte)


        if self.m_storestart:

            if byte == CONST.CTRLCHAR:
                self.m_bitshiftnext = True

            else:
                if self.m_bitshiftnext:

                    byte |= CONST.BIT5
                    self.m_bitshiftnext = False
                    self.m_list.append(byte)

                elif byte != CONST.FRAMECHAR:
                    self.m_list.append(byte)


        elif self.m_storeend:

            framelen = len(self.m_list)

            if framelen:

                checksum = sum(self.m_list[:-1]).to_bytes(4, 'big')[-1]

                if checksum == self.m_list[-1]:
                    self.frame_list.append(self.m_list[:])
                # else:
                    # print("Wrong checksum")

                self.m_list = []
                self.m_storeend = False


            else:
                self.m_storestart = True
                self.m_storeend = False
                self.m_fstart = False


    #----------------------------------------------------------------------
    def __create_recordlist__(self):
        """Complete the raw header with the correct/full size.

        Returns
        -------
        list
            Full sized DatexHeaderResponse.
        """

        data_list = []
        for header in self.frame_list:
            data = header[:-1] + [0]*(DatexHeaderResponse.LENGTH - len(header)) + [header[-1]]
            data_list.append(data)

        return data_list


    #----------------------------------------------------------------------
    def read_waveforms(self, record_list, ignore_missging=False):
        """Update the dictionary of waveforms with new decoded data.

        Parameters
        ----------
        record_list: array
           List of raw headers.
        """

        for record in map(DatexHeaderResponse, record_list):

            if record['r_maintype'] != CONST.DRI_MT_WAVE:
                continue

            sroffArray = [record['sr_offset1'], record['sr_offset2'], record['sr_offset3'], record['sr_offset4'], record['sr_offset5'], record['sr_offset6'], record['sr_offset7'], record['sr_offset8']]
            srtypeArray = [record['sr_type1'], record['sr_type2'], record['sr_type3'], record['sr_type4'], record['sr_type5'], record['sr_type6'], record['sr_type7'], record['sr_type8']]

            unixtime = record['r_time']
            date_ = datetime(1970, 1, 1, 0, 0, 0, 0) + timedelta(seconds=unixtime)


            for i, srtype, offset in zip(range(8), srtypeArray, sroffArray):
                if srtype == CONST.DRI_EOL_SUBR_LIST:
                    break

                if i == 7:
                    nextoffset = 1450
                else:
                    nextoffset = sroffArray[i+1]

                    # When just one waveform is requested.
                    if nextoffset == 0:
                        nextoffset = WAVEFORMS_DICT[{d[1]:d[0] for d in CONST.DRI_WAVEFORM.items()}[srtype]]['samps'] * 2
                        nextoffset = nextoffset + offset + 6


                buffer = record['-data,'][6+offset : nextoffset]


                for k, m in CONST.DRI_WAVEFORM.items():
                    if m == srtype:

                        if self.FILTER_WAVEFORMS and not k in self.FILTER_WAVEFORMS:
                            continue

                        # if not k in self.FILTER_WAVEFORMS:
                            # continue

                        values = self.read_shorts(buffer[:])


                        # NO shifting
                        if not False in (np.array(values) > CONST.DATA_INVALID):
                            values = [v*WAVEFORMS_DICT[k].get('shift', 1) for v in values]
                            # values = [v*WAVEFORMS_DICT[k].get('shift_', 1) for v in values]

                        dates = [date_] * len(values)

                        # update DATA_WAVE_SUBRECORD
                        if not k in self.DATA_WAVE:
                            self.DATA_WAVE[k] = DataFrame({'datetime': dates, 'values': values,})
                        else:
                            self.DATA_WAVE[k] = self.DATA_WAVE[k].append(DataFrame({'datetime': dates, 'values': values,}), ignore_index=True, sort=True)

                        # update __DATA_WAVE_SUBRECORD__
                        if not k in self.__DATA_WAVE__:
                            self.__DATA_WAVE__[k] = DataFrame({'datetime': dates, 'values': values,})
                        else:
                            self.__DATA_WAVE__[k] = self.__DATA_WAVE__[k].append(DataFrame({'datetime': dates, 'values': values,}), ignore_index=True, sort=True)


                if nextoffset <= offset or nextoffset > 1450:
                    break

        if not ignore_missging:
            for f in self.DATA_WAVE:
                if f not in self.__DATA_WAVE__:
                    self.DATA_WAVE[f](DataFrame({'datetime': dates[0], 'values': CONST.DATA_INVALID,}))
                    self.__DATA_WAVE__[f](DataFrame({'datetime': dates[0], 'values': CONST.DATA_INVALID,}))


    #----------------------------------------------------------------------
    def read_shorts(self, buffer):
        """Convert an array if bytes from signed 16 bits to integer.

        Parameters
        ----------
        buffer: array
            Array with raw bytes, It will be processed in pairs (for complete 16 bits).
        """

        return [i[0] for i in struct.iter_unpack('<h', bytes(buffer))]



    #----------------------------------------------------------------------
    def read_subrecords(self, record_list):
        """Update the DataFrame of subrecords with new decoded data.

        Parameters
        ----------
        record_list: array
           Raw DatexHeaderResponse.
        """

        for record in map(DatexHeaderResponse, record_list):

            if record['r_maintype'] != CONST.DRI_MT_PHDB:
                continue

            sroffArray = [record['sr_offset1'], record['sr_offset2'], record['sr_offset3'], record['sr_offset4'], record['sr_offset5'], record['sr_offset6'], record['sr_offset7'], record['sr_offset8']]
            srtypeArray = [record['sr_type1'], record['sr_type2'], record['sr_type3'], record['sr_type4'], record['sr_type5'], record['sr_type6'], record['sr_type7'], record['sr_type8']]

            unixtime = record['r_time']
            # print(unixtime)
            date_ = datetime(1970, 1, 1, 0, 0, 0, 0) + timedelta(seconds=unixtime)


            #----------------------------------------------------------------------

            # phdata_ptr = PhysiologicalData()
            # phdata_ptr.load(record['-data,'])

            #----------------------------------------------------------------------

            phdata_ptr = PhysiologicalData()
            for i, srtype, offset in zip(range(8), srtypeArray, sroffArray):
                if srtype == CONST.DRI_EOL_SUBR_LIST:
                    break

                buffer = record['-data,'][4+offset:4+offset + 270]

                if i == 0:
                    phdata_ptr.DATA['basic'] = HeaderHandler(data=buffer, init=phdata_ptr['basic'], size=270).DATA
                elif i== 1:
                    phdata_ptr.DATA['ext1'] = HeaderHandler(data=buffer, init=phdata_ptr['ext1'], size=270).DATA
                elif i == 2:
                    phdata_ptr.DATA['ext2'] = HeaderHandler(data=buffer, init=phdata_ptr['ext2'], size=270).DATA
                elif i == 3:
                    phdata_ptr.DATA['ext3'] = HeaderHandler(data=buffer, init=phdata_ptr['ext3'], size=270).DATA

            #----------------------------------------------------------------------

            subrecord = FormatSubrecord(date_, phdata_ptr)  #.format()
            self.MODULES, self.MODULES_ACTIVE, self.MEANSURES_AVAILABLE = subrecord.module_status()

            df = subrecord.format(self.MODULES_ACTIVE, self.FILTER_SUBRECORDS)


            # DATA_SUBRECORD update
            if not df is None:
                if self.DATA_SUBRECORD.empty:
                    self.DATA_SUBRECORD = df.copy()
                else:
                    self.DATA_SUBRECORD = self.DATA_SUBRECORD.append(df.copy(), ignore_index=True, sort=True)

            # __DATA_SUBRECORD__ update
            if not df is None:
                if self.__DATA_SUBRECORD__.empty:
                    self.__DATA_SUBRECORD__ = df.copy()
                else:
                    self.__DATA_SUBRECORD__ = self.__DATA_SUBRECORD__.append(df.copy(), ignore_index=True, sort=True)



########################################################################
class FormatSubrecord:
    """Parse raw data into Pandas DataFrames."""

    #----------------------------------------------------------------------
    def __init__(self, date_, header):
        """
        Parameters
        ----------
        date_ : Datetime object
            Datetime of the current set.

        header : PhysiologicalData object
            Header with raw data.
        """
        self.data = {}
        self.date = date_
        self.header = header

        self.data = [

            # Basic
            ('INV-BP', ['p_group', 'p1']),
            ('INV-BP', ['p_group', 'p2']),
            ('INV-BP', ['p_group', 'p3']),
            ('INV-BP', ['p_group', 'p4']),
            ('INV-BP', ['p_group', 'p5']),
            ('INV-BP', ['p_group', 'p6']),
            ('TEMP', ['t_group', 't1']),
            ('TEMP', ['t_group', 't2']),
            ('TEMP', ['t_group', 't3']),
            ('TEMP', ['t_group', 't4']),
            'ECG',
            'NIBP',
            'SpO2',
            'CO2',
            'O2',
            'N2O',
            'AA',
            'FLOW-VOL',
            'CO-WEDGE',
            'NMT',
            'ECG-EXTRA',
            'SvO2',

            #Ext1
            'ECG-ARRH',
            'ECG-12',

            #Ext2
            'NMT2',
            'EEG',
            'EEG-BIS',
            'ENTROPY',
            'EEG2',

            # Ext3
            'GASEX',
            'FLOW-VOL2',
            'BAL-GAS',
            'TONO',
            'AA2',

        ]


    #----------------------------------------------------------------------
    def module_status(self):
        """Return the list of present and active modules.

        Based in the status bits is possible determine the state of the
        respective module.

        Returns
        -------
        list
            List of groups with modules availables.
        list
            List of groups with modules availables and actives.
        list
            List of measures availables and actives.
        """

        modules = []
        modules_active = []
        meansures_available = []

        for measure in self.data:
            if isinstance(measure, tuple):
                measure, replace = measure
                name = '{} ({})'.format(measure, replace[1])
            else:
                replace = ['', '']
                name = measure

            exist, active = self.check_module(measure, replace)

            if exist:
                modules.append(name)
                if active:
                    modules_active.append(name)


                    measures = []

                    for g in GROUPS_DICT[measure]:



                        if g['label'].endswith(': MOD'):
                            continue

                        if g['label'].endswith(': ACT'):
                            continue


                        if 'label_format' in g:
                            d = LABEL_TO_DICT[g['label_format'][1]]['dict']
                            k = '{subclass}:{key}'.format(**LABEL_TO_DICT[g['label_format'][1]])
                            label = g['label_format'][0].format(d[self.header[k]])
                        else:
                            label = g['label']




                        if replace[1]:
                            measures.append(label.replace(measure, name))
                        else:
                            measures.append(label)


                    meansures_available.extend(measures)

        return modules, modules_active, meansures_available



    #----------------------------------------------------------------------
    def format(self, active, filters=None):
        """Process a subrecord (their raw header), aply shifts and get references.

        Parameters
        ----------
        active : array
            List of groups to parse.
        filters: array, optional
            A sub list of desired subrecords.

        Returns
        -------
        DataFrame
            DataFrame with single row that contains all measures with label
            as headers.

        """
        # if not active:
            # return

        formated = {}

        for measure in self.data:

            if isinstance(measure, tuple):
                measure, replace = measure
            else:
                replace = ['', '']

            # if measure in [st.split(':')[0].split(' ')[0] for st in active]:

            for component in GROUPS_DICT[measure]:
                label = component['label']

                if label.endswith(': ACT') or label.endswith(': MOD'):
                    continue


                if replace[1]:
                    name = '{} ({})'.format(label.strip(), replace[1])
                else:
                    name = label.strip()


                # if filters and not name in filters:
                    # continue

                if filters and not (name in filters):
                    continue

                if 'label_format' in component:
                    d = LABEL_TO_DICT[component['label_format'][1]]['dict']
                    k = '{subclass}:{key}'.format(**LABEL_TO_DICT[component['label_format'][1]])
                    label = component['label_format'][0].format(d[self.header[k]])

                # desc = component['desc']
                key = '{}:{}'.format(component['subclass'], component['key'].replace(*replace))

                shift = component.get('shift', 1)

                if 'dict' in component:

                    dict_ = component['dict']
                    if self.header[key] == 'False':
                        value = dict_[0]
                    elif self.header[key] == 'True':
                        value = dict_[1]
                    else:
                        value = dict_.get(self.header[key], None)

                else:

                    # if isinstance(self.header[key], (int, float)):

                        if key.split(':')[-1].replace('-', '0').isdigit():
                            value = self.header[key]
                            if isinstance(value, (int, float)) and value > CONST.DATA_INVALID:
                                value = value * shift

                        else:
                            value = self.get_short(key)
                            # value = short_value
                            if isinstance(value, (int, float)) and value:
                                if value > CONST.DATA_INVALID:
                                    value =  value * shift

                    # else:
                        # value = self.header[key]


                formated[name] = [value]

        if formated:
            formated['datetime'] = self.date

        return DataFrame(formated)



    #----------------------------------------------------------------------
    def get_short(self, key):
        """From index in header, convert data to integer, validates and return it.

        Parameters
        ----------
        key : Header index
            Location if header of target value.


        Returns
        -------
        int, None, bytearray
            Int if valus is a signed 16 bits, None if the value is over range
            and bytearray in other cases.

        """

        data = self.header[key+',']
        if len(data) == 2:
            value = struct.unpack('>h', bytes(data))[0]
            if value <= CONST.DATA_OVER_RANGE:
                return None
            else:
                return value
        else:
            return self.header[key]



    #----------------------------------------------------------------------
    def check_module(self, label, replace=None):
        """Check the status module from determinate group.

        Parameters
        ----------
        label : str
            Group for check their respective module.
        replace : dict
            Some groups are indexed for multiples modules, in that case, the
            indexes must be removed.

        Returns
        -------
        bool
            Module exist.

        bool
            Module is active.
        """

        mod_exist = LABEL_TO_DICT['{}: MOD'.format(label)]
        mod_activ = LABEL_TO_DICT['{}: ACT'.format(label)]

        if replace[0]:
            e = mod_exist['key'].replace(*replace)
            a = mod_activ['key'].replace(*replace)
        else:
            e = mod_exist['key']
            a = mod_activ['key']

        exist = self.header['{}:{}'.format(mod_exist['subclass'], e)] == 'True'
        activ = self.header['{}:{}'.format(mod_activ['subclass'], a)] == 'True'

        return exist, activ

