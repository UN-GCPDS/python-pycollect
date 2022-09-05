from datetime import datetime, date

import pyedflib

########################################################################
class EDFChannel:
    """New EDF+ channel."""

    #----------------------------------------------------------------------
    def __init__(self, data, **kwargs):
        """New channel.

        Parameters
        ----------

        data: array, required

        label: str, recommended
            channel label (string, <= 16 characters, must be unique

        dimension: str, recommended
            physical dimension (e.g., mV) (string, <= 8 characters)

        sample_rate: int, required
            sample frequency in hertz

        physical_max: float, required
            maximum physical value

        physical_min: float, required
            minimum physical value

        digital_max: int, optional
            maximum digital value (int, -2**15 <= x < 2**15)

        digital_min: int, optional
            minimum digital value (int, -2**15 <= x < 2**15)

        transducer: str, optional
            sets the transducer used in this channel

        prefilter: str, optional
            sets the prefilter used in this chanel ("HP:0.1Hz", "LP:75Hz N:50Hz", etc.)
        """

        self.channel = {}
            # 'label': None,
            # 'dimension': None,
            # 'sample_rate': None,
            # 'physical_max': None,
            # 'physical_min': None,
            # 'digital_max': None,
            # 'digital_min': None,
            # 'transducer': None,
            # 'prefilter': None,
            # }
        self.channel.update(kwargs)

        self.data = data


    # #----------------------------------------------------------------------
    # def set_data(self, data):
        # """"""
        # self.data = data


    #----------------------------------------------------------------------
    def __setitem__(self, item, value):
        """"""
        self.channel[item] = value



########################################################################
class EDF:
    """Create an EDF+ file format."""

    #----------------------------------------------------------------------
    def __init__(self, filename):
        """Create an EDF+ file format.

        Parameters
        ----------
        filename : str
            Filename for new EDF+ file.
        """

        self.filename = filename

        self.channel_info = []
        self.data_list = []
        self.anotations = []


    #----------------------------------------------------------------------
    def add_channel(self, channel):
        """Add new chanel to current EDF+.

        Parameters
        ----------
        chanel : EDFChannel object
        """

        self.channel_info.append(channel.channel)
        self.data_list.append(channel.data)


    #----------------------------------------------------------------------
    def save(self):
        """Save as EDF+ file."""

        f = pyedflib.EdfWriter(self.filename, len(self.channel_info), file_type=pyedflib.FILETYPE_EDFPLUS)

        f.setHeader(self.header)
        f.setSignalHeaders(self.channel_info)
        f.writeSamples(self.data_list)

        f.close()


    #----------------------------------------------------------------------
    def write_annotation(self, onset, description, duration=-1):
        """Writes an annotation/event to the file.

        Parameters
        ----------
        onset: int
            Second, where happened the annotation

        duration: int, optional
            Duration of event anotated

        description: str
            Description of event
        """

        self.anotations.append((onset, duration, description))


    #----------------------------------------------------------------------
    def set_header(self, **kwargs):
        """Sets the file header.

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

        self.header = {
            "admincode": '',
            "birthdate": date(1900, 1, 1),
            "equipment": '',
            "gender": 0,
            "patientcode": '',
            "patientname": '',
            "patient_additional": '',
            "recording_additional": '',
            "startdate": datetime.now(),
            "technician": '',
            }

        self.header.update(kwargs)
