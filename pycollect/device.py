"""
=========
GE Device
=========

Connect and request Subrecord and Waveform:

.. code:: ipython3

    device = GEDevice()
    device.connect('/dev/ttyUSB0')

    device.request(subtype=device.DISPL, waveform_set=['PLETH', 'ECG1'])

    device.collect(True)


To clear the buffer input:

.. code:: ipython3

    device.clear_buffer()


To stop the data collecting:

.. code:: ipython3

    device.collect(False)

"""

from struct import pack
from threading import Thread

from .dataconstants import CONST
from .measures import WAVEFORMS_DICT
from .headers import DatexHeaderRequest, DatexHeaderWaveRequest

import serial

########################################################################
class FakeDevice:
    """Debugger class for simulate the input data."""

    #----------------------------------------------------------------------
    def __init__(self, raw_file):
        """Establish the connection and handle the data input from monitor.

        Parameters
        ----------
        raw_file : str, optional
            Input file with raw data.
        """

        self.raw_file = raw_file
        self.raw = self.__read_raw__()

        self.device = None


    #----------------------------------------------------------------------
    def __read_raw__(self):
        """Return generator with the input raw data.

        Returns
        -------
        Generator
            Generator for single bytes.
        """

        file = open(self.raw_file, 'rb')
        data = file.read()
        for d in data:
            yield d


    #----------------------------------------------------------------------
    def connect(self, port, timeout):
        """Establish the connection and debug an unrelated serial device.

        Parameters
        ----------
        port : str
            Serial port.
        timeout : integer
            Timeout for serial comunication.
        """

        self.device = serial.Serial(port, timeout=timeout)

        if self.device:
            return self.device
        else:
            return None


    #----------------------------------------------------------------------
    def read(self, size):
        """Return the input raw file one byte at time.

        Parameters
        ----------
        size: int
            Buffer input size to read.

        Returns
        -------
        list
            Array with raw data.
        """

        # Very important delay
        import time
        time.sleep(0.001)

        if self.device:
            self.device.read(size)

        try:
            return [next(self.raw)]
        except:  #The file will be readed in infinite loop
            self.raw = self.__read_raw__()
            return [next(self.raw)]


    #----------------------------------------------------------------------
    def write(self, data):
        """Write on serial port if available.

        Parameters
        ----------
        data : bytes
            Desired object to write in serial port.
        """

        if self.device:
            self.device.write(data)


    #----------------------------------------------------------------------
    def writable(self):
        """Check if serial port is writable..

        Returns
        ----------
        bool
            Port writable.
        """

        if self.device:
            return self.device.writable()
        else:
            return True


    #----------------------------------------------------------------------
    def close(self):
        """Close the serial port."""

        if self.device:
            return self.device.close()





########################################################################
class GEDevice:
    """Establish the connection and handle the data input from monitor."""

    DISPL = CONST.DRI_PH_DISPL
    TREND_10S = CONST.DRI_PH_10S_TREND
    TREND_60S = CONST.DRI_PH_60S_TREND

    # DEFAULT_REQUEST = ['date', 'ENTROPY RE', 'ENTROPY SE', 'ENTROPY BSR', 'TEMP (t1)', 'NIBP SYS',
                       # 'NIBP DIA', 'NIBP MEAN', 'CO2 ET','CO2 FI','CO2 RR', 'CO2 PAMB', 'O2 ET', 'O2 FI',
                       # 'N2O ET', 'N2O FI', 'AA ET', 'AA FI', 'AA',
                       # 'FLOW-VOL: MSR', 'FLOW-VOL PPEAK', 'FLOW-VOL COMP', 'FLOW-VOL PEEP',
                       # 'FLOW-VOL TV-INSP', 'FLOW-VOL TV-EXP', 'FLOW-VOL MV-EXP',

                       # 'FLOW', 'AA', 'PLETH',
                       # ]


    DEFAULT_REQUEST = ['date',
                       'ENTROPY RE', 'ENTROPY SE', 'ENTROPY BSR',  #disp, numeric, 1 Hz
                       'NIBP SYS','NIBP DIA', 'NIBP MEAN',  #disp, numeric, 1 Hz
                       'ECG IMP-RR',  #disp, numeric, 1 Hz
                       'ECG HR',  #disp, numeric, 1 Hz
                       'TEMP (t1)',  #disp, numeric, 1 Hz
                       'CO2 FI', 'CO2 ET',  #disp, numeric, 1 Hz
                       'ECG1',  #wave, numeric, 300 Hz
                       'ENT_100',  #wave, numeric, 100 Hz
                       'PLETH',  #wave, numeric, 100 Hz
                       ]




    # DEFAULT_REQUEST2 = DEFAULT_REQUEST[:]
    # DEFAULT_REQUEST3 = DEFAULT_REQUEST[:]
    # DEFAULT_REQUEST4 = DEFAULT_REQUEST[:]
    # DEFAULT_REQUEST5 = DEFAULT_REQUEST[:]

    # DEFAULT_REQUEST_LISTS = [DEFAULT_REQUEST,
                             # DEFAULT_REQUEST2,
                             # DEFAULT_REQUEST3,
                             # DEFAULT_REQUEST4,
                             # DEFAULT_REQUEST5,
                             # ]


    #----------------------------------------------------------------------
    def on_connection_loss(self):
        """Overwritable method."""


    #----------------------------------------------------------------------
    def __init__(self, raw_file=None):
        """Establish the connection and handle the data input from monitor.

        Parameters
        ----------
        raw_file : str, optional
            Read from local file, no serial.
        """

        if raw_file:
            self.device = FakeDevice(raw_file)

        self.READING = False
        self.BUFFER = []
        self.FAKE = bool(raw_file)


    #----------------------------------------------------------------------
    def connect(self, port, timeout=1):
        """Establish the connection with the CARESCAPE Monitor Bx50.

          * **Baudrate:** 19200
          * **Parity:** even
          * **Stop bits:** 1
          * **bytesize:** 8 bits
          * **rtscts:** True

        Parameters
        ----------
        port : str
            Serial port address.
        timeout: int, in secods
            Serial port read and write timeout.
        """

        try:
            if self.FAKE:
                if port:
                    self.device.connect(port, timeout)
                return True
            else:
                self.device = serial.Serial(port=port,
                                            baudrate=19200,
                                            timeout=timeout,
                                            parity=serial.PARITY_EVEN,
                                            stopbits=serial.STOPBITS_ONE,
                                            bytesize=serial.EIGHTBITS,

                                            write_timeout=timeout,

                                            rtscts = True,
                                            )

            self.stop()
            return True

        except Exception as e:
            print(e)
            return False


    #----------------------------------------------------------------------
    def close(self):
        """Close serial port"""

        try:
            self.device.close()
        except:
            pass

    #----------------------------------------------------------------------
    def request(self, subtype=None, waveform_set=None, interval=1):
        """Create and send a data request of Subrecord or/and Waveform type.

        Parameters
        ----------
        subtype : subrecord type object
            `DISPL`, `TREND_10S` or `TREND_60S`

        waveform_set: array
            List of waveform types.

        interval: int, in seconds
            If subtype is `DISPL` interval is accepted and must be an integer
            equal or greater to 1.
        """

        # Subtype
        if subtype == self.DISPL:
            # if 0 < interval < 1:
                # interval = 1  #displayed values requiere 5 seconds or more
            if interval < 0:
                interval = int(pack('>h', interval).hex(), 16)

            self.request_transfer(subtype=self.DISPL, interval=interval)

        elif subtype in [self.TREND_10S, self.TREND_60S]:
            interval = 1  #no matter, must be positive.
            self.request_transfer(subtype, interval=interval)

        if waveform_set:
            wave_set = self.create_waveform_set(waveform_set)
            self.request_multiple_wave_transfer(wave_set=wave_set, transmission_type=CONST.WF_REQ_CONT_START)


    #----------------------------------------------------------------------
    def request_transfer(self, subtype, interval):
        """Create and send header of Subrecord type.

        Parameters
        ----------
        subtype : subrecord type object
            `DISPL`, `TREND_10S` or `TREND_60S`

        interval: int, in seconds
            If subtype is `DISPL` interval is accepted and must be an integer
            equal or greater to 5
        """

        request = DatexHeaderRequest()

        request.set('r_len', 49)
        # request.set('r_dri_level', dri_level)
        request.set('r_time', 0)
        request.set('r_maintype', CONST.DRI_MT_PHDB)

        request.set('sr_offset1', 0)
        request.set('sr_type1', 0)  #Physiological data request
        request.set('sr_offset2', 0)
        request.set('sr_type2', CONST.DRI_EOL_SUBR_LIST)  #Last subrecord

        request.set('phdb_rcrd_type', subtype)
        request.set('tx_interval', interval)

        if interval:
            phdb_class_bf = CONST.DRI_PHDBCL_REQ_BASIC_MASK | CONST.DRI_PHDBCL_REQ_EXT1_MASK | CONST.DRI_PHDBCL_REQ_EXT2_MASK | CONST.DRI_PHDBCL_REQ_EXT3_MASK
        else:
            phdb_class_bf = 0x0000

        request.set('phdb_class_bf', phdb_class_bf)

        data = request.request()
        self.write_buffer(data)


    #----------------------------------------------------------------------
    def request_multiple_wave_transfer(self, wave_set, transmission_type):
        """Create and send header of Waveform type.

        Parameters
        ----------
        wave_set : array
            List of constants that represents each waveform type requested, if
            list lenghth is less than 8, the last integer must be 255.

        transmission_type: transmission type object
            `WF_REQ_CONT_START` for start start transmission, `WF_REQ_CONT_STOP`
            for stop it and `WF_REQ_TIMED_START` for request a timed transmission.
        """

        request = DatexHeaderWaveRequest()

        request.set('r_len', 72)  #size of hdr + wfreq type
        # request.set('r_dri_level', dri_level)
        request.set('r_time', 0)
        request.set('r_maintype', CONST.DRI_MT_WAVE)

        request.set('sr_offset1', 0)
        request.set('sr_type1', CONST.DRI_WAVEFORM['CMD'])  #Physiological data request
        request.set('sr_offset2', 0)
        request.set('sr_type2', CONST.DRI_EOL_SUBR_LIST)  #Last subrecord

        request.set('req_type', transmission_type)
        request.set('res', 0)
        request.set('type', wave_set)

        data = request.request()
        self.write_buffer(data)


    #----------------------------------------------------------------------
    def write_buffer(self, data):
        """Check if device is writeble and send the data.

        Parameters
        ----------
        data : bytes array
            Bytes with the header that bust sent to the device.
        """

        # assert self.device.writable(), 'Device is not writable.'
        try:
            self.device.write(data)
        except:
            self.close()
            self.on_connection_loss()


    #----------------------------------------------------------------------
    def create_waveform_set(self, waveform_set):
        """Generate Waveform set.

        Parameters
        ----------
        waveform_set: array
            List of waveform types.

        Returns
        -------
        list
            A list of integer that represent the waveforms desired.
        """

        waveform_type = []
        rample_rate = []

        for waveform in waveform_set:

            if not waveform in CONST.DRI_WAVEFORM:
                raise Exception('Waveform {} is not available'.format(waveform))

            waveform_type.append(CONST.DRI_WAVEFORM[waveform])
            rample_rate.append(WAVEFORMS_DICT[waveform]['samps'])

        # assert sum(rample_rate) <= 600, "Sample rate must be less or equal to 600"
        if sum(rample_rate) > 600:
            raise Exception("Sample rate must be less or equal to 600")

        waveform_type.append(CONST.DRI_EOL_SUBR_LIST)
        waveform_type.extend([0]*(8 - len(waveform_type)))

        return waveform_type[:8]


    #----------------------------------------------------------------------
    def stop_wave_transfer(self):
        """Send the request for stop the Waveform transmission."""

        self.request_multiple_wave_transfer(wave_set=0, transmission_type=CONST.WF_REQ_CONT_STOP)


    #----------------------------------------------------------------------
    def stop_transfer(self):
        """Send the request for stop the Subrecords transmission."""

        self.request_transfer(subtype=self.DISPL, interval=0)
        self.request_transfer(subtype=self.TREND_10S, interval=0)
        self.request_transfer(subtype=self.TREND_60S, interval=0)


    #----------------------------------------------------------------------
    def stop(self):
        """Send the request for stop the Subrecords and Waveform transmission."""

        self.stop_wave_transfer()
        self.stop_transfer()
        # self.device.close()


    #----------------------------------------------------------------------
    def read(self, size=2**12):
        """Write into the data buffer the bytes readed from serial port.

        Parameters
        ----------
        size: integer, 2**12
           Input buffer size.
        """

        size = 2 ** 8

        while self.READING:
            try:
                data = self.device.read(size)
                self.BUFFER.extend(data)
            except serial.SerialException:
                self.READING = False
                self.close()
                self.on_connection_loss()


    #----------------------------------------------------------------------
    def clear_buffer(self):
        """Crear the data buffer, not the serial input buffer."""

        self.BUFFER = []


    #----------------------------------------------------------------------
    def collect(self, flag=True, size=2**12):
        """Enable or disable the continuous data reading.

        Parameters
        ----------
        flag: bool, True
           Enable or disable the continuous data reading.
        size: integer, 2**12
           Input buffer size.

        """
        self.READING = flag

        if self.READING:
            self.thr_read = Thread(target=self.read, args=(size, ))
            self.thr_read.start()

