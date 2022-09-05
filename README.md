
# PyCollect #
**PyCollect** is a software package for collecting data from the GE patient monitors,
for the purpose of conducting research and preparing training materials.


```python
%pylab inline
```

    Populating the interactive namespace from numpy and matplotlib


## Install ##


### From source ##
```bash
git clone git clone git@bitbucket.org:gcpds/pycollect.git
cd pycollect
python setup.py install
```

### From PyPi (not available yet) ##
```bash
pip install pycollect
```

## Usage ##
There are two main modules, `GEDevice` that handle the connection and data recollecting, and `GEDecode` that parse and sort the received data strings.


```python
from pycollect import GEDevice, GEDecode
```

### Collect data ##

#### Connection ###


```python
device = GEDevice()
device.connect('/dev/ttyUSB0')
```




    True




```python
device.stop()
```

#### Send request ####

##### Subrecords #####

There are three subrecord types for the actual measurement data:

 * `device.DISPL` for the displayed values.
 * `device.TREND_10S` for the 10 s trended values.
 * `device.TREND_60S` for the 60 s trended values.


```python
import time
# device.request(subtype=device.DISPL) 
# time.sleep(1)
device.request(subtype=device.TREND_10S)
# time.sleep(1)
# device.request(subtype=device.TREND_60S) 
```

##### Waveforms #####
Depending on the total number of samples per second the monitor sends a waveform packet every 1000 ms, 500 ms or 250 ms.  
Request up to 8 waveforms but total sample rate should be less than 600 samples/sec, sample rate for **ECG** is 300, **INVP** 100, **EEG** 100, **PLETH** 100, respiratory (**CO2**, **O2**, **NO2**...) 25 each.


```python
device.request(interval=1, waveform_set=['PLETH', 'ECG1'])
```


```python
#request more that 600 samples/sec generate an exception
try:
    device.request(waveform_set=['ECG1', 'ECG2', 'ECG3'])
except Exception as error:
    print(error)
```

    Sample rate must be less than 600



```python
from pycollect.modules import WAVEFORMS_DICT

for wave in WAVEFORMS_DICT:
    print("{label}: {samps}".format(**WAVEFORMS_DICT[wave]))
```

    ECG1: 300
    ECG2: 300
    ECG3: 300
    INVP1: 100
    INVP2: 100
    INVP3: 100
    INVP4: 1
    INVP5: 100
    INVP6: 100
    PLETH: 100
    CO2: 25
    NO2: 25
    AA: 25
    AWP: 25
    FLOW: 1
    VOL: 25
    RESP: 25
    EEG1: 100
    EEG2: 100
    EEG3: 1
    EEG4: 100
    TONO_PRESS: 1
    SPI_LOOP_STATUS: 1
    ENT_100: 1
    EEG_BIS: 1


### Read data ###
The transmitted data is recollected asynchronously with a background thread and appended to the `BUFFER` list.


```python
device.collect(True)
```

Is possible to check the status of `BUFFER` with:


```python
print('Length: {} bytes'.format(len(device.BUFFER)))
print(device.BUFFER[:43])
# print(bytes(device.BUFFER))
# (device.READING)
import struct

# struct.unpack('>h', bytes([14, 10]))
[int(_) for _ in struct.pack('>h', 3660)]
```

    Length: 3356 bytes
    [126, 40, 0, 164, 10, 0, 0, 95, 178, 51, 91, 0, 0, 0, 0, 0, 0, 0, 0, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 116, 126]





    [14, 76]



    Exception in thread Thread-9:
    Traceback (most recent call last):
      File "/usr/lib/python3.6/site-packages/serial/serialposix.py", line 501, in read
        'device reports readiness to read but returned no data '
    serial.serialutil.SerialException: device reports readiness to read but returned no data (device disconnected or multiple access on port?)
    
    During handling of the above exception, another exception occurred:
    
    Traceback (most recent call last):
      File "/usr/lib/python3.6/threading.py", line 916, in _bootstrap_inner
        self.run()
      File "/usr/lib/python3.6/threading.py", line 864, in run
        self._target(*self._args, **self._kwargs)
      File "/home/yeison/Development/gcpds/pycollect/pycollect/device.py", line 258, in read
        data = self.device.read(size)
      File "/usr/lib/python3.6/site-packages/serial/serialposix.py", line 509, in read
        raise SerialException('read failed: {}'.format(e))
    serial.serialutil.SerialException: read failed: device reports readiness to read but returned no data (device disconnected or multiple access on port?)
    



```python
from datetime import datetime
file = open('{}.raw'.format(datetime.now()), 'wb')
file.write(bytes(device.BUFFER))
file.close()
```

for clear the buffer just:


```python
device.clear_buffer()
```

for stop the reading:


```python
device.collect(False)
```

### Decode data ##


```python
decoder = GEDecode()
decoder.process(device.BUFFER)
```


```python
print("Modules: ", decoder.MODULES)
print("Active modules: ", decoder.MODULES_ACTIVE)
```

    Modules:  ['INV-BP:p1', 'INV-BP:p2', 'TEMP:t1', 'ECG', 'NINV-BP', 'SpO2', 'NMT', 'ECG-EXTRA', 'ECG-ARRH', 'ECG-12', 'NMT2', 'ENTROPY']
    Active modules:  ['TEMP', 'ECG', 'NINV-BP', 'SpO2', 'NMT', 'ECG-EXTRA', 'ECG-ARRH', 'ECG-12', 'NMT2', 'ENTROPY']


The `DATA_SUBRECORD` will contain the displayed values


```python
decoder.DATA_SUBRECORD
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>TEMP</th>
      <th>TEMP LBL</th>
      <th>ECG HR</th>
      <th>ECG ST1</th>
      <th>ECG ST2</th>
      <th>ECG ST3</th>
      <th>ECG IMP-RR</th>
      <th>ECG: ASY</th>
      <th>ECG HR SRC</th>
      <th>...</th>
      <th>ECG-12 LEAD CH1</th>
      <th>ECG-12 LEAD CH2</th>
      <th>ECG-12 LEAD CH3</th>
      <th>NMT2 T1</th>
      <th>NMT2 T2</th>
      <th>NMT2 T3</th>
      <th>NMT2 T4</th>
      <th>ENTROPY EEG</th>
      <th>ENTROPY EMG</th>
      <th>ENTROPY BSR</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2018-06-27 15:43:00</td>
      <td>None</td>
      <td>T4</td>
      <td>71</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>False</td>
      <td>Not selected</td>
      <td>...</td>
      <td>ECG I</td>
      <td>ECG II</td>
      <td>Not selected</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2018-06-27 15:44:00</td>
      <td>None</td>
      <td>T4</td>
      <td>74</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>False</td>
      <td>Not selected</td>
      <td>...</td>
      <td>ECG I</td>
      <td>ECG II</td>
      <td>Not selected</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2018-06-27 15:45:00</td>
      <td>None</td>
      <td>T4</td>
      <td>69</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>False</td>
      <td>Not selected</td>
      <td>...</td>
      <td>ECG I</td>
      <td>ECG II</td>
      <td>Not selected</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 75 columns</p>
</div>




```python
decoder.DATA_SUBRECORD.columns;
```


```python
decoder.DATA_SUBRECORD[['date', 'ECG HR', 'SpO2', 'TEMP', 'TEMP LBL']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>ECG HR</th>
      <th>SpO2</th>
      <th>TEMP</th>
      <th>TEMP LBL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2018-06-27 15:43:00</td>
      <td>71</td>
      <td>94.54</td>
      <td>None</td>
      <td>T4</td>
    </tr>
  </tbody>
</table>
</div>



`DATA_WAVE_SUBRECORD` will contain the waveforms requested


```python
decoder.DATA_WAVE_SUBRECORD.keys()
```




    dict_keys([])




```python
data = decoder.DATA_WAVE_SUBRECORD['PLETH']

pyplot.figure(None, figsize=(20, 7), dpi=100)
pyplot.plot(data)
pyplot.show()
```


![png](../../README_files/../../README_34_0.png)


    Exception in thread Thread-23:
    Traceback (most recent call last):
      File "/usr/lib/python3.6/site-packages/serial/serialposix.py", line 501, in read
        'device reports readiness to read but returned no data '
    serial.serialutil.SerialException: device reports readiness to read but returned no data (device disconnected or multiple access on port?)
    
    During handling of the above exception, another exception occurred:
    
    Traceback (most recent call last):
      File "/usr/lib/python3.6/threading.py", line 916, in _bootstrap_inner
        self.run()
      File "/usr/lib/python3.6/threading.py", line 864, in run
        self._target(*self._args, **self._kwargs)
      File "/home/yeison/Development/gcpds/pycollect/pycollect/device.py", line 258, in read
        data = self.device.read(size)
      File "/usr/lib/python3.6/site-packages/serial/serialposix.py", line 509, in read
        raise SerialException('read failed: {}'.format(e))
    serial.serialutil.SerialException: read failed: device reports readiness to read but returned no data (device disconnected or multiple access on port?)
    


### Save data ##
The data can be saved in two differents formats _csv_ and _edf_, each type of data will be saved with their own sufix: **.wave** for waveforms, **.trend10s** and **.trend60s** for trends.

#### Save data as CSV ###


```python
decoder.save_as_csv('data_out')
```

#### Save data as EDF+ ###
The _edf_ format need extra patient information.


```python
decoder.set_edf_header(
    admincode = '',
    birthdate = date(1900, 1, 1), #datetime object
    equipment = '',
    gender = 0, #0 for male, 1 for female
    patientcode = '',
    patientname = '',
    patient_additional = '',
    recording_additional = '',
    technician = '',
)

decoder.save_as_edf('data_out')
```

## Output ##

## References ##

  * [AS/3, CS/3 Monitoring System Main Software S/5 Monitor System Main Software Computer Interface](https://bitbucket.org/gcpds/docs/raw/887831aef98e473e4cc214b0ad809d39347444f2/AS3-S5%20Comm%20Protocol%20Computer%20Interface.pdf)
  * [Data acquisition from S/5 GE Datex anesthesia monitor using VSCapture: An open source.NET/Mono tool](https://bitbucket.org/gcpds/docs/raw/887831aef98e473e4cc214b0ad809d39347444f2/JAnaesthClinPharmacol293423-4307986_115759.pdf)
  * [An Open-Source Anaesthesia Workstation (Linux)](https://bitbucket.org/gcpds/docs/raw/887831aef98e473e4cc214b0ad809d39347444f2/xenon2014b.pdf)

