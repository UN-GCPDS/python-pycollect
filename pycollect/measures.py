"""
========
Measures
========

All measurement data is represented as signed 16-bit values. Some control
information is embedded into the measurement data by assigning special meaning
to certain values.

As values with special meaning start from -32001 downwards, the smallest valid
value is always -32000.

.. include:: ../content/measures.rst

"""

GROUPS = [

########################################################################
# ECG

# The heart rate value is not necessarily from the ECG measurement but is
# based on the monitor's heart rate source selection.

{'label': 'ECG HR',
 'name': 'HR',
 'desc': 'Heart rate',
 'key': 'ecg:hr',
 'unit': '1/min',
 'shift': 1,
 'subclass': 'basic',
 'transducer': '',
 'prefilter': '',
 'physical_min': 0,
 'physical_max': 32768,
 },


# St values are calculated from currently selected user leads Ecg1-3.
# Labels in hdr indicates selected label. Only if selected one of V1-V6
# then label is set to V. (ext1 group includes 12-lead st values.

{'label': 'ECG ST1',
 'name': 'ST1',
 'desc': 'St-level',
 'key': 'ecg:st1',
 'unit': 'mm',
 'shift': 1/100,
 'subclass': 'basic',
 },

{'label': 'ECG ST2',
 'name': 'ST2',
 'desc': 'St-level',
 'key': 'ecg:st2',
 'unit': 'mm',
 'shift': 1/100,
 'subclass': 'basic',
 },

{'label': 'ECG ST3',
 'name': 'ST3',
 'desc': 'St-level',
 'key': 'ecg:st2',
 'unit': 'mm',
 'shift': 1/100,
 'subclass': 'basic',
 },

# Based on measurement of ECG impedance.
{'label': 'ECG IMP-RR',
 'name': 'Imped.',
 'desc': 'Respiration rate',
 'key': 'ecg:imp_rr',
 'unit': '1/min',
 'shift': 1,
 'subclass': 'basic',
 'transducer': '',
 'prefilter': '',
 'physical_min': 0,
 'physical_max': 32768,
 },

#----------------------------------------------------------------------
# Status

{'label': 'ECG: MOD',
 'desc': 'Measurement module existence',
 'key': 'ecg:hdr:status:0',
 'subclass': 'basic',
 },

{'label': 'ECG: ACT',
 'desc': 'Measurement activity',
 'key': 'ecg:hdr:status:1',
 'subclass': 'basic',
 },

{'label': 'ECG: ASY',
 'desc': 'Asystole',
 'key': 'ecg:hdr:status:2',
 'subclass': 'basic',
 },

{'label': 'ECG HR-SRC',
 'desc': 'Heart rate source',
 'key': 'ecg:hdr:status:3-6',
 'subclass': 'basic',
 'dict': {0: 'Not selected',
          1: 'ECG',
          2: 'Invasive pressure channel 1',
          3: 'Invasive pressure channel 2',
          4: 'Invasive pressure channel 3',
          5: 'Invasive pressure channel 4',
          6: 'SpO2',
          7: 'Invasive pressure channel 5',
          8: 'Invasive pressure channel 6',
          },
 },

{'label': 'ECG: NS',
 'desc': 'Noise',
 'key': 'ecg:hdr:status:7',
 'subclass': 'basic',
 },

{'label': 'ECG: AR',
 'desc': 'Artifact',
 'key': 'ecg:hdr:status:8',
 'subclass': 'basic',
 },

{'label': 'ECG: LRN',
 'desc': 'Learning',
 'key': 'ecg:hdr:status:9',
 'subclass': 'basic',
 },

{'label': 'ECG: PCR',
 'desc': 'Pacer On',
 'key': 'ecg:hdr:status:10',
 'subclass': 'basic',
 },

{'label': 'ECG: CH1',
 'desc': 'Channel 1 off',
 'key': 'ecg:hdr:status:11',
 'subclass': 'basic',
 },

{'label': 'ECG: CH2',
 'desc': 'Channel 2 off',
 'key': 'ecg:hdr:status:12',
 'subclass': 'basic',
 },

{'label': 'ECG: CH3',
 'desc': 'Channel 3 off',
 'key': 'ecg:hdr:status:13',
 'subclass': 'basic',
 },

#----------------------------------------------------------------------
# Label

{'label': 'ECG LEAD-CH1',
 'desc': 'Lead configuration for channel 1',
 'key': 'ecg:hdr:label:0-3',
 'subclass': 'basic',
 'dict': {0: 'Not selected',
          1: 'ECG I',
          2: 'ECG II',
          3: 'ECG III',
          4: 'ECG AVR',
          5: 'ECG AVL',
          6: 'ECG AVF',
          7: 'ECG V',
          },
 },

{'label': 'ECG LEAD-CH2',
 'desc': 'Lead configuration for channel 2',
 'key': 'ecg:hdr:label:4-7',
 'subclass': 'basic',
 'dict': {0: 'Not selected',
          1: 'ECG I',
          2: 'ECG II',
          3: 'ECG III',
          4: 'ECG AVR',
          5: 'ECG AVL',
          6: 'ECG AVF',
          7: 'ECG V',
          },
 },

{'label': 'ECG LEAD-CH3',
 'desc': 'Lead configuration for channel 3',
 'key': 'ecg:hdr:label:8-11',
 'subclass': 'basic',
 'dict': {0: 'Not selected',
          1: 'ECG I',
          2: 'ECG II',
          3: 'ECG III',
          4: 'ECG AVR',
          5: 'ECG AVL',
          6: 'ECG AVF',
          7: 'ECG V',
          },
 },


########################################################################
# Invasive blood pressures

{'label': 'INV-BP SYS',
 'name': 'P1sys',
 'desc': 'Invasive pressure',
 'key': 'p_group:sys',
 'unit': 'mmHg',
 'shift': 1/100,
 'subclass': 'basic',
 },

{'label': 'INV-BP DIA',
 'name': 'P1dia',
 'desc': 'Invasive pressure',
 'key': 'p_group:dia',
 'unit': 'mmHg',
 'shift': 1/100,
 'subclass': 'basic',
 },

{'label': 'INV-BP MEAN',
 'name': 'P1mea',
 'desc': 'Invasive pressure',
 'key': 'p_group:mean',
 'unit': 'mmHg',
 'shift': 1/100,
 'subclass': 'basic',
 },

{'label': 'INV-BP HR',
 'name': 'PR(P1)',
 'desc': 'Pulse rate',
 'key': 'p_group:hr',
 'unit': '1/min',
 'shift': 1,
 'subclass': 'basic',
 },

#----------------------------------------------------------------------
# Status

{'label': 'INV-BP: MOD',
 'desc': 'Measurement module existence',
 'key': 'p_group:hdr:status:0',
 'subclass': 'basic',
 },

{'label': 'INV-BP: ACT',
 'desc': 'Measurement activity',
 'key': 'p_group:hdr:status:1',
 'subclass': 'basic',
 },

{'label': 'INV-BP: ZR',
 'desc': 'Zeroing',
 'key': 'p_group:hdr:status:2',
 'subclass': 'basic',
 },

#----------------------------------------------------------------------
# Label

{'label': 'INV-BP LBL',
 'desc': 'Invasive pressure label',
 'key': 'p_group:hdr:label',
 'subclass': 'basic',
 'dict': {0: 'Not defined',
          1: 'ART',
          2: 'CVP',
          3: 'PA',
          4: 'RAP',
          5: 'RVP',
          6: 'LAP',
          7: 'ICP',
          8: 'ABP',
          9: 'P1',
          10: 'P2',
          11: 'P3',
          12: 'P4',
          13: 'P5',
          14: 'P6',
          },
 },


########################################################################
# Non-invasive blood pressure

{'label': 'NIBP SYS',
 'name': 'NIBPsy',
 'desc': 'Invasive pressure',
 'key': 'nibp:sys',
 'unit': 'mmHg',
 'shift': 1/100,
 'subclass': 'basic',
 'transducer': '',
 'prefilter': '',
 'physical_min': 0,
 'physical_max': 327,
 },

{'label': 'NIBP DIA',
 'name': 'NIBPdi',
 'desc': 'Invasive pressure',
 'key': 'nibp:dia',
 'unit': 'mmHg',
 'shift': 1/100,
 'subclass': 'basic',
 'transducer': '',
 'prefilter': '',
 'physical_min': 0,
 'physical_max': 327,
 },

{'label': 'NIBP MEAN',
 'name': 'NIBPm',
 'desc': 'Invasive pressure',
 'key': 'nibp:mean',
 'unit': 'mmHg',
 'shift': 1/100,
 'subclass': 'basic',
 'transducer': '',
 'prefilter': '',
 'physical_min': 0,
 'physical_max': 327,
 },

{'label': 'NIBP HR',
 'name': 'PR(NIBP)',
 'desc': 'Pulse rate',
 'key': 'nibp:hr',
 'unit': '1/min',
 'shift': 1,
 'subclass': 'basic',
 },

#----------------------------------------------------------------------
# Status

{'label': 'NIBP: MOD',
 'desc': 'Measurement module existence',
 'key': 'nibp:hdr:status:0',
 'subclass': 'basic',
 },

{'label': 'NIBP: ACT',
 'desc': 'Measurement activity',
 'key': 'nibp:hdr:status:1',
 'subclass': 'basic',
 },

#----------------------------------------------------------------------
# Label

{'label': 'NIBP CUFF',
 'desc': 'Invasive pressure cuff type',
 'key': 'nibp:hdr:label:0-2',
 'subclass': 'basic',
 'dict': {0: 'Not defined',
          1: 'Infant',
          2: 'Reserved',
          3: 'Adult',
          },
 },

{'label': 'NIBP: AUTO',
 'desc': 'Invasive pressure: AUTO mode selected',
 'key': 'nibp:hdr:label:3',
 'subclass': 'basic',
 },

{'label': 'NIBP: STAT',
 'desc': 'Invasive pressure: STAT mode selected',
 'key': 'nibp:hdr:label:4',
 'subclass': 'basic',
 },

{'label': 'NIBP: MSR',
 'desc': 'Invasive pressure: measuring',
 'key': 'nibp:hdr:label:5',
 'subclass': 'basic',
 },

{'label': 'NIBP: STASIS',
 'desc': 'Invasive pressure: STASIS ON',
 'key': 'nibp:hdr:label:6',
 'subclass': 'basic',
 },

{'label': 'NIBP: CLBR',
 'desc': 'Invasive pressure: calibrating',
 'key': 'nibp:hdr:label:7',
 'subclass': 'basic',
 },

{'label': 'NIBP: OLD',
 'desc': 'Invasive pressure: data is older than 60s',
 'key': 'nibp:hdr:label:8',
 'subclass': 'basic',
 },


########################################################################
# Temperatures

{'label': 'TEMP',
 'name': 'T1',
 'desc': 'Temperature',
 'key': 't_group:temp',
 'unit': '\N{DEGREE SIGN}C',
 'shift': 1/100,
 'subclass': 'basic',
 'transducer': '',
 'prefilter': '',
 'physical_min': None,
 'physical_max': None,
 },

#----------------------------------------------------------------------
# Status

{'label': 'TEMP: MOD',
 'desc': 'Measurement module existence',
 'key': 't_group:hdr:status:0',
 'subclass': 'basic',
 },

{'label': 'TEMP: ACT',
 'desc': 'Measurement activity',
 'key': 't_group:hdr:status:1',
 'subclass': 'basic',
 },

#----------------------------------------------------------------------
# Label

{'label': 'TEMP LBL',
 'desc': 'Temperature label',
 'key': 't_group:hdr:label',
 'subclass': 'basic',
 'dict': {0: 'Not used',
          1: 'ESO',
          2: 'NASO',
          3: 'TYMP',
          4: 'RECT',
          5: 'BLAD',
          6: 'AXIL',
          7: 'SKIN',
          8: 'AIRW',
          9: 'ROOM',
          10: 'MYO',
          11: 'T1',
          12: 'T2',
          13: 'T3',
          14: 'T4',
          15: 'CORE',
          16: 'SURF',
          },
 },

########################################################################
#SpO2

{'label': 'SpO2',
 'name': 'SpO2',
 'desc': 'Oxygenation percentage',
 'key': 'SpO2:SpO2',
 'unit': '%',
 'shift': 1/100,
 'subclass': 'basic',
 },

{'label': 'SpO2 PR',
 'name': 'PR(SpO2)',
 'desc': 'Pulse rate',
 'key': 'SpO2:pr',
 'unit': '1/min',
 'shift': 1,
 'subclass': 'basic',
 },

{'label': 'SpO2 IR-AMP',
 'name': 'SpO2_ir',
 'desc': 'Modulation',
 'key': 'SpO2:ir_amp',
 'unit': '%',
 'shift': 1,
 'subclass': 'basic',
 },

{'label': 'SpO2 [SO2|SaO2|SvO2]',
 'name': 'SvO2p',
 'label_format': ['SpO2 {}', 'SpO2 LBL'],
 'desc': 'Modulation, value is specified by the label.',
 'key': 'SpO2:SO2',
 'unit': '%',
 'shift': 1/100,
 'subclass': 'basic',
 },

#----------------------------------------------------------------------
# Status

{'label': 'SpO2: MOD',
 'desc': 'Measurement module existence',
 'key': 'SpO2:hdr:status:0',
 'subclass': 'basic',
 },

{'label': 'SpO2: ACT',
 'desc': 'Measurement activity',
 'key': 'SpO2:hdr:status:1',
 'subclass': 'basic',
 },

#----------------------------------------------------------------------
# Label

{'label': 'SpO2 LBL',
 'desc': 'Measurement module existence',
 'key': 'SpO2:hdr:label:0-1',
 'subclass': 'basic',
 'dict': {0: 'SO2',
          1: 'SaO2',
          2: 'SvO2',
          3: 'Not used',
          },
 },

########################################################################
# CO2

{'label': 'CO2 ET',
 'name': 'EtC02',
 'desc': 'Expiratory concentration',
 'key': 'co2:et',
 'unit': '%',
 'shift': 1/100,
 'subclass': 'basic',
 'transducer': '',
 'prefilter': '',
 'physical_min': 0,
 'physical_max': 100,
 },

{'label': 'CO2 FI',
 'name': 'FiC02',
 'desc': 'Inspiratory concentration',
 'key': 'co2:fi',
 'unit': '%',
 'shift': 1/100,
 'subclass': 'basic',
 'transducer': '',
 'prefilter': '',
 'physical_min': 0,
 'physical_max': 100,
 },

{'label': 'CO2 RR',
 'name': 'RR(CO2)',
 'desc': 'Respiration rate',
 'key': 'co2:rr',
 'unit': '1/min',
 'shift': 1,
 'subclass': 'basic',
 },

{'label': 'CO2 PAMB',
 'name': 'Pamb',
 'desc': 'Ambient pressure',
 'key': 'co2:amb_press',
 'unit': 'mmHg',
 'shift': 1/10,
 'subclass': 'basic',
 },

#----------------------------------------------------------------------
# Status

{'label': 'CO2: MOD',
 'desc': 'Measurement module existence',
 'key': 'co2:hdr:status:0',
 'subclass': 'basic',
 },

{'label': 'CO2: ACT',
 'desc': 'Measurement activity',
 'key': 'co2:hdr:status:1',
 'subclass': 'basic',
 },

{'label': 'CO2: AP',
 'desc': 'Apnea',
 'key': 'co2:hdr:status:2',
 'subclass': 'basic',
 },

{'label': 'CO2: CS',
 'desc': 'Calibrating sensor',
 'key': 'co2:hdr:status:3',
 'subclass': 'basic',
 },

{'label': 'CO2: ZS',
 'desc': 'Zeroing sensor',
 'key': 'co2:hdr:status:4',
 'subclass': 'basic',
 },

{'label': 'CO2: OC',
 'desc': 'Occlusion',
 'key': 'co2:hdr:status:5',
 'subclass': 'basic',
 },

{'label': 'CO2: ALK',
 'desc': 'Air leak',
 'key': 'co2:hdr:status:6',
 'subclass': 'basic',
 },

#----------------------------------------------------------------------
# Label

{'label': 'CO2 LBL',
 'desc': 'These bits indicate the respiration rate source',
 'key': 'co2:hdr:label:0-2',
 'subclass': 'basic',
 'dict': {0: 'Not selected',
          1: 'CO2',
          2: 'ECG, Impedance respiratory',
          },
 },


########################################################################
# O2

{'label': 'O2 ET',
 'name': 'FeO2',
 'desc': 'Expiratory concentration',
 'key': 'o2:et',
 'unit': '%',
 'shift': 1/100,
 'subclass': 'basic',
 },

{'label': 'O2 FI',
 'name': 'FiO2',
 'desc': 'Inspiratory concentration',
 'key': 'o2:fi',
 'unit': '%',
 'shift': 1/100,
 'subclass': 'basic',
 },

#----------------------------------------------------------------------
# Status

{'label': 'O2: MOD',
 'desc': 'Measurement module existence',
 'key': 'o2:hdr:status:0',
 'subclass': 'basic',
 },

{'label': 'O2: ACT',
 'desc': 'Measurement activity',
 'key': 'o2:hdr:status:1',
 'subclass': 'basic',
 },

{'label': 'CO2: CLBR',
 'desc': 'Caliabrating',
 'key': 'o2:hdr:status:2',
 'subclass': 'basic',
 },

{'label': 'CO2: MNS',
 'desc': 'Measurement off',
 'key': 'o2:hdr:status:3',
 'subclass': 'basic',
 },

#----------------------------------------------------------------------
# Label
# Not used


########################################################################
# N2O

{'label': 'N2O ET',
 'name': 'FeN2O',
 'desc': 'Expiratory concentration',
 'key': 'n2o:et',
 'unit': '%',
 'shift': 1/100,
 'subclass': 'basic',
 },

{'label': 'N2O FI',
 'name': 'FiN2O',
 'desc': 'Inspiratory concentration',
 'key': 'n2o:fi',
 'unit': '%',
 'shift': 1/100,
 'subclass': 'basic',
 },

#----------------------------------------------------------------------
# Status

{'label': 'N2O: MOD',
 'desc': 'Measurement module existence',
 'key': 'n2o:hdr:status:0',
 'subclass': 'basic',
 },

{'label': 'N2O: ACT',
 'desc': 'Measurement activity',
 'key': 'n2o:hdr:status:1',
 'subclass': 'basic',
 },

{'label': 'N2O: CLBR',
 'desc': 'Caliabrating',
 'key': 'n2o:hdr:status:2',
 'subclass': 'basic',
 },

{'label': 'N2O: MNS',
 'desc': 'Measurement off',
 'key': 'n2o:hdr:status:3',
 'subclass': 'basic',
 },


#----------------------------------------------------------------------
# Label
# Not used


########################################################################
# Anesthesia agents

{'label': 'AA ET',
 'name': 'FeAA',
 'desc': 'Anesthesia Agents ET',
 'key': 'aa:et',
 'unit': '%',
 'shift': 1/100,
 'subclass': 'basic',
 },

{'label': 'AA FI',
 'name': 'FiAA',
 'desc': 'Anesthesia Agent FI',
 'key': 'aa:fi',
 'unit': '%',
 'shift': 1/100,
 'subclass': 'basic',
 },

{'label': 'AA MAC-SUM',
 'name': 'MAC',
 'desc': 'Anesthesia Agents MAC SUM',
 'key': 'aa:mac_sum',
 'unit': '%',
 'shift': 1/100,
 'subclass': 'basic',
 },

#----------------------------------------------------------------------
# Status

{'label': 'AA: MOD',
 'desc': 'Measurement module existence',
 'key': 'aa:hdr:status:0',
 'subclass': 'basic',
 },

{'label': 'AA: ACT',
 'desc': 'Measurement activity',
 'key': 'aa:hdr:status:1',
 'subclass': 'basic',
 },

{'label': 'AA: CLBR',
 'desc': 'Caliabrating',
 'key': 'aa:hdr:status:2',
 'subclass': 'basic',
 },

{'label': 'AA: MNS',
 'desc': 'Measurement off',
 'key': 'aa:hdr:status:3',
 'subclass': 'basic',
 },

#----------------------------------------------------------------------
# Label

{'label': 'AA',
 'desc': 'Anesthesia Agent',
 'key': 'aa:hdr:label',
 'subclass': 'basic',
 'dict': {0: 'Unknow',
          1: 'None',
          2: 'HAL',
          3: 'ENF',
          4: 'ISO',
          5: 'DES',
          6: 'SEV'},
 },


########################################################################
# Flow & volume measurement

{'label': 'FLOW-VOL RR',
 'name': 'RR(Spir)',
 'desc': 'Respiration rate',
 'key': 'flow_vol:rr',
 'unit': '1/min',
 'shift': 1,
 'subclass': 'basic',
 },

{'label': 'FLOW-VOL PPEAK',
 'name': 'Ppeak',
 'desc': 'Peak pressure',
 'key': 'flow_vol:ppeak',
 'unit': 'cmH2O',
 'shift': 1/100,
 'subclass': 'basic',
 },

{'label': 'FLOW-VOL PEEP',
 'name': 'PEEP',
 'desc': 'Positive end exp. pressure',
 'key': 'flow_vol:peep',
 'unit': 'cmH2O',
 'shift': 1/100,
 'subclass': 'basic',
 },

{'label': 'FLOW-VOL PPLAT',
 'name': 'Pplat',
 'desc': 'Plateau pressure',
 'key': 'flow_vol:pplat',
 'unit': 'cmH2O',
 'shift': 1/100,
 'subclass': 'basic',
 },

{'label': 'FLOW-VOL TV-INSP',
 'name': 'TVinsp',
 'desc': 'Inspiratory tidal volume',
 'key': 'flow_vol:tv_insp',
 'unit': 'ml',
 'shift': 1/10,
 'subclass': 'basic',
 },

{'label': 'FLOW-VOL TV-EXP',
 'name': 'TVexp',
 'desc': 'Expiratory tidal volume',
 'key': 'flow_vol:tv_exp',
 'unit': 'ml',
 'shift': 1/10,
 'subclass': 'basic',
 },

{'label': 'FLOW-VOL COMP',
 'name': 'Compl',
 'desc': 'Compliance',
 'key': 'flow_vol:compliance',
 'unit': 'ml/cmH2O',
 'shift': 1/100,
 'subclass': 'basic',
 },

{'label': 'FLOW-VOL MV-EXP',
 'name': 'MVexp',
 'desc': 'Expiratory minute volume',
 'key': 'flow_vol:mv_exp',
 'unit': 'l/min',
 'shift': 1/100,
 'subclass': 'basic',
 },

#----------------------------------------------------------------------
# Status

{'label': 'FLOW-VOL: MOD',
 'desc': 'Measurement module existence',
 'key': 'flow_vol:hdr:status:0',
 'subclass': 'basic',
 },

{'label': 'FLOW-VOL: ACT',
 'desc': 'Measurement activity',
 'key': 'flow_vol:hdr:status:1',
 'subclass': 'basic',
 },

{'label': 'FLOW-VOL: DIS',
 'desc': 'Disconnection',
 'key': 'flow_vol:hdr:status:2',
 'subclass': 'basic',
 },

{'label': 'FLOW-VOL: CLBR',
 'desc': 'Calibrating',
 'key': 'flow_vol:hdr:status:3',
 'subclass': 'basic',
 },

{'label': 'FLOW-VOL: ZR',
 'desc': 'Zeroing',
 'key': 'flow_vol:hdr:status:4',
 'subclass': 'basic',
 },

{'label': 'FLOW-VOL: OBS',
 'desc': 'Obstruction',
 'key': 'flow_vol:hdr:status:5',
 'subclass': 'basic',
 },

{'label': 'FLOW-VOL: LK',
 'desc': 'Leak',
 'key': 'flow_vol:hdr:status:6',
 'subclass': 'basic',
 },

{'label': 'FLOW-VOL: MSR',
 'desc': 'Measurement off',
 'key': 'flow_vol:hdr:status:7',
 'subclass': 'basic',
 },

#----------------------------------------------------------------------
# Label
# Not used


########################################################################
# Cardiac output & wedge pressure

{'label': 'CO-WEDGE CO',
 'name': 'C.O.',
 'desc': 'Cardiac output',
 'key': 'co_wedge:co',
 'unit': 'ml/min',
 'shift': 1,
 'subclass': 'basic',
 },

{'label': 'CO-WEDGE TEMP',
 'name': 'Tblood',
 'desc': 'Blood temperature',
 'key': 'co_wedge:blood_temp',
 'unit': '\N{DEGREE SIGN}C',
 'shift': 1,
 'subclass': 'basic',
 },

{'label': 'CO-WEDGE REF',
 'name': 'RVEF',
 'desc': 'Right heart ejection fraction',
 'key': 'co_wedge:ref',
 'unit': '%',
 'shift': 1,
 'subclass': 'basic',
 },

{'label': 'CO-WEDGE PCWP',
 'name': 'PCWP',
 'desc': 'Wedge pressure',
 'key': 'co_wedge:pcwp',
 'unit': 'mmHg',
 'shift': 1/100,
 'subclass': 'basic',
 },

#----------------------------------------------------------------------
# Status

{'label': 'CO-WEDGE: MOD',
 'desc': 'Measurement module existence',
 'key': 'co_wedge:hdr:status:0',
 'subclass': 'basic',
 },

{'label': 'CO-WEDGE: ACT',
 'desc': 'Measurement activity',
 'key': 'co_wedge:hdr:status:1',
 'subclass': 'basic',
 },

#----------------------------------------------------------------------
# Label

{'label': 'CO-WEDGE CO-AGE',
 'desc': 'Age of CO reading is > 60 s',
 'key': 'co_wedge:hdr:label:0',
 'subclass': 'basic',
 },

{'label': 'CO-WEDGE PCWP-AGE',
 'desc': 'Age of PCWP reading is > 60 s',
 'key': 'co_wedge:hdr:label:1',
 'subclass': 'basic',
 },


########################################################################
# NMT

{'label': 'NMT T1',
 'name': 'T1%',
 'desc': 'Wedge pressure',
 'key': 'nmt:t1',
 'unit': '%',
 'shift': 1/10,
 'subclass': 'basic',
 },

{'label': 'NMT TRATIO',
 'name': 'TOF%',
 'desc': 't4/t1 in TOF mode, t2/t1 in DB mode',
 'key': 'nmt:tratio',
 'unit': '%',
 'shift': 1/10,
 'subclass': 'basic',
 },

{'label': 'NMT PTC-COUNT',
 'name': 'PTC',
 'desc': 'Post tetanic count, max. value 21. Has value 31 if count not\
 available',
 'key': 'nmt:ptc:0-4',
 'subclass': 'basic',
 },

{'label': 'NMT PTC-TOF-COUNT',
 'desc': 'TOF count in TOF mode',
 'key': 'nmt:ptc:5-8',
 'subclass': 'basic',
 },

{'label': 'NMT PTC-DB-COUNT',
 'desc': 'DB count in DB mode',
 'key': 'nmt:ptc:5-7',
 'subclass': 'basic',
 },

{'label': 'NMT PTC-ST-COUNT',
 'desc': 'ST count in ST mode',
 'key': 'nmt:ptc:5-6',
 'subclass': 'basic',
 },

{'label': 'NMT PTC-STIM',
 'desc': 'Stimulus current',
 'key': 'nmt:ptc:9-15',
 'unit': 'mA',
 'subclass': 'basic',
 },

#----------------------------------------------------------------------
# Status

{'label': 'NMT: MOD',
 'desc': 'Measurement module existence',
 'key': 'nmt:hdr:status:0',
 'subclass': 'basic',
 },

{'label': 'NMT: ACT',
 'desc': 'Measurement activity',
 'key': 'nmt:hdr:status:1',
 'subclass': 'basic',
 },

{'label': 'NMT STM',
 'desc': 'Stimulus mode',
 'key': 'nmt:hdr:status:2-3',
 'subclass': 'basic',
 'dict': {0: 'Train Of Four (TOF mode)',
          1: 'Double Burst (DB mode)',
          2: 'Single Twitch (ST mode)',
          3: 'Post-tetanic count',
          4: 'Tetanic',
          5: 'Regional block',
          },
 },

{'label': 'NMT TIME',
 'desc': 'Time',
 'key': 'nmt:hdr:label:4-5',
 'subclass': 'basic',
 'dict': {0: 'Not used',
          1: '100 us',
          2: '200 us',
          3: '300 us'
          },
 },

{'label': 'NMT: SUP',
 'desc': 'Supramax current found',
 'key': 'nmt:hdr:label:6',
 'subclass': 'basic',
 },

{'label': 'NMT: CLBR',
 'desc': 'Calibrated',
 'key': 'nmt:hdr:label:7',
 'subclass': 'basic',
 },

#----------------------------------------------------------------------
# Label
# Not used

########################################################################
# ECG extra

{'label': 'ECG-EXTRA: HR',
 'name': 'HR(ECG)',
 'desc': 'Heart rate as derived from the ecg signal',
 'key': 'ecg_extra:hr_ecg',
 'subclass': 'basic',
 },

{'label': 'ECG-EXTRA: HR-MAX',
 'name': 'HRmax',
 'desc': 'Maximum heart rate',
 'key': 'ecg_extra:hr_max',
 'subclass': 'basic',
 },

{'label': 'ECG-EXTRA: HR-MIN',
 'name': 'HRmin',
 'desc': 'Minimum heart rate',
 'key': 'ecg_extra:hr_min',
 'subclass': 'basic',
 },

#----------------------------------------------------------------------
# Status
#status from ECG (overwrite module status)

{'label': 'ECG-EXTRA: MOD',
 'desc': 'Measurement module existence',
 'key': 'ecg:hdr:status:0',
 'subclass': 'basic',
 },

{'label': 'ECG-EXTRA: ACT',
 'desc': 'Measurement activity',
 'key': 'ecg:hdr:status:1',
 'subclass': 'basic',
 },

#----------------------------------------------------------------------
# Label
# Not used

########################################################################
# SvO2

{'label': 'SvO2',
 'name': 'SvO2',
 'desc': 'SvO2',
 'key': 'svo2:svo2',
 'unit': '%',
 'shift': 1/100,
 'subclass': 'basic',
 },

#----------------------------------------------------------------------
# Status

{'label': 'SvO2: MOD',
 'desc': 'Measurement module existence',
 'key': 'svo2:hdr:status:0',
 'subclass': 'basic',
 },

{'label': 'SvO2: ACT',
 'desc': 'Measurement activity',
 'key': 'svo2:hdr:status:1',
 'subclass': 'basic',
 },

#----------------------------------------------------------------------
# Label
# Not used


########################################################################
# ECG-ARRH
# Arrhythmia analysis related data


{'label': 'ECG-ARRH HR',
 'name': 'HR(aECG)',
 'desc': 'Heart rate',
 'key': 'ecg_arrh:hr',
 'unit': '1/min',
 'shift': 1,
 'subclass': 'ext1',
 },

{'label': 'ECG-ARRH RR',
 'name': 'RRt(aECG)',
 'desc': 'The RR interval',
 'key': 'ecg_arrh:rr_time',
 'unit': '1/min',
 'shift': 1,
 'subclass': 'ext1',
 },

{'label': 'ECG-ARRH PVC',
 'name': 'PVC',
 'desc': 'Premature Ventricular Contractions',
 'key': 'ecg_arrh:pvc',
 'unit': '?',  #TODO: Set correct unit.
 'shift': 1,
 'subclass': 'ext1',
 },

# {'label': 'ECG-ARRH RESERVED',
 # 'desc': '',  #TODO: Set correct description.
 # 'key': 'ecg_arrh:arrh_reserved',
 # 'unit': '?',  #TODO: Set correct unit.
 # 'shift': 1,
 # },

#----------------------------------------------------------------------
# Status

{'label': 'ECG-ARRH: MOD',
 'desc': 'Measurement module existence',
 'key': 'ecg_arrh:hdr:status:0',
 'subclass': 'ext1',
 },

{'label': 'ECG-ARRH: ACT',
 'desc': 'Measurement activity',
 'key': 'ecg_arrh:hdr:status:1',
 'subclass': 'ext1',
 },

#----------------------------------------------------------------------
# Label


########################################################################
# ECG-12

{'label': 'ECG-12 STI',
 'name': 'ST(I)',
 'desc': 'St-level',
 'key': 'ecg_12:stI',
 'unit': 'mm',
 'shift': 1/100,
 'subclass': 'ext1',
 },

{'label': 'ECG-12 STII',
 'name': 'ST(II)',
 'desc': 'St-level',
 'key': 'ecg_12:stII',
 'unit': 'mm',
 'shift': 1/100,
 'subclass': 'ext1',
 },

{'label': 'ECG-12 STIII',
 'name': 'ST(III)',
 'desc': 'St-level',
 'key': 'ecg_12:stIII',
 'unit': 'mm',
 'shift': 1/100,
 'subclass': 'ext1',
 },

{'label': 'ECG-12 STAVL',
 'name': 'ST(AVL)',
 'desc': 'St-level',
 'key': 'ecg_12:stAVL',
 'unit': 'mm',
 'shift': 1/100,
 'subclass': 'ext1',
 },

{'label': 'ECG-12 STAVR',
 'name': 'ST(AVR)',
 'desc': 'St-level',
 'key': 'ecg_12:stAVR',
 'unit': 'mm',
 'shift': 1/100,
 'subclass': 'ext1',
 },

{'label': 'ECG-12 STAVF',
 'name': 'ST(AVF)',
 'desc': 'St-level',
 'key': 'ecg_12:stAVF',
 'unit': 'mm',
 'shift': 1/100,
 'subclass': 'ext1',
 },

{'label': 'ECG-12 STV1',
 'name': 'ST(V1)',
 'desc': 'St-level',
 'key': 'ecg_12:stV1',
 'unit': 'mm',
 'shift': 1/100,
 'subclass': 'ext1',
 },

{'label': 'ECG-12 STV2',
 'name': 'ST(V2)',
 'desc': 'St-level',
 'key': 'ecg_12:stV2',
 'unit': 'mm',
 'shift': 1/100,
 'subclass': 'ext1',
 },

{'label': 'ECG-12 STV3',
 'name': 'ST(V3)',
 'desc': 'St-level',
 'key': 'ecg_12:stV3',
 'unit': 'mm',
 'shift': 1/100,
 'subclass': 'ext1',
 },

{'label': 'ECG-12 STV4',
 'name': 'ST(V4)',
 'desc': 'St-level',
 'key': 'ecg_12:stV4',
 'unit': 'mm',
 'shift': 1/100,
 'subclass': 'ext1',
 },

{'label': 'ECG-12 STV5',
 'name': 'ST(V5)',
 'desc': 'St-level',
 'key': 'ecg_12:stV5',
 'unit': 'mm',
 'shift': 1/100,
 'subclass': 'ext1',
 },

{'label': 'ECG-12 STV6',
 'name': 'ST(V6)',
 'desc': 'St-level',
 'key': 'ecg_12:stV6',
 'unit': 'mm',
 'shift': 1/100,
 'subclass': 'ext1',
 },

#----------------------------------------------------------------------
# Status

{'label': 'ECG-12: MOD',
 'desc': 'Measurement module existence',
 'key': 'ecg_12:hdr:status:0',
 'subclass': 'ext1',
 },

{'label': 'ECG-12: ACT',
 'desc': 'Measurement activity',
 'key': 'ecg_12:hdr:status:1',
 'subclass': 'ext1',
 },

#----------------------------------------------------------------------
# Label

{'label': 'ECG-12 LEAD-CH1',
 'desc': 'Lead configuration for channel 1',
 'key': 'ecg_12:hdr:label:0-3',
 'subclass': 'ext1',
 'dict': {0: 'Not selected',
          1: 'ECG I',
          2: 'ECG II',
          3: 'ECG III',
          4: 'ECG AVR',
          5: 'ECG AVL',
          6: 'ECG AVF',
          7: 'ECG V',
          },
 },

{'label': 'ECG-12 LEAD-CH2',
 'desc': 'Lead configuration for channel 2',
 'key': 'ecg_12:hdr:label:4-7',
 'subclass': 'ext1',
 'dict': {0: 'Not selected',
          1: 'ECG I',
          2: 'ECG II',
          3: 'ECG III',
          4: 'ECG AVR',
          5: 'ECG AVL',
          6: 'ECG AVF',
          7: 'ECG V',
          },
 },

{'label': 'ECG-12 LEAD-CH3',
 'desc': 'Lead configuration for channel 3',
 'key': 'ecg_12:hdr:label:8-11',
 'subclass': 'ext1',
 'dict': {0: 'Not selected',
          1: 'ECG I',
          2: 'ECG II',
          3: 'ECG III',
          4: 'ECG AVR',
          5: 'ECG AVL',
          6: 'ECG AVF',
          7: 'ECG V',
          },
 },

########################################################################
# NMT2

{'label': 'NMT2 T1',
 'desc': 'T1 absolute value',
 'key': 'nmt2:nmt_t1',
 'subclass': 'ext2',
 },

{'label': 'NMT2 T2',
 'desc': 'T2 absolute value',
 'key': 'nmt2:nmt_t2',
 'subclass': 'ext2',
 },

{'label': 'NMT2 T3',
 'desc': 'T3 absolute value',
 'key': 'nmt2:nmt_t3',
 'subclass': 'ext2',
 },

{'label': 'NMT2 T4',
 'desc': 'T4 absolute value',
 'key': 'nmt2:nmt_t4',
 'subclass': 'ext2',
 },

#----------------------------------------------------------------------
# Status

{'label': 'NMT2: MOD',
 'desc': 'Measurement module existence',
 'key': 'nmt2:hdr:status:0',
 'subclass': 'ext2',
 },

{'label': 'NMT2: ACT',
 'desc': 'Measurement activity',
 'key': 'nmt2:hdr:status:1',
 'subclass': 'ext2',
 },

#----------------------------------------------------------------------
# Label
# Not used

########################################################################
# EEG

{'label': 'EEG FEMG',
 'name': 'FEMG',
 'desc': 'Frontal electro-myography',
 'key': 'eeg:femg',
 'unit': 'uv',
 'shift': 1/10,
 'subclass': 'ext2',
 },

{'label': 'EEG EEG1-AMPL',
 'name': 'Ampl1',
 'desc': 'RMS amplitude',
 'key': 'eeg:eeg1:ampl',
 'unit': 'uv',
 'shift': 1/10,
 'subclass': 'ext2',
 },

{'label': 'EEG EEG1-SFR',
 'name': 'SEF1',
 'desc': 'Spectral edge frequency',
 'key': 'eeg:eeg1:sef',
 'unit': 'Hz',
 'shift': 1/10,
 'subclass': 'ext2',
 },

{'label': 'EEG EEG1-MNF',
 'name': 'MF1',
 'desc': 'Median frequency',
 'key': 'eeg:eeg1:mf',
 'unit': 'Hz',
 'shift': 1/10,
 'subclass': 'ext2',
 },

{'label': 'EEG EEG1-DELTA',
 'name': 'Delta1',
 'desc': 'Relative power spectral content in delta band',
 'key': 'eeg:eeg1:delta_proc',
 'unit': '%',
 'shift': 1,
 'subclass': 'ext2',
 },

{'label': 'EEG EEG1-THETA',
 'name': 'Theta1',
 'desc': 'Relative power spectral content in theta band',
 'key': 'eeg:eeg1:theta_proc',
 'unit': '%',
 'shift': 1,
 'subclass': 'ext2',
 },

{'label': 'EEG EEG1-ALPHA',
 'name': 'Alpha1',
 'desc': 'Relative power spectral content in alpha band',
 'key': 'eeg:eeg1:alpha_proc',
 'unit': '%',
 'shift': 1,
 'subclass': 'ext2',
 },

{'label': 'EEG EEG1-BETA',
 'name': 'Beta1',
 'desc': 'Relative power spectral content in beta band',
 'key': 'eeg:eeg1:beta_proc',
 'unit': '%',
 'shift': 1,
 'subclass': 'ext2',
 },

{'label': 'EEG EEG1-BSR',
 'name': 'BSR1',
 'desc': 'Burst suppression ratio',
 'key': 'eeg:eeg1:bsr',
 'unit': '%',
 'shift': 1,
 'subclass': 'ext2',
 },

{'label': 'EEG EEG2-AMPL',
 'name': 'Ampl2',
 'desc': 'RMS amplitude',
 'key': 'eeg:eeg2:ampl',
 'unit': 'uv',
 'shift': 1/10,
 'subclass': 'ext2',
 },

{'label': 'EEG EEG2-SFR',
 'name': 'SEF2',
 'desc': 'Spectral edge frequency',
 'key': 'eeg:eeg2:sef',
 'unit': 'Hz',
 'shift': 1/10,
 'subclass': 'ext2',
 },

{'label': 'EEG EEG2-MF',
 'name': 'MF2',
 'desc': 'Median frequency',
 'key': 'eeg:eeg2:mf',
 'unit': 'Hz',
 'shift': 1/10,
 'subclass': 'ext2',
 },

{'label': 'EEG EEG2-DELTA',
 'name': 'Delta2',
 'desc': 'Relative power spectral content in delta band',
 'key': 'eeg:eeg2:delta_proc',
 'unit': '%',
 'shift': 1,
 'subclass': 'ext2',
 },

{'label': 'EEG EEG2-THETA',
 'name': 'Theta2',
 'desc': 'Relative power spectral content in theta band',
 'key': 'eeg:eeg2:theta_proc',
 'unit': '%',
 'shift': 1,
 'subclass': 'ext2',
 },

{'label': 'EEG EEG2-ALPHA',
 'name': 'Alpha2',
 'desc': 'Relative power spectral content in alpha band',
 'key': 'eeg:eeg2:alpha_proc',
 'unit': '%',
 'shift': 1,
 'subclass': 'ext2',
 },

{'label': 'EEG EEG2-BETA',
 'name': 'Beta2',
 'desc': 'Relative power spectral content in beta band',
 'key': 'eeg:eeg2:beta_proc',
 'unit': '%',
 'shift': 1,
 'subclass': 'ext2',
 },

{'label': 'EEG EEG2-BSR',
 'name': 'BSR2',
 'desc': 'Burst suppression ratio',
 'key': 'eeg:eeg2:bsr',
 'unit': '%',
 'shift': 1,
 'subclass': 'ext2',
 },

{'label': 'EEG EEG3-AMPL',
 'name': 'Ampl3',
 'desc': 'RMS amplitude',
 'key': 'eeg:eeg3:ampl',
 'unit': 'uv',
 'shift': 1/10,
 'subclass': 'ext2',
 },

{'label': 'EEG EEG3-SEF',
 'name': 'SEF3',
 'desc': 'Spectral edge frequency',
 'key': 'eeg:eeg3:sef',
 'unit': 'Hz',
 'shift': 1/10,
 'subclass': 'ext2',
 },

{'label': 'EEG EEG3-MF',
 'name': 'MF3',
 'desc': 'Median frequency',
 'key': 'eeg:eeg3:mf',
 'unit': 'Hz',
 'shift': 1/10,
 'subclass': 'ext2',
 },

{'label': 'EEG EEG3-DELTA',
 'name': 'Delta3',
 'desc': 'Relative power spectral content in delta band',
 'key': 'eeg:eeg3:delta_proc',
 'unit': '%',
 'shift': 1,
 'subclass': 'ext2',
 },

{'label': 'EEG EEG3-THETA',
 'name': 'Theta3',
 'desc': 'Relative power spectral content in theta band',
 'key': 'eeg:eeg3:theta_proc',
 'unit': '%',
 'shift': 1,
 'subclass': 'ext2',
 },

{'label': 'EEG EEG3-ALPHA',
 'name': 'Alpha3',
 'desc': 'Relative power spectral content in alpha band',
 'key': 'eeg:eeg3:alpha_proc',
 'unit': '%',
 'shift': 1,
 'subclass': 'ext2',
 },

{'label': 'EEG EEG3-BETA',
 'name': 'Beta3',
 'desc': 'Relative power spectral content in beta band',
 'key': 'eeg:eeg3:beta_proc',
 'unit': '%',
 'shift': 1,
 'subclass': 'ext2',
 },

{'label': 'EEG EEG3 BSR',
 'name': 'BSR3',
 'desc': 'Burst suppression ratio',
 'key': 'eeg:eeg3:bsr',
 'unit': '%',
 'shift': 1,
 'subclass': 'ext2',
 },

{'label': 'EEG EEG4-AMPL',
 'name': 'Ampl4',
 'desc': 'RMS amplitude',
 'key': 'eeg:eeg4:ampl',
 'unit': 'uv',
 'shift': 1/10,
 'subclass': 'ext2',
 },

{'label': 'EEG EEG4-SEF',
 'name': 'SEF4',
 'desc': 'Spectral edge frequency',
 'key': 'eeg:eeg4:sef',
 'unit': 'Hz',
 'shift': 1/10,
 'subclass': 'ext2',
 },

{'label': 'EEG EEG4-MF',
 'name': 'MF4',
 'desc': 'Median frequency',
 'key': 'eeg:eeg4:mf',
 'unit': 'Hz',
 'shift': 1/10,
 'subclass': 'ext2',
 },

{'label': 'EEG EEG4-DELTA',
 'name': 'Delta4',
 'desc': 'Relative power spectral content in delta band',
 'key': 'eeg:eeg4:delta_proc',
 'unit': '%',
 'shift': 1,
 'subclass': 'ext2',
 },

{'label': 'EEG EEG4-THETA',
 'name': 'Tetha4',
 'desc': 'Relative power spectral content in theta band',
 'key': 'eeg:eeg4:theta_proc',
 'unit': '%',
 'shift': 1,
 'subclass': 'ext2',
 },

{'label': 'EEG EEG4-ALPHA',
 'name': 'Alpha4',
 'desc': 'Relative power spectral content in alpha band',
 'key': 'eeg:eeg4:alpha_proc',
 'unit': '%',
 'shift': 1,
 'subclass': 'ext2',
 },

{'label': 'EEG EEG4-BETA',
 'name': 'Beta4',
 'desc': 'Relative power spectral content in beta band',
 'key': 'eeg:eeg4:beta_proc',
 'unit': '%',
 'shift': 1,
 'subclass': 'ext2',
 },

{'label': 'EEG EEG4-BSR',
 'name': 'BSR4',
 'desc': 'Burst suppression ratio',
 'key': 'eeg:eeg4:bsr',
 'unit': '%',
 'shift': 1,
 'subclass': 'ext2',
 },

#----------------------------------------------------------------------
# Status

{'label': 'EEG: MOD',
 'desc': 'Measurement module existence',
 'key': 'eeg:hdr:status:0',
 'subclass': 'ext2',
 },

{'label': 'EEG: ACT',
 'desc': 'Measurement activity',
 'key': 'eeg:hdr:status:1',
 'subclass': 'ext2',
 },

{'label': 'EEG: MSN',
 'desc': 'Measurement on',
 'key': 'eeg:hdr:status:2',
 'subclass': 'ext2',
 },

{'label': 'EEG: MONTAGE',
 'desc': 'Montage (in use: 0...7)',
 'key': 'eeg:hdr:status:3-6',
 'subclass': 'ext2',
 },

{'label': 'EEG: HEAD',
 'desc': 'Headbox off',
 'key': 'eeg:hdr:status:7',
 'subclass': 'ext2',
 },

{'label': 'EEG: SSEP',
 'desc': 'SSEP cable off',
 'key': 'eeg:hdr:status:8',
 'subclass': 'ext2',
 },

{'label': 'EEG: CH1-LEADS',
 'desc': 'Channel 1 leads off',
 'key': 'eeg:hdr:status:9',
 'subclass': 'ext2',
 },

{'label': 'EEG: CH2-LEADS',
 'desc': 'Channel 2 leads off',
 'key': 'eeg:hdr:status:10',
 'subclass': 'ext2',
 },

{'label': 'EEG: CH3-LEADS',
 'desc': 'Channel 3 leads off',
 'key': 'eeg:hdr:status:11',
 'subclass': 'ext2',
 },

{'label': 'EEG: CH4-LEADS',
 'desc': 'Channel 4 leads off',
 'key': 'eeg:hdr:status:12',
 'subclass': 'ext2',
 },

{'label': 'EEG: CH1-ARTF',
 'desc': 'Channel 1 artefact',
 'key': 'eeg:hdr:status:13',
 'subclass': 'ext2',
 },

{'label': 'EEG: CH2-ARTF',
 'desc': 'Channel 2 artefact',
 'key': 'eeg:hdr:status:14',
 'subclass': 'ext2',
 },

{'label': 'EEG: CH3-ARTF',
 'desc': 'Channel 3 artefact',
 'key': 'eeg:hdr:status:15',
 'subclass': 'ext2',
 },

{'label': 'EEG: CH4-ARTF',
 'desc': 'Channel 4 artefact',
 'key': 'eeg:hdr:status:16',
 'subclass': 'ext2',
 },

{'label': 'EEG: CH1-NS',
 'desc': 'Channel 1 noise',
 'key': 'eeg:hdr:status:17',
 'subclass': 'ext2',
 },

{'label': 'EEG: CH2-NS',
 'desc': 'Channel 2 noise',
 'key': 'eeg:hdr:status:18',
 'subclass': 'ext2',
 },

{'label': 'EEG: CH3-NS',
 'desc': 'Channel 3 noise',
 'key': 'eeg:hdr:status:19',
 'subclass': 'ext2',
 },

{'label': 'EEG: CH4-NS',
 'desc': 'Channel 4 noise',
 'key': 'eeg:hdr:status:20',
 'subclass': 'ext2',
 },

{'label': 'EEG: EP',
 'desc': 'EP selection',
 'key': 'eeg:hdr:status:21',
 'subclass': 'ext2',
 'dict': {0: 'AEP',
          1: 'SSEP',
          },
 },

{'label': 'EEG: MSN',
 'desc': 'Measurement type',
 'key': 'eeg:hdr:status:22',
 'subclass': 'ext2',
 'dict': {0: 'referential',
          1: 'bipolar',
          },
 },

#----------------------------------------------------------------------
# Label
# Not used



########################################################################
# EEG BIS

{'label': 'EEG-BIS',
 'name': 'BIS',
 'desc': '',  #TODO: Set correct description.
 'key': 'eeg_bis:bis',
 'unit': '?',  #TODO: Set correct unit.
 'shift': 1,
 'subclass': 'ext2',
 },

{'label': 'EEG-BIS SQI',
 'name': 'BisSQI',
 'desc': '',  #TODO: Set correct description.
 'key': 'eeg_bis:sqi_val',
 'unit': '?',  #TODO: Set correct unit.
 'shift': 1,
 'subclass': 'ext2',
 },

{'label': 'EEG-BIS EMG',
 'name': 'BisEMG',
 'desc': '',  #TODO: Set correct description.
 'key': 'eeg_bis:emg_val',
 'unit': '?',  #TODO: Set correct unit.
 'shift': 1,
 'subclass': 'ext2',
 },

{'label': 'EEG-BIS SR',
 'name': 'BisSR',
 'desc': '',  #TODO: Set correct description.
 'key': 'eeg_bis:sr_val',
 'unit': '?',  #TODO: Set correct unit.
 'shift': 1,
 'subclass': 'ext2',
 },

#----------------------------------------------------------------------
# Label

#----------------------------------------------------------------------
# Status

{'label': 'EEG-BIS: MOD',
 'desc': 'Measurement module existence',
 'key': 'eeg_bis:hdr:status:0',
 'subclass': 'ext2',
 },

{'label': 'EEG-BIS: ACT',
 'desc': 'Measurement activity',
 'key': 'eeg_bis:hdr:status:1',
 'subclass': 'ext2',
 },


########################################################################
# ENTROPY

{'label': 'ENTROPY SE',
 'name': 'SE',
 'desc': 'State entropy',
 'key': 'ent:eeg_ent',
 'unit': '%',
 'shift': 1,
 'subclass': 'ext2',
 'transducer': '',
 'prefilter': '',
 'physical_min': 0,
 'physical_max': 100,
 },

{'label': 'ENTROPY RE',
 'name': 'RE',
 'desc': 'Response entropy',
 'key': 'ent:emg_ent',
 'unit': '%',
 'shift': 1,
 'subclass': 'ext2',
 'transducer': '',
 'prefilter': '',
 'physical_min': 0,
 'physical_max': 100,
 },

{'label': 'ENTROPY BSR',
 'name': 'BSR',
 'desc': 'Burst suppression rate',
 'key': 'ent:bsr_ent',
 'unit': '%',
 'shift': 1,
 'subclass': 'ext2',
 'transducer': '',
 'prefilter': '',
 'physical_min': 0,
 'physical_max': 100,
 },

#----------------------------------------------------------------------
# Label

#----------------------------------------------------------------------
# Status

{'label': 'ENTROPY: MOD',
 'desc': 'Measurement module existence',
 'key': 'ent:hdr:status:0',
 'subclass': 'ext2',
 },

{'label': 'ENTROPY: ACT',
 'desc': 'Measurement activity',
 'key': 'ent:hdr:status:1',
 'subclass': 'ext2',
 },


########################################################################
# EEG2

{'label': 'EEG2 COMMON',
 'desc': '',  #TODO: Set correct description.
 'key': 'eeg2:common_reference',
 'unit': '?',  #TODO: Set correct unit.
 'shift': 1,
 'subclass': 'ext2',
 },

{'label': 'EEG2 CH1M',
 'desc': '',  #TODO: Set correct description.
 'key': 'eeg2:montage_label_ch_1_m',
 'unit': '?',  #TODO: Set correct unit.
 'shift': 1,
 'subclass': 'ext2',
 },

{'label': 'EEG2 CH1P',
 'desc': '',  #TODO: Set correct description.
 'key': 'eeg2:montage_label_ch_1_p',
 'unit': '?',  #TODO: Set correct unit.
 'shift': 1,
 'subclass': 'ext2',
 },

{'label': 'EEG2 CH2M',
 'desc': '',  #TODO: Set correct description.
 'key': 'eeg2:montage_label_ch_2_m',
 'unit': '?',  #TODO: Set correct unit.
 'shift': 1,
 'subclass': 'ext2',
 },

{'label': 'EEG2 CH2P',
 'desc': '',  #TODO: Set correct description.
 'key': 'eeg2:montage_label_ch_2_p',
 'unit': '?',  #TODO: Set correct unit.
 'shift': 1,
 'subclass': 'ext2',
 },

{'label': 'EEG2 CH3M',
 'desc': '',  #TODO: Set correct description.
 'key': 'eeg2:montage_label_ch_3_m',
 'unit': '?',  #TODO: Set correct unit.
 'shift': 1,
 'subclass': 'ext2',
 },

{'label': 'EEG2 CH3P',
 'desc': '',  #TODO: Set correct description.
 'key': 'eeg2:montage_label_ch_3_p',
 'unit': '?',  #TODO: Set correct unit.
 'shift': 1,
 'subclass': 'ext2',
 },

{'label': 'EEG2 CH4M',
 'desc': '',  #TODO: Set correct description.
 'key': 'eeg2:montage_label_ch_4_m',
 'unit': '?',  #TODO: Set correct unit.
 'shift': 1,
 'subclass': 'ext2',
 },

{'label': 'EEG2 CH4P',
 'desc': '',  #TODO: Set correct description.
 'key': 'eeg2:montage_label_ch_4_p',
 'unit': '?',  #TODO: Set correct unit.
 'shift': 1,
 'subclass': 'ext2',
 },

#----------------------------------------------------------------------
# Label

#----------------------------------------------------------------------
# Status

{'label': 'EEG2: MOD',
 'desc': 'Measurement module existence',
 'key': 'eeg2:hdr:status:0',
 'subclass': 'ext2',
 },

{'label': 'EEG2: ACT',
 'desc': 'Measurement activity',
 'key': 'eeg2:hdr:status:1',
 'subclass': 'ext2',
 },


########################################################################
# Gas exchange measurements

{'label': 'GASEX VO2',
 'name': 'VO2',
 'desc': 'Oxygen consumption',
 'key': 'gasex:vo2',
 'unit': 'ml/min',
 'shift': 1/10,
 'subclass': 'ext3',
 },

{'label': 'GASEX VCO2',
 'name': 'VCO2',
 'desc': 'Carbon dioxide consumption',
 'key': 'gasex:vco2',
 'unit': 'ml/min',
 'shift': 1/10,
 'subclass': 'ext3',
 },

{'label': 'GASEX EE',
 'name': 'EE',
 'desc': 'Energy expenditure',
 'key': 'gasex:ee',
 'unit': 'kcal/24h',
 'subclass': 'ext3',
 },

{'label': 'GASEX RQ',
 'name': 'RQ',
 'desc': 'Respiratory quotient',
 'key': 'gasex:rq',
 'subclass': 'ext3',
 },

#----------------------------------------------------------------------
# Status

{'label': 'GASEX: MOD',
 'desc': 'Measurement module existence',
 'key': 'gasex:hdr:status:0',
 'subclass': 'ext3',
 },

{'label': 'GASEX: ACT',
 'desc': 'Measurement activity',
 'key': 'gasex:hdr:status:1',
 'subclass': 'ext3',
 },

#----------------------------------------------------------------------
# Label
# Not used


########################################################################
# Flow & volume group 2

{'label': 'FLOW-VOL2 IPEEP',
 'name': 'PEEPi',
 'desc': 'Intrinsic PEEP',
 'key': 'flow_vol2:ipeep',
 'unit': 'cmH2O',
 'shift': 1/100,
 'subclass': 'ext3',
 },

{'label': 'FLOW-VOL2 Pmean',
 'name': 'Pmean',
 'desc': 'Mean pressure',
 'key': 'flow_vol2:pmean',
 'unit': 'cmH2O',
 'shift': 1/100,
 'subclass': 'ext3',
 },

{'label': 'FLOW-VOL2 RAW',
 'name': 'Raw',
 'desc': 'Airway resistance',
 'key': 'flow_vol2:raw',
 'unit': 'cmH2O',
 'shift': 1/100,
 'subclass': 'ext3',
 },

{'label': 'FLOW-VOL2 MVINSP',
 'name': 'MVinsp',
 'desc': 'Inspired minute volume',
 'key': 'flow_vol2:mv_insp',
 'unit': 'L/min',
 'shift': 1/100,
 'subclass': 'ext3',
 },

{'label': 'FLOW-VOL2 EPEEP',
 'name': 'PEEPe',
 'desc': 'Extrinsic PEEP',
 'key': 'flow_vol2:epeep',
 'unit': 'cmH2O',
 'shift': 1/100,
 'subclass': 'ext3',
 },

{'label': 'FLOW-VOL2 MVESEX',
 'name': 'MVspo',
 'desc': 'Spontaneous expired minute volume',
 'key': 'flow_vol2:mv_spont',
 'unit': 'L/min',
 'shift': 1/100,
 'subclass': 'ext3',
 },

{'label': 'FLOW-VOL2 IERATIO',
 'name': 'I:E',
 'desc': '',  #TODO: Set correct description.
 'key': 'flow_vol2:ie_ratio',
 'subclass': 'ext3',
 },

{'label': 'FLOW-VOL2 ISPTIME',
 'name': 'Tinsp',
 'desc': '',  #TODO: Set correct description.
 'key': 'flow_vol2:insp_time',
 'subclass': 'ext3',
 },

{'label': 'FLOW-VOL2 EXPTIME',
 'name': 'Texp',
 'desc': '',  #TODO: Set correct description.
 'key': 'flow_vol2:exp_time',
 'subclass': 'ext3',
 },

{'label': 'FLOW-VOL2 STCCOMP',
 'name': 'StCom',
 'desc': '',  #TODO: Set correct description.
 'key': 'flow_vol2:static_compliance',
 'subclass': 'ext3',
 },

{'label': 'FLOW-VOL2 STCPPLAT',
 'name': 'StPplat',
 'desc': '',  #TODO: Set correct description.
 'key': 'flow_vol2:static_pplat',
 'subclass': 'ext3',
 },

{'label': 'FLOW-VOL2 STCPEEPE',
 'name': 'StPEEP',
 'desc': '',  #TODO: Set correct description.
 'key': 'flow_vol2:static_peepe',
 'subclass': 'ext3',
 },

{'label': 'FLOW-VOL2 STCPEEPI',
 'name': 'StPEEPi',
 'desc': '',  #TODO: Set correct description.
 'key': 'flow_vol2:static_peepi',
 'subclass': 'ext3',
 },

#----------------------------------------------------------------------
# Status

{'label': 'FLOW-VOL2: MOD',
 'desc': 'Measurement module existence',
 'key': 'flow_vol2:hdr:status:0',
 'subclass': 'ext3',
 },

{'label': 'FLOW-VOL2: ACT',
 'desc': 'Measurement activity',
 'key': 'flow_vol2:hdr:status:1',
 'subclass': 'ext3',
 },

#----------------------------------------------------------------------
# Label
# Not used

########################################################################
# Balance gas

{'label': 'BAL-GAS ET',
 'name': 'FeBal',
 'desc': 'Expiratory concentration',
 'key': 'bal:et',
 'unit': '%',
 'shift': 1/100,
 'subclass': 'ext3',
 },

{'label': 'BAL-GAS FI',
 'name': 'FiBal',
 'desc': 'Inspiratory concentration',
 'key': 'bal:fi',
 'unit': '%',
 'shift': 1/100,
 'subclass': 'ext3',
 },

#----------------------------------------------------------------------
# Status

{'label': 'BAL-GAS: MOD',
 'desc': 'Measurement module existence',
 'key': 'bal:hdr:status:0',
 'subclass': 'ext3',
 },

{'label': 'BAL-GAS: ACT',
 'desc': 'Measurement activity',
 'key': 'bal:hdr:status:1',
 'subclass': 'ext3',
 },

#----------------------------------------------------------------------
# Label
# Not used


########################################################################
# Tonometry

{'label': 'TONO PrCO2',
 'name': 'PgCO2',
 'desc': 'PrCO2 concentration',
 'key': 'tono:prco2',
 'unit': 'kPa',
 'shift': 1/100,
 'subclass': 'ext3',
 },

{'label': 'TONO P(r-Et)CO2',
 'name': 'EtPgC',
 'desc': 'P(r-Et)CO2 gap',
 'key': 'tono:pr_et',
 'unit': 'kPa',
 'shift': 1/100,
 'subclass': 'ext3',
 },

{'label': 'TONO P(r-a)CO2',
 'name': 'PaCO2',
 'desc': 'P(r-a)CO2 gap',
 'key': 'tono:pr_pa',
 'unit': 'kPa',
 'shift': 1/100,
 'subclass': 'ext3',
 },

{'label': 'TONO PADELAY',
 'name': 'Delay',
 'desc': 'PaCO2 delay',
 'key': 'tono:pa_delay',
 'unit': 'min',
 'shift': 1,
 'subclass': 'ext3',
 },

{'label': 'TONO PHI',
 'name': 'pHi',
 'desc': 'pHi value',
 'key': 'tono:phi',
 'shift': 1/100,
 'subclass': 'ext3',
 },

{'label': 'TONO PHIDELAY',
 'name': 'pHiDel',
 'desc': 'pHi delay',
 'key': 'tono:phi_delay',
 'unit': 'min',
 'shift': 1,
 'subclass': 'ext3',
 },

{'label': 'TONO PAMB',
 'name': 'Pamb',
 'desc': 'Ambient pressure',
 'key': 'tono:amb_press',
 'unit': 'mmHg',
 'shift': 1/10,
 'subclass': 'ext3',
 },

{'label': 'TONO CMPA',
 'name': 'CMPA',
 'desc': 'Research data',
 'key': 'tono:cpma',
 'subclass': 'ext3',
 },

#----------------------------------------------------------------------
# Status

{'label': 'TONO: MOD',
 'desc': 'Measurement module existence',
 'key': 'tono:hdr:status:0',
 'subclass': 'ext3',
 },

{'label': 'TONO: ACT',
 'desc': 'Measurement activity',
 'key': 'tono:hdr:status:1',
 'subclass': 'ext3',
 },

{'label': 'TONO: LEAK',
 'desc': 'Leak',
 'key': 'tono:hdr:status:2',
 'subclass': 'ext3',
 },

{'label': 'TONO: VOLDR',
 'desc': 'volume dropped in catheter',
 'key': 'tono:hdr:status:3',
 'subclass': 'ext3',
 },

{'label': 'TONO: TECHFAIL',
 'desc': 'Technical failure',
 'key': 'tono:hdr:status:4',
 'subclass': 'ext3',
 },

{'label': 'TONO: UNFILL',
 'desc': 'Unable to fill catheter',
 'key': 'tono:hdr:status:5',
 'subclass': 'ext3',
 },

{'label': 'TONO: OVER',
 'desc': 'PrCO2 over limit',
 'key': 'tono:hdr:status:6',
 'subclass': 'ext3',
 },

#----------------------------------------------------------------------
# Label
# Not used


########################################################################
# AA2

{'label': 'AA2 MAC-AGE-SUM',
 'name': 'MACag',
 'desc': '',  #TODO: Set correct description.
 'key': 'aa2:mac_age_sum',
 'unit': '?',  #TODO: Set correct unit.
 'shift': 1,
 'subclass': 'ext3',
 },

#----------------------------------------------------------------------
# Status

{'label': 'AA2: MOD',
 'desc': 'Measurement module existence',
 'key': 'aa2:hdr:status:0',
 'subclass': 'ext3',
 },

{'label': 'AA2: ACT',
 'desc': 'Measurement activity',
 'key': 'aa2:hdr:status:1',
 'subclass': 'ext3',
 },

#----------------------------------------------------------------------
# Label


]


WAVEFORMS = [

{'label': 'ECG1',
 'desc': '',  #TODO: Set correct description.
 'unit': 'uV',
 #'unit': 'mV',
 'shift_': 1/1000,
 # 'shift': 1/1000000,
 'samps': 300,
 'transducer': '',
 'prefilter': '',
 'physical_min': -1000e-6,
 'physical_max': 1000e-6,
},

{'label': 'ECG2',
 'desc': '',  #TODO: Set correct description.
 'unit': 'uV',
 #'unit': 'mV',
 'shift_': 1/1000,
 # 'shift': 1/1000000,
 'shift': 1,
 'samps': 300,
 'transducer': '',
 'prefilter': '',
 'physical_min': -1000e-6,
 'physical_max': 1000e-6,
},

{'label': 'ECG3',
 'desc': '',  #TODO: Set correct description.
 'unit': 'uV',
 #'unit': 'mV',
 'shift_': 1/1000,
 # 'shift': 1/1000000,
 'shift': 1,
 'samps': 300,
 'transducer': '',
 'prefilter': '',
 'physical_min': -1000e-6,
 'physical_max': 1000e-6,
},

{'label': 'INVP1',
 'desc': 'Invasive blood pressure',
 'unit': 'mmHg',
 'shift': 1/100,
 'samps': 100,
 'transducer': '',
 'prefilter': '',
 'physical_min': None,
 'physical_max': None,
},

{'label': 'INVP2',
 'desc': 'Invasive blood pressure',
 'unit': 'mmHg',
 'shift': 1/100,
 'samps': 100,
 'transducer': '',
 'prefilter': '',
 'physical_min': None,
 'physical_max': None,
},

{'label': 'INVP3',
 'desc': 'Invasive blood pressure',
 'unit': 'mmHg',
 'shift': 1/100,
 'samps': 100,
 'transducer': '',
 'prefilter': '',
 'physical_min': None,
 'physical_max': None,
},

{'label': 'INVP4',
 'desc': 'Invasive blood pressure',
 'unit': 'mmHg',
 'shift': 1/100,
 'samps': 100,
 'transducer': '',
 'prefilter': '',
 'physical_min': None,
 'physical_max': None,
},

{'label': 'INVP5',
 'desc': 'Invasive blood pressure',
 'unit': 'mmHg',
 'shift': 1/100,
 'samps': 100,
 'transducer': '',
 'prefilter': '',
 'physical_min': None,
 'physical_max': None,
},

{'label': 'INVP6',
 'desc': 'Invasive blood pressure',
 'unit': 'mmHg',
 'shift': 1/100,
 'samps': 100,
 'transducer': '',
 'prefilter': '',
 'physical_min': None,
 'physical_max': None,
},

{'label': 'PLETH',
 'desc': 'Plethysmograph: modulation',
 'unit': '%',
 'shift': 1/100,
 'samps': 100,
 'transducer': '',
 'prefilter': '',
 'physical_min': -5,
 'physical_max': 10,
},

{'label': 'CO2',
 'desc': 'CO2 concentration',
 'unit': '%',
 'shift': 1/100,
 'samps': 25,
 'transducer': '',
 'prefilter': '',
 'physical_min': None,
 'physical_max': None,
},

{'label': 'N2O',
 'desc': 'N2O concentration',
 'unit': '%',
 'shift': 1/100,
 'samps': 25,
 'transducer': '',
 'prefilter': '',
 'physical_min': None,
 'physical_max': None,
},

{'label': 'AA_WAVE',
 'desc': 'Anaesthesia agent',
 'unit': '%',
 'shift': 1/100,
 'samps': 25,
 'transducer': '',
 'prefilter': '',
 'physical_min': None,
 'physical_max': None,
},

{'label': 'AWP',
 'desc': 'Airway pressure',
 'unit': 'cmH2O',
 'shift': 1/10,
 'samps': 25,
 'transducer': '',
 'prefilter': '',
 'physical_min': None,
 'physical_max': None,
},

{'label': 'FLOW',
 'desc': 'Airway flow',
 'unit': 'l/min',
 'shift': 1/10,
 'samps': 25,
 'transducer': '',
 'prefilter': '',
 'physical_min': None,
 'physical_max': None,
},

{'label': 'VOL',
 'desc': 'Airway volume',
 'unit': '?',  #TODO: Set correct unit.
 'shift': '?',  #TODO: Set correct shift.
 'samps': 25,
 'transducer': '',
 'prefilter': '',
 'physical_min': None,
 'physical_max': None,
},

{'label': 'RESP',
 'desc': 'ECG impedance',
 'unit': '\N{OHM SIGN}',
 'shift': 1/100,
 'samps': 25,
 'transducer': '',
 'prefilter': '',
 'physical_min': None,
 'physical_max': None,
},

{'label': 'EEG1',
 'desc': '',  #TODO: Set correct description.
 'unit': 'uV',
 'shift': 1/10,
 'samps': 100,
 'transducer': '',
 'prefilter': '',
 'physical_min': None,
 'physical_max': None,
},

{'label': 'EEG2',
 'desc': '',  #TODO: Set correct description.
 'unit': 'uV',
 'shift': 1/10,
 'samps': 100,
 'transducer': '',
 'prefilter': '',
 'physical_min': None,
 'physical_max': None,
},

{'label': 'EEG3',
 'desc': '',  #TODO: Set correct description.
 'unit': 'uV',
 'shift': 1/10,
 'samps': 100,
 'transducer': '',
 'prefilter': '',
 'physical_min': None,
 'physical_max': None,
},

{'label': 'EEG4',
 'desc': '',  #TODO: Set correct description.
 'unit': 'uV',
 'shift': 1/10,
 'samps': 100,
 'transducer': '',
 'prefilter': '',
 'physical_min': None,
 'physical_max': None,
},

{'label': 'TONO_PRESS',
 'desc': '',  #TODO: Set correct description.
 'unit': '?',  #TODO: Set correct unit.
 'shift': '?',  #TODO: Set correct shift.
 'samps': '?',  #TODO: Set correct samples.
 'transducer': '',
 'prefilter': '',
 'physical_min': None,
 'physical_max': None,
},

{'label': 'SPI_LOOP_STATUS',
 'desc': '',  #TODO: Set correct description.
 'unit': '?',  #TODO: Set correct unit.
 'shift': '?',  #TODO: Set correct shift.
 'samps': '?',  #TODO: Set correct samples.
 'transducer': '',
 'prefilter': '',
 'physical_min': None,
 'physical_max': None,
},

{'label': 'ENT_100',
 'desc': 'EEG channel from ENT100 module.',
 'unit': 'uV',
 'shift': 1/10,
 'samps': 100,
 'transducer': '',
 'prefilter': '',
 'physical_min': -250e-6,
 'physical_max': 250e-6,
},

{'label': 'EEG_BIS',
 'desc': '',  #TODO: Set correct description.
 'unit': '?',  #TODO: Set correct unit.
 'shift': '?',  #TODO: Set correct shift.
 'samps': '?',  #TODO: Set correct samples.
 'transducer': '',
 'prefilter': '',
 'physical_min': None,
 'physical_max': None,
},

]


GROUPS_DICT = {}
for k in GROUPS:
    key = k['label'].split()[0]
    key = key.replace(':', '')
    if key in GROUPS_DICT:
        GROUPS_DICT[key] = GROUPS_DICT[key] + [k]
    else:
        GROUPS_DICT[key] = [k]


LABEL_TO_DICT = {}
for k in GROUPS:
    LABEL_TO_DICT[k['label']] = k


WAVEFORMS_DICT = {}
for k in WAVEFORMS:
    WAVEFORMS_DICT[k['label']] = k


if __name__ == '__main__':

    try:
        rest = open('../docs/source/content/measures.rst', 'w')
    except:
        print("You should not be running this file.")
        import sys
        sys.exit()

    rest.write('Physiological measures\n')
    rest.write('======================\n\n')




    for list_ in GROUPS_DICT:


        rest.write('\n\n')
        rest.write('-'*len(list_)+'\n')
        rest.write(list_+'\n')
        rest.write('-'*len(list_)+'\n\n')


        C = [30, 75, 10, 10]
        fields = [d['label'] for d in GROUPS_DICT[list_]]
        rest.write('+'+('-'*C[0]+'+')+('-'*C[1]+'+')+('-'*C[2]+'+')+('-'*C[3]+'+')+'\n')
        row = ['**Label**', '**Description**', '**Unit**', '**Range**']
        i = 0
        for c in row:
            rest.write('|')
            rest.write(c.ljust(C[i], ' '))
            i += 1
        rest.write('|\n')
        rest.write('+'+('='*C[0]+'+')+('='*C[1]+'+')+('='*C[2]+'+')+('='*C[3]+'+')+'\n')
        for field in fields:

            # ref = ':ref:`{}`'.format(field)


            LABEL_TO_DICT[field].get('dict', None)

            unit = LABEL_TO_DICT[field].get('unit', None)
            # shift = str(LABEL_TO_DICT[field].get('shift', '1'))

            if unit is None:
                if LABEL_TO_DICT[field].get('dict', None):
                    unit = 'str'
                    # shift = ''
                if ':' in field:
                    unit = 'bool'
                    # shift = ''

            min_ = LABEL_TO_DICT[field].get('physical_min', None)
            max_ = LABEL_TO_DICT[field].get('physical_max', None)
            if min_ != None and max_ != None:
                range_ = '{} - {}'.format(min_, max_)
            else:
                range_ = ''



            row = ['``{}``'.format(field),
                   # '*{}*'.format(LABEL_TO_DICT[field]['desc']+str(LABEL_TO_DICT[field].get('dict', ''))),
                   '{}'.format(LABEL_TO_DICT[field]['desc']),
                   '{}'.format(unit),
                   '{}'.format(range_),
                   # shift,
                   # '``{}``'.format(LABEL_TO_DICT[field]['key']),
                   ]

            i = 0
            for c in row:
                rest.write('|')
                rest.write(c.ljust(C[i], ' '))
                i += 1
            rest.write('|\n')


            if LABEL_TO_DICT[field].get('dict', {}):
                # rest.write('\n')
                row = [''] * len(C)

                i = 0
                for c in row:
                    rest.write('|')
                    rest.write(c.ljust(C[i], ' '))
                    i += 1
                rest.write('|\n')

            for k in LABEL_TO_DICT[field].get('dict', {}):



                row = ['', '  * {}: {}'.format(k, LABEL_TO_DICT[field]['dict'][k]), '', '']



                i = 0
                for c in row:
                    rest.write('|')
                    rest.write(c.ljust(C[i], ' '))
                    i += 1
                rest.write('|\n')



            rest.write('+'+('-'*C[0]+'+')+('-'*C[1]+'+')+('-'*C[2]+'+')+('-'*C[3]+'+')+'\n')
        rest.write('\n')


    rest.write('\n\nWaveform measures\n')
    rest.write('=================\n\n\n')

    C = [30, 75, 10, 10]


    fields = [d['label'] for d in GROUPS_DICT[list_]]
    rest.write('+'+('-'*C[0]+'+')+('-'*C[1]+'+')+('-'*C[2]+'+')+('-'*C[3]+'+')+'\n')
    row = ['**Label**', '**Description**', '**Unit**', '**Samps**']
    i = 0
    for c in row:
        rest.write('|')
        rest.write(c.ljust(C[i], ' '))
        i += 1

    rest.write('|\n')
    rest.write('+'+('='*C[0]+'+')+('='*C[1]+'+')+('='*C[2]+'+')+('='*C[3]+'+')+'\n')

    for measure in WAVEFORMS_DICT:
        label = WAVEFORMS_DICT[measure]['label']
        desc = WAVEFORMS_DICT[measure]['desc']
        unit = WAVEFORMS_DICT[measure]['unit']
        # shift = WAVEFORMS_DICT[measure]['shift']
        samps = WAVEFORMS_DICT[measure]['samps']




        # ref = ':ref:`{}`'.format(field)
        row = ['``{}``'.format(label),
               '{}'.format(desc),
               '{}'.format(unit),
               # str(shift),
               '{}'.format(samps),
               # '``{}``'.format(LABEL_TO_DICT[field]['key']),

               ]
        i = 0
        for c in row:
            rest.write('|')
            rest.write(c.ljust(C[i], ' '))
            i += 1
        rest.write('|\n')
        rest.write('+'+('-'*C[0]+'+')+('-'*C[1]+'+')+('-'*C[2]+'+')+('-'*C[3]+'+')+'\n')
    rest.write('\n')



        # rest.write(measure+'\n')
        # rest.write('-'*len(measure)+'\n')
        # rest.write(desc+'\n\n')
        # rest.write(' * Unit: ``{}``\n'.format(unit))
        # rest.write(' * Shift: {}\n'.format(int(1/shift)))
        # rest.write(' * Samps/s: {}\n'.format(samps))
        # print('\n\n')

    rest.close()

