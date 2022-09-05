"""
=======
Headers
=======

Datex Header
------------

All requests use this header:

+-------------+--------------------------------------------------------------------------+
| **Byte No** | **Description**                                                          |
+-------------+--------------------------------------------------------------------------+
|1            |Start flag: FRAMECHAR                                                     |
+-------------+--------------------------------------------------------------------------+
|2            |(start of header)                                                         |
+-------------+                                                                          |
|3            |Total length = 0031h = 49d bytes (word r_len)                             |
+-------------+--------------------------------------------------------------------------+
|4            |Reserved, set to zero (byte res1)                                         |
+-------------+--------------------------------------------------------------------------+
|5            |Ignored by monitor, set to zero (byte r_dri_level)                        |
+-------------+--------------------------------------------------------------------------+
|6            |Reserved = 0000H (byte res2[2])                                           |
+-------------+                                                                          |
|7            |                                                                          |
+-------------+--------------------------------------------------------------------------+
|8            |Transmission time = 0x00000000, ignored by monitor when sending           |
+-------------+transmission request (dword r_time).                                      |
|9            |                                                                          |
+-------------+                                                                          |
|10           |However, time can be meaningful in outputted messages, which use the      |
+-------------+header of the same structure (dword r_time).                              |
|11           |                                                                          |
+-------------+--------------------------------------------------------------------------+
|12           |Reserved = 00000000H (dword res3)                                         |
+-------------+                                                                          |
|13           |                                                                          |
+-------------+                                                                          |
|14           |                                                                          |
+-------------+                                                                          |
|15           |                                                                          |
+-------------+--------------------------------------------------------------------------+
|16           |Main type of record = DRI_MT_PHDB = 0 (r_maintype)                        |
+-------------+                                                                          |
|17           |                                                                          |
+-------------+--------------------------------------------------------------------------+
|18           |Offset to the first subrecord = 0000H (sr_desc[0].offset)                 |
+-------------+                                                                          |
|19           |                                                                          |
+-------------+--------------------------------------------------------------------------+
|20           |Type of first subrecord, DRI_PH_XMIT_REQ = 0 (sr_desc[0].sr_type)         |
+-------------+--------------------------------------------------------------------------+
|21           |Offset to the second subrecord = 0000H,                                   |
+-------------+calculated from the beginning of the data area after the header part.     |
|22           |Value is not meaningful, since there is only one subrecord in the request |
|             |(sr_desc[1].offset).                                                      |
+-------------+--------------------------------------------------------------------------+
|23           |"No more subrecords" (sr_desc[1].sr_type)                                 |
+-------------+--------------------------------------------------------------------------+
|24           |                                                                          |
+-------------+                                                                          |
|25           |sr_desc[2].offset = 000, no meaning since only one subrecord transmitted. |
+-------------+                                                                          |
|26           |sr_desc[2].sr_type, no meaning                                            |
+-------------+--------------------------------------------------------------------------+
|27           |                                                                          |
+-------------+                                                                          |
|28           |sr_desc[3].offset = 000, no meaning                                       |
+-------------+                                                                          |
|29           |sr_desc[3].sr_type, no meaning                                            |
+-------------+--------------------------------------------------------------------------+
|30           |                                                                          |
+-------------+                                                                          |
|31           |sr_desc[4].offset = 000, no meaning                                       |
+-------------+                                                                          |
|32           |sr_desc[4].sr_type, no meaning                                            |
+-------------+--------------------------------------------------------------------------+
|33           |                                                                          |
+-------------+                                                                          |
|34           |sr_desc[5].offset = 000, no meaning                                       |
+-------------+                                                                          |
|35           |sr_desc[5].sr_type, no meaning                                            |
+-------------+--------------------------------------------------------------------------+
|36           |                                                                          |
+-------------+                                                                          |
|37           |sr_desc[6].offset = 000, no meaning                                       |
+-------------+                                                                          |
|38           |sr_desc[6].sr_type, no meaning                                            |
+-------------+--------------------------------------------------------------------------+
|39           |                                                                          |
+-------------+                                                                          |
|40           |sr_desc[7].offset = 000, no meaning                                       |
+-------------+                                                                          |
|41           |sr_desc[7].sr_type = 0, no meaning                                        |
+-------------+--------------------------------------------------------------------------+
"""

from collections import OrderedDict
from .dataconstants import CONST

datex_header = [  #40 bytes

    ('r_len', [2, 0]),
    ('r_nbr', [1, 0]),
    ('r_dri_level', [1, 0]),
    ('plug_id', [2, 0]),
    ('r_time', [4, 0]),
    ('reserved1', [1, 0]),
    ('reserved2', [1, 0]),
    ('reserved3', [2, 0]),
    ('r_maintype', [2, 0]),

    ('sr_offset1', [2, 0]),
    ('sr_type1', [1, 0]),
    ('sr_offset2', [2, 0]),
    ('sr_type2', [1, 0]),
    ('sr_offset3', [2, 0]),
    ('sr_type3', [1, 0]),
    ('sr_offset4', [2, 0]),
    ('sr_type4', [1, 0]),
    ('sr_offset5', [2, 0]),
    ('sr_type5', [1, 0]),
    ('sr_offset6', [2, 0]),
    ('sr_type6', [1, 0]),
    ('sr_offset7', [2, 0]),
    ('sr_type7', [1, 0]),
    ('sr_offset8', [2, 0]),
    ('sr_type8', [1, 0]),

]


phdb_request = [  #9 bytes

    ('phdb_rcrd_type', [1, 0]),
    ('tx_interval', [2, 0x0a]),
    ('phdb_class_bf', [4, 0]),
    ('reserved', [2, 0]),

]


wave_request = [  #32 bytes

    ('req_type', [2, 0]),
    ('res', [2, 0]),
    ('type', [8, 0]),
    ('reserved', [20, 0]),

]


response = [

    ('data', [1450, 0]),

]


group_hdr = [  #6 bytes

    ('status', [4, 0]),
    ('label', [2, 0]),

]


# Invasive pressures
p_group = [  #14 bytes

    ('hdr', OrderedDict(group_hdr[:])),  #6 bytes

    ('sys', [2, 0]),
    ('dia', [2, 0]),
    ('mean', [2, 0]),

    ('hr', [2, 0]),

]


# Non-invasive blood pressure
nibp_group = [  #14 bytes

    ('hdr', OrderedDict(group_hdr[:])),  #6 bytes

    ('sys', [2, 0]),
    ('dia', [2, 0]),
    ('mean', [2, 0]),

    ('hr', [2, 0]),
]


# ECG
ecg_group = [  #16 bytes

    ('hdr', OrderedDict(group_hdr[:])),  #6 bytes

    ('hr', [2, 0]),

    ('st1', [2, 0]),
    ('st2', [2, 0]),
    ('st3', [2, 0]),

    ('imp_rr', [2, 0]),

]


# Temperature
t_group = [  #8 bytes

    ('hdr', OrderedDict(group_hdr[:])),  #6 bytes

    ('temp', [2, 0]),

]


# SpO2
SpO2_pl_group = [  #14 bytes

    ('hdr', OrderedDict(group_hdr[:])),  #6 bytes

    ('SpO2', [2, 0]),
    ('pr', [2, 0]),
    ('ir_amp', [2, 0]),
    ('SO2', [2, 0]),

]


# CO2
co2_group = [  #14 bytes

    ('hdr', OrderedDict(group_hdr[:])),  #6 bytes

    ('et', [2, 0]),
    ('fi', [2, 0]),
    ('rr', [2, 0]),

    ('amb_press', [2, 0]),

]


# O2
o2_group = [  #10 bytes

    ('hdr', OrderedDict(group_hdr[:])),  #6 bytes

    ('et', [2, 0]),
    ('fi', [2, 0]),

]


# N2O
n2o_group = [  #10 bytes

    ('hdr', OrderedDict(group_hdr[:])),  #6 bytes

    ('et', [2, 0]),
    ('fi', [2, 0]),

]


# Anesthesia agents
aa_group = [  #12 bytes

    ('hdr', OrderedDict(group_hdr[:])),  #6 bytes

    ('et', [2, 0]),
    ('fi', [2, 0]),

    ('mac_sum', [2, 0]),

]


# Flow & volume measurement
flow_vol_group = [  #22 bytes

    ('hdr', OrderedDict(group_hdr[:])),  #6 bytes

    ('rr', [2, 0]),
    ('ppeak', [2, 0]),
    ('peep', [2, 0]),
    ('pplat', [2, 0]),
    ('tv_insp', [2, 0]),
    ('tv_exp', [2, 0]),
    ('compliance', [2, 0]),
    ('mv_exp', [2, 0]),

]

# Cardiac output & wedge pressure
co_wedge_group = [  #14 bytes

    ('hdr', OrderedDict(group_hdr[:])),  #6 bytes

    ('co', [2, 0]),
    ('blood_temp', [2, 0]),
    ('ref', [2, 0]),
    ('pcwp', [2, 0]),

]


nmt_group = [  #12 bytes

    ('hdr', OrderedDict(group_hdr[:])),  #6 bytes

    ('t1', [2, 0]),
    ('tratio', [2, 0]),
    ('ptc', [2, 0]),

]


ecg_extra_group = [  #6 bytes

    ('hr_ecg', [2, 0]),
    ('hr_max', [2, 0]),
    ('hr_min', [2, 0]),

]

svo2_group = [  #8 bytes

    ('hdr', OrderedDict(group_hdr[:])),  #6 bytes
    ('svo2', [2, 0]),

]


ecg_arrh_group = [  #48 bytes

    ('hdr', OrderedDict(group_hdr[:])),  #6 bytes
    ('hr', [2, 0]),
    ('rr_time', [2, 0]),
    ('pvc', [2, 0]),
    ('arrh_reserved', [4, 0]),
    ('reserved', [32, 0]),

]


# ECG_12
ecg_12_group = [  #30 bytes

    ('hdr', OrderedDict(group_hdr[:])),  #6 bytes

    ('stI', [2, 0]),
    ('stII', [2, 0]),
    ('stIII', [2, 0]),
    ('stAVL', [2, 0]),
    ('stAVR', [2, 0]),
    ('stAVF', [2, 0]),
    ('stV1', [2, 0]),
    ('stV2', [2, 0]),
    ('stV3', [2, 0]),
    ('stV4', [2, 0]),
    ('stV5', [2, 0]),
    ('stV6', [2, 0]),

]


# Ext 1 class
ext1_phdb = [  #270 bytes

    ('ecg_arrh', OrderedDict(ecg_arrh_group[:])),  #48 bytes

    # ECG_12
    ('ecg_12', OrderedDict(ecg_12_group[:])),  #30 bytes

    ('reserved', [192, 0])

]


nmt2_group = [  #24 bytes

    ('hdr', OrderedDict(group_hdr[:])),  #6 bytes

    ('reserved', [2, 0]),
    ('nmt_t1', [2, 0]),
    ('nmt_t2', [2, 0]),
    ('nmt_t3', [2, 0]),
    ('nmt_t4', [2, 0]),
    ('nmt_resv1', [2, 0]),
    ('nmt_resv2', [2, 0]),
    ('nmt_resv3', [2, 0]),
    ('nmt_resv4', [2, 0]),

]


# EEG Channel
eeg_channel = [  #16 bytes

    ('ampl', [2, 0]),
    ('sef', [2, 0]),
    ('mf', [2, 0]),
    ('delta_proc', [2, 0]),
    ('theta_proc', [2, 0]),
    ('alpha_proc', [2, 0]),
    ('beta_proc', [2, 0]),
    ('bsr', [2, 0]),

]


# EEG
eeg_group = [  #72 bytes

    ('hdr', OrderedDict(group_hdr[:])),  #6 bytes

    ('femg', [2, 0]),

    # EEG Channel
    ('eeg1', OrderedDict(eeg_channel[:])),  #16 bytes
    ('eeg2', OrderedDict(eeg_channel[:])),  #16 bytes
    ('eeg3', OrderedDict(eeg_channel[:])),  #16 bytes
    ('eeg4', OrderedDict(eeg_channel[:])),  #16 bytes

]


eeg_bis_group = [  #16 bytes

    ('hdr', OrderedDict(group_hdr[:])),  #6 bytes

    ('bis', [2, 0]),
    ('sqi_val', [2, 0]),
    ('emg_val', [2, 0]),
    ('sr_val', [2, 0]),
    ('reserved', [2, 0]),

]


entropy_group = [  #28 bytes

    ('hdr', OrderedDict(group_hdr[:])),  #6 bytes

    ('eeg_ent', [2, 0]),
    ('emg_ent', [2, 0]),
    ('bsr_ent', [2, 0]),
    ('reserved', [16, 0]),

]


eeg2_group = [  #31 bytes

    ('hdr', OrderedDict(group_hdr[:])),  #6 bytes

    ('common_reference', [1, 0]),
    ('montage_label_ch_1_m', [1, 0]),
    ('montage_label_ch_1_p', [1, 0]),
    ('montage_label_ch_2_m', [1, 0]),
    ('montage_label_ch_2_p', [1, 0]),
    ('montage_label_ch_3_m', [1, 0]),
    ('montage_label_ch_3_p', [1, 0]),
    ('montage_label_ch_4_m', [1, 0]),
    ('montage_label_ch_4_p', [1, 0]),
    ('reserved', [16, 0]),

]


ext2_phdb = [  #270 bytes

    # NMT2
    ('nmt2', OrderedDict(nmt2_group[:])),  #24 bytes

    # EEG
    ('eeg', OrderedDict(eeg_group[:])),  #72 bytes

    ('eeg_bis', OrderedDict(eeg_bis_group[:])),  #16 bytes
    ('ent', OrderedDict(entropy_group[:])),  #28 bytes
    ('reserved1', [58, 0]),
    ('eeg2', OrderedDict(eeg2_group[:])),  #31 bytess
    ('reserved', [41, 0]),

]


gasex_group = [  #14 bytes

    ('hdr', OrderedDict(group_hdr[:])),  #6 bytes

    ('vo2', [2, 0]),
    ('vco2', [2, 0]),
    ('ee', [2, 0]),
    ('rq', [2, 0]),

]


flow_vol_group2 = [  #46 bytes

    ('hdr', OrderedDict(group_hdr[:])),  #6 bytes

    ('ipeep', [2, 0]),
    ('pmean', [2, 0]),
    ('raw', [2, 0]),
    ('mv_insp', [2, 0]),
    ('epeep', [2, 0]),
    ('mv_spont', [2, 0]),
    ('ie_ratio', [2, 0]),
    ('insp_time', [2, 0]),
    ('exp_time', [2, 0]),
    ('static_compliance', [2, 0]),
    ('static_pplat', [2, 0]),
    ('static_peepe', [2, 0]),
    ('static_peepi', [2, 0]),
    ('reserved', [14, 0]),

]


bal_gas_group = [  #10 bytes

    ('hdr', OrderedDict(group_hdr[:])),  #6 bytes

    ('et', [2, 0]),
    ('fi', [2, 0]),

]


tono_group = [  #22 bytes

    ('hdr', OrderedDict(group_hdr[:])),  #6 bytes

    ('prco2', [2, 0]),
    ('pr_et', [2, 0]),
    ('pr_pa', [2, 0]),
    ('pa_delay', [2, 0]),
    ('phi', [2, 0]),
    ('phi_delay', [2, 0]),
    ('amb_press', [2, 0]),
    ('cpma', [2, 0]),

]


aa2_group = [  #24 bytes

    ('hdr', OrderedDict(group_hdr[:])),  #6 bytes

    ('mac_age_sum', [2, 0]),
    ('reserved', [16, 0]),

]


ext3_phdb = [  #270 bytes

    ('gasex', OrderedDict(gasex_group[:])),  #14 bytes
    ('flow_vol2', OrderedDict(flow_vol_group2[:])),  #46 bytes
    ('bal', OrderedDict(bal_gas_group[:])),  #10 bytes
    ('tono', OrderedDict(tono_group[:])),  #22 bytes
    ('aa2', OrderedDict(aa2_group[:])),  #24 bytes
    ('reserved', [154, 0]),

]


basic_phdb = [  #270 bytes


    # ECG
    ('ecg', OrderedDict(ecg_group[:])),  #16 bytes

    # Invasive pressures
    ('p1', OrderedDict(p_group[:])),  #14 bytes
    ('p2', OrderedDict(p_group[:])),  #14 bytes
    ('p3', OrderedDict(p_group[:])),  #14 bytes
    ('p4', OrderedDict(p_group[:])),  #14 bytes

    # Non-invasive blood pressure
    ('nibp', OrderedDict(nibp_group[:])),  #14 bytes

    # Temperature
    ('t1', OrderedDict(t_group[:])),  #8 bytes
    ('t2', OrderedDict(t_group[:])),  #8 bytes
    ('t3', OrderedDict(t_group[:])),  #8 bytes
    ('t4', OrderedDict(t_group[:])),  #8 bytes

    # SpO2
    ('SpO2', OrderedDict(SpO2_pl_group[:])),  #14 bytes

    # CO2
    ('co2', OrderedDict(co2_group[:])),  #14 bytes

    # O2
    ('o2', OrderedDict(o2_group[:])),  #10 bytes

    # N2O
    ('n2o', OrderedDict(n2o_group[:])),  #10 bytes

    # Anesthesia agents
    ('aa', OrderedDict(aa_group[:])),  #12 bytes

    # Flow & volume measurement
    ('flow_vol', OrderedDict(flow_vol_group[:])),  #22 bytes


    ('co_wedge', OrderedDict(co_wedge_group[:])),  #14 bytes
    ('nmt', OrderedDict(nmt_group[:])),  #12 bytes
    ('ecg_extra', OrderedDict(ecg_extra_group[:])),  #6 bytes
    ('svo2', OrderedDict(svo2_group[:])),  #8 bytes

    ('p5', OrderedDict(p_group[:])),  #14 bytes
    ('p6', OrderedDict(p_group[:])),  #14 bytes

    ('reserved', [2, 0]),

]



dri_phdb = [  #1088 bytes

    ('time', [4, 0]),

    ('basic', OrderedDict(basic_phdb[:])),  #270 bytes
    ('ext1', OrderedDict(ext1_phdb[:])),  #270 bytes
    ('ext2', OrderedDict(ext2_phdb[:])),  #270 bytes
    ('ext3', OrderedDict(ext3_phdb[:])),  #270 bytes

    ('marker', [1, 0]),
    ('reserved', [1, 0]),
    ('cl_drilvl_subt', [2, 0]),

]



dri_trend10s = [

    ('r_len', [2, 0]),

    ('data01', [2, 0]),
    ('data02', [2, 0]),
    ('data03', [2, 0]),
    ('data04', [2, 0]),
    ('data05', [2, 0]),
    ('data06', [2, 0]),
    ('data07', [2, 0]),
    ('data08', [2, 0]),
    ('data09', [2, 0]),
    ('data10', [2, 0]),
    ('data11', [2, 0]),
    ('data12', [2, 0]),
    ('data13', [2, 0]),
    ('data14', [2, 0]),
    ('data15', [2, 0]),
    ('data16', [2, 0]),
    ('data17', [2, 0]),
    ('data18', [2, 0]),
    ('data19', [2, 0]),
    # ('data20', [2, 0]),


]



########################################################################
class HeaderHandler:
    """Header Handler.

    Establish a way to read and write GE protocol headers.
    """

    #----------------------------------------------------------------------
    def __init__(self, data=None, init=None, size=None):
        """

        Parameters
        ----------
        data : array
            Load an array to build the header.
        init : OrderedDict
            Initialize the the data header with this values.
        size : str
            Define the size in bytes of the current header.
        """

        if init:
            self.DATA = init
            self.LENGTH = size
        else:
            self.DATA = OrderedDict(self.DATA)

        bytes_ = self.__length__(self.DATA)
        assert bytes_ == self.LENGTH, 'Size must be {} no {}.'.format(self.LENGTH, bytes_)

        if data:
            self.load(data)


    #----------------------------------------------------------------------
    def __length__(self, header):
        """Calculate the bytes length of the current header.

        Parameters
        ----------
        header : dict
            Target header in dict format for calculate the size.

        Returns
        -------
        int
            Number of bytes used by the header.
        """

        bytes_ = 0
        for v in header.items():
            if isinstance(v[1], OrderedDict):
                bytes_ += self.__length__(v[1])
            else:
                bytes_ += v[1][0]
        return bytes_


    #----------------------------------------------------------------------
    def set(self, element, value):
        """Modify the value of one header element.

        Parameters
        ----------
        element : str
            Header element.
        value : str
            New value for element.
        """

        assert element in self.DATA, '{} is not part of this header'.format(element)
        self.DATA[element][1] = value


    #----------------------------------------------------------------------
    def load(self, data):
        """Load the `data` into the current header values.

        Parameters
        ----------
        data : array
            Load an array to build the header.
        """

        bytes_ = 0
        inset_data = []

        for element, field in self.DATA.items():

            if isinstance(field, OrderedDict):
                size = self.__length__(field)
                value = data[bytes_:bytes_+size]
                inset_data.append(HeaderHandler(data=value, init=self.DATA[element], size=size).DATA.copy())
                bytes_ = bytes_+size

            else:
                size, _ = field
                value = data[bytes_:bytes_+size]
                value = list(reversed(value))
                inset_data.append(value[:])
                bytes_ = bytes_+size

        index = 0
        for element in self.DATA:
            e = inset_data[index]
            if isinstance(e, list):
                self.DATA[element][1] = inset_data[index][:]
                self.DATA[element] = self.DATA[element][:]

            else:
                self.DATA[element] = inset_data[index]
            index += 1


    #----------------------------------------------------------------------
    def __getitem__(self, element):
        """Return value from header.

        Parameters
        ----------
        element : str
            Define de index and the format of requested value.

        Returns
        -------
        int, list, HeaderHandler
            Target element, could be of many types due to the nested suported format.

        Note
        ----
        recursive format:
            header['basic:ecg:hr']
        reverse the byte array before to read:
            header['-basic:ecg:hr']
        return the byte array without convert to integer:
            header['basic:ecg:hr,']
        return the boolean for the bit `4`:
            header['basic:ecg:hr:4]
        return the integer generated with the bits `0` to `5`:
            header['basic:ecg:hr:0-5]
        """

        target = self.DATA

        # if format is reversed
        reverse = False
        if element.startswith('-'):
            element = element[1:]
            reverse = True

        # if single index and request is a list
        if element.count(':') == 0 and element.endswith(','):
            value = target[element[:-1]][1]
            if reverse:
                return list(reversed(value))
            return value

        # if multiple index
        if ':' in element:
            args = element.split(':')
            for arg in args:

                # if index is a list
                if arg.endswith(','):
                    if reverse:
                        return reversed(target[arg[:-1]][1])
                    return target[arg[:-1]][1]

                else:
                    # if index is a numeric index.
                    if arg.isdigit():
                        dd = self.to32bits(target[1])
                        if not reverse:
                            dd = list(reversed(dd))
                        return str(bool(int(dd[int(arg)])))

                    # if index is a range
                    elif arg.replace('-', '0').isdigit():
                        l, h = [int(_) for _ in arg.split('-')]
                        return int(''.join(map(str, self.to32bits(target[1])[l:h+1])), 2)

                    # normal index
                    else:
                        target = target[arg]

        # normal index
        else:
            target = target[element]

        if isinstance(target, OrderedDict):
            return target

        elif isinstance(target, list):
            value = target[1]

            # an integer
            if isinstance(value, int):
                return value

            # a single element array
            elif isinstance(value, list) and len(value)==1:
                return value[0]

            # a multiple element array
            return int(bytes(value).hex(), 16)


    #----------------------------------------------------------------------
    def to32bits(self, value):
        """Convert a value into a 32 bits array.

        Parameters
        ----------
        value : array, int
            A length 4 array or integer value, if integer then it will be converted to [0, 0, 0, value].

        Returns
        -------
        list
            List of 32 bits that represents the input value.
        """

        if isinstance(value, int):
            value = [0, 0, 0, value]

        return list(''.join(['{:08b}'.format(_) for _ in value]))


    #----------------------------------------------------------------------
    def array(self):
        """Return the sorted byte array with the correct size.

        If one element is defined as 2 bytes length, this must be splitted and
        completed (if necessary) with an empty byte.

        Returns
        -------
        list
            Single array with data header values, linke in C, C++, C#.
        """

        array = []
        for _, v in self.DATA.items():
            bytes_, value = v
            if isinstance(value, (list, tuple, set)):
                array.extend(value)
            else:
                array.extend([d for d in (value).to_bytes(bytes_, 'little')])  #no change

        assert len(array) == self.LENGTH, 'Array size must be {}'.format(self.LENGTH)

        return array


    #----------------------------------------------------------------------
    def request(self):
        """Generate the final header.

        Returns
        -------
        list
            The main data with `start-flag`, `checksum` and `end-flag`.
        """

        data = self.array()

        framebyte = [CONST.CTRLCHAR, CONST.FRAMECHAR & CONST.BIT5COMPL]
        ctrlbyte = [CONST.CTRLCHAR, CONST.CTRLCHAR & CONST.BIT5COMPL]

        buffer = []
        check_sum = 0
        buffer.append(CONST.FRAMECHAR)

        for byte in data:

            if byte == CONST.FRAMECHAR:
                buffer.extend(framebyte)
                check_sum += sum(framebyte)

            elif byte == CONST.CTRLCHAR:
                buffer.extend(ctrlbyte)
                check_sum += sum(ctrlbyte)

            else:
                buffer.append(byte)
                check_sum += byte
                check_sum = (check_sum).to_bytes(4, 'big')[-1]

        buffer.extend([check_sum, CONST.FRAMECHAR])

        return buffer



########################################################################
class DatexHeaderRequest(HeaderHandler):
    """Header for request transfer.

    This header is the combination of `Datex Header` and the follow header:

    +-------------+--------------------------------------------------------------------------+
    | **Byte No** | **Description**                                                          |
    +-------------+--------------------------------------------------------------------------+
    |42           |Request current values of physiological database = DRI_PH_DISPL           |
    |             |(field phdb_rcrd_type of struct phdb_req)                                 |
    +-------------+--------------------------------------------------------------------------+
    |43           |Transmission interval in seconds = 00A, i.e., send current values of      |
    +-------------+physiological database every 10 seconds                                   |
    |44           |(field tx_interval of struct phdb_req)                                    |
    +-------------+--------------------------------------------------------------------------+
    |45           |                                                                          |
    +-------------+                                                                          |
    |46           |reserved[0] of struct phdb_req, must be zeroed                            |
    +-------------+--------------------------------------------------------------------------+
    |47           |                                                                          |
    +-------------+                                                                          |
    |48           |reserved[1] of struct phdb_req, must be zeroed                            |
    +-------------+--------------------------------------------------------------------------+
    |49           |                                                                          |
    +-------------+                                                                          |
    |50           |reserved[2] of struct phdb_req, must be zeroed                            |
    +-------------+--------------------------------------------------------------------------+
    |51           |Checksum                                                                  |
    +-------------+--------------------------------------------------------------------------+
    |52           |End flag: FRAMECHAR                                                       |
    +-------------+--------------------------------------------------------------------------+
    """
    LENGTH = 49  #without checksum and flags

    #----------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        """"""
        self.DATA = datex_header + phdb_request
        super().__init__(*args, **kwargs)


    #----------------------------------------------------------------------
    def __str__(self):
        """"""
        return '{}:{}bytes'.format('DatexHeaderRequest', self.LENGTH)



########################################################################
class DatexHeaderWaveRequest(HeaderHandler):
    """Header for request wave transfer.

    This header is the combination of `Datex Header` and the follow header, is
    user for create the recuest of waveforms.

    +-------------+--------------------------------------------------------------------------+
    | **Byte No** | **Description**                                                          |
    +-------------+--------------------------------------------------------------------------+
    |42           |Request type: one of WF_REQ_CONT_START, WF_REQ_CONT_STOP or               |
    +-------------+WF_REQ_TIMED_START.                                                       |
    |43           |                                                                          |
    +-------------+--------------------------------------------------------------------------+
    |44           |Duration of snapshot                                                      |
    +-------------+                                                                          |
    |45           |                                                                          |
    +-------------+--------------------------------------------------------------------------+
    |46-53        |An array of the requested waveform subrecords.                            |
    |             |There is room for up to 8 waveforms, but the monitor sends only the       |
    |             |waveforms that fit within the 600 samples/s limitation and ignores the    |
    |             |rest.                                                                     |
    |             |The type array must be terminated using the DRI_EOL_SUBR_LIST constant    |
    |             |(0xFF), unless there are 8 waveforms is the request.                      |
    +-------------+--------------------------------------------------------------------------+
    |54-73        |Reserved                                                                  |
    +-------------+--------------------------------------------------------------------------+
    |74           |Checksum                                                                  |
    +-------------+--------------------------------------------------------------------------+
    |75           |End flag: FRAMECHAR                                                       |
    +-------------+--------------------------------------------------------------------------+
    """
    LENGTH = 72 #without checksum and flags

    #----------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        """"""
        self.DATA = datex_header + wave_request
        super().__init__(*args, **kwargs)


    #----------------------------------------------------------------------
    def __str__(self):
        """"""
        return '{}:{}bytes'.format('DatexHeaderWaveRequest', self.LENGTH)



########################################################################
class DatexHeaderResponse(HeaderHandler):
    """The data transmitted from monitor is writed in this header.

    This header is the combination of `Datex Header` and the follow header, is
    used for store the waveforms inputs.

    +-------------+--------------------------------------------------------------------------+
    | **Byte No** | **Description**                                                          |
    +-------------+--------------------------------------------------------------------------+
    |42-1491      |Data                                                                      |
    +-------------+--------------------------------------------------------------------------+
    |1492         |Checksum                                                                  |
    +-------------+--------------------------------------------------------------------------+
    |1493         |End flag: FRAMECHAR                                                       |
    +-------------+--------------------------------------------------------------------------+
    """

    LENGTH = 1490 #without checksum and flags

    #----------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        """"""
        self.DATA = datex_header + response
        super().__init__(*args, **kwargs)


    #----------------------------------------------------------------------
    def __str__(self):
        """"""
        return '{}:{}bytes'.format('DatexHeaderResponse', self.LENGTH)



########################################################################
class PhysiologicalData(HeaderHandler):
    """The data transmitted from monitor is writed in this header.

    This header is the combination of `Datex Header` and the follow header, is
    used for store the requested subrecords.

    +-------------+--------------------------------------------------------------------------+
    | **Byte No** | **Description**                                                          |
    +-------------+--------------------------------------------------------------------------+
    |0-4          |Time                                                                      |
    +-------------+--------------------------------------------------------------------------+
    |5-274        |`basic` subclass                                                          |
    +-------------+--------------------------------------------------------------------------+
    |275-544      |`ext1` subclass                                                           |
    +-------------+--------------------------------------------------------------------------+
    |545-814      |`ext2` subclass                                                           |
    +-------------+--------------------------------------------------------------------------+
    |815-1084     |`ext3` subclass                                                           |
    +-------------+--------------------------------------------------------------------------+
    |1085         |Marker, contains the number of latest entered mark.                       |
    +-------------+--------------------------------------------------------------------------+
    |1086         |contains control information for patient data management functions, used  |
    |             |internally by the monitor.                                                |
    +-------------+--------------------------------------------------------------------------+
    |1087-1088    |The last word of the subrecord, contains                                  |
    |             | * The physiological data record class.                                   |
    |             | * The current D-O Record Interface level.                                |
    |             | * The subrecord type.                                                    |
    +-------------+--------------------------------------------------------------------------+
    """

    LENGTH = 1088 #without checksum and flags

    #----------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        """"""
        self.DATA = dri_phdb
        super().__init__(*args, **kwargs)


    #----------------------------------------------------------------------
    def __str__(self):
        """"""
        return '{}:{}bytes'.format('PhysiologicalData', self.LENGTH)



