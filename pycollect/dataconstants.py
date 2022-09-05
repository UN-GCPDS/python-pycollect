
########################################################################
class CONST:
    """"""

    # Data validity macros
    DATA_INVALID_LIMIT = 	-32001  #limit for special invalid data values
    DATA_INVALID = 		-32767  #there is no valid data
    DATA_NOT_UPDATED = 		-32766  #data is not updated
    DATA_DISCONT = 		-32765  #data discontinuity (calibration ...)
    DATA_UNDER_RANGE = 		-32764  #data exceeds lower valid limit
    DATA_OVER_RANGE = 		-32763  #data exceeds upper valid limit
    DATA_NOT_CALIBRATED = 	-32762  #data is not calibrated


    # Asynchronous interface specific constants
    FRAMECHAR = 	0x7E
    CTRLCHAR = 		0x7D
    BIT5 = 		0x7C
    BIT5COMPL = 	0x5F


    # # # Datex Record Interface data structure definitions
    # # DRI_MAX_SUBRECS = 8  # of subrecords in a packet
    # # DRI_MAX_PHDBRECS = 5  # of phys.db records in a packet


    # # data packet maintypes
    DRI_MT_PHDB = 0  #Physiological data and related transmission requests.
    DRI_MT_WAVE = 1  #Waveform data and related transmission requests.
    # DRI_MT_ALARM = 4  #Alarm data and related transmission requests.


    # Data packet subtypes
    DRI_PH = 		0
    DRI_PH_DISPL = 	1
    DRI_PH_10S_TREND = 	2
    DRI_PH_60S_TREND = 	3
    DRI_PH_AUX = 	4

    # DRI_TREND_DOWN_CTRL = 5
    # DRI_TREND_DOWN_REQ = 6



    DRI_PHDBCL_REQ_BASIC_MASK = 	0x0000      #Enable sending of Basic physiological data class
    DRI_PHDBCL_DENY_BASIC_MASK = 	0x0001     #Disable sending of Basic physiological data class
    DRI_PHDBCL_REQ_EXT1_MASK = 		0x0002       #Enable sending of Ext1 physiological data class
    DRI_PHDBCL_REQ_EXT2_MASK = 		0x0004       #Enable sending of Ext2 physiological data class
    DRI_PHDBCL_REQ_EXT3_MASK = 		0x0008       #Enable sending of Ext3 physiological data class

    # DRI_PHDBCL_BASIC =	0
    # DRI_PHDBCL_EXT1 = 	1
    # DRI_PHDBCL_EXT2 = 	2
    # DRI_PHDBCL_EXT3 = 	3


    # Datex Record Interface level types
    # DRI_LEVEL_95 = 0x02
    # DRI_LEVEL_97 = 0x03
    # DRI_LEVEL_98 = 0x04
    # DRI_LEVEL_99 = 0x05
    # DRI_LEVEL_2000 = 0x06
    # DRI_LEVEL_2001 = 0x07
    # DRI_LEVEL_2003 = 0x08
    # DRI_LEVEL_2005 = 0x09

    WF_REQ_CONT_START = 	0
    WF_REQ_CONT_STOP = 		1
    WF_REQ_TIMED_START = 	2


    DRI_EOL_SUBR_LIST = 0xFF
    DRI_WAVEFORM = {

        'CMD': 			0,  #is used to carry transmission requests to the monitor
        'ECG1': 		1,
        'ECG2': 		2,
        'ECG3': 		3,
        'INVP1': 		4,
        'INVP2': 		5,
        'INVP3': 		6,
        'INVP4': 		7,
        'PLETH': 		8,
        'CO2': 			9,
        'O2': 			10,
        'N2O': 			11,
        'AA_WAVE': 		12,
        'AWP': 			13,
        'FLOW': 		14,
        'RESP': 		15,
        'INVP5': 		16,
        'INVP6': 		17,
        'EEG1': 		18,
        'EEG2': 		19,
        'EEG3': 		20,
        'EEG4': 		21,
        'VOL': 			23,
        'TONO_PRESS': 		24,
        'SPI_LOOP_STATUS': 	29,
        'ENT_100': 		32,
        'EEG_BIS': 		35,

    }
