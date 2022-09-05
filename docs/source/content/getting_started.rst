===============
Getting started
===============

Install
=======

From source
-----------

.. code:: bash

   git clone git clone git@bitbucket.org:gcpds/pycollect.git
   cd pycollect
   python setup.py install


From PyPi (not available yet)
-----------------------------

.. code:: bash

   pip install pycollect


Collect data
============

There are two main modules, ``GEDevice`` that handle the connection and
data recollecting, and ``GEDecode`` that parse and sort the received
data strings.

.. code:: ipython3

    from pycollect import GEDevice


Connection
----------

.. code:: ipython3

    device = GEDevice()
    device.connect('/dev/ttyUSB0')



Send request
------------

A request is an instruction that enable the data transmission from monitor.


Subrecords
~~~~~~~~~~

There are three subrecord types for the actual measurement data:

-  ``device.DISPL`` for the displayed values.
-  ``device.TREND_10S`` for the 10 s trended values.
-  ``device.TREND_60S`` for the 60 s trended values.

When ``device.DISPL`` is used, there is an extra argument, ``interval``, that
indicate the transmission interval in seconds, this must be possitive and
greater or equal to 5.

.. code:: ipython3

    device.request(subtype=device.DISPL)

``device.TREND_10S`` and ``device.TREND_60S`` are used for request trends.

.. code:: ipython3

    device.request(subtype=device.TREND_10S)

.. code:: ipython3

    device.request(subtype=device.TREND_60S)

*No further transmission requests are needed after this.*


Waveforms
~~~~~~~~~

Depending on the total number of samples per second the monitor sends a waveform
packet every *1000 ms*, *500 ms* or *250 ms*.
Request up to 8 waveforms but total sample rate should be less than
600 samples/sec, sample rate for **ECG** is 300, **INVP** 100, **EEG** 100,
**PLETH** 100, respiratory (**CO2**, **O2**, **NO2** ...) 25 each.


The waveform options can be consulted with:

.. code:: ipython3

    from pycollect.modules import WAVEFORMS_DICT

    for wave in WAVEFORMS_DICT:
        print("{label}: {samps}".format(**WAVEFORMS_DICT[wave]))

.. parsed-literal::

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


.. code:: ipython3

    device.request(waveform_set=['PLETH', 'ECG1'])  #400 samp/s

The limit of sample rate can not be exceeded:


.. code:: ipython3

    try:
        device.request(waveform_set=['ECG1', 'ECG2', 'ECG3'])  #900 samp/s
    except Exception as error:
        print(error)

.. parsed-literal::

    Sample rate must be less or equal to 600.


*No further transmission requests are needed after this.*


Mixings
~~~~~~~
A combination of **Waveforms** and **Subrecords** can be requested at the same
time.

.. code:: ipython3

    device.request(subtype=device.DISPL, waveform_set=['PLETH', 'ECG1'])

Or in a sequence of requests.

.. code:: ipython3

    device.request(subtype=device.DISPL, interval=10)
    device.request(waveform_set=['PLETH', 'ECG1'])


.. code:: ipython3

    device.request(subtype=device.DISPL, interval=10)
    device.request(subtype=device.TREND_60S)
    device.request(waveform_set=['PLETH', 'ECG1'])


Read data
---------

The transmitted data is recollected asynchronously with a background thread and
appended to a ``BUFFER`` list.

To activate the data collecting.

.. code:: ipython3

    device.collect(True)


To clear the buffer input:

.. code:: ipython3

    device.clear_buffer()


To stop the data collecting:

.. code:: ipython3

    device.collect(False)



Decode data
===========

The ``GEDecode`` module is used for parse and sort the received data strings.

.. code:: ipython3

    from pycollect import GEDecode


.. code:: ipython3

    decoder = GEDecode(device.BUFFER)
    decoder.process(True)



Clear buffers
=============

There are a set of methods for clear correctly the stored buffer and recollected data.

.. code:: ipython3

    device.clear_buffer()  # clear input buffer.
    decoder.clear_buffer()  # clear decoded data, breaks the synchrony.
    decoder.clear_data()  # clear recollected data.

The above instructions breaks the synchrony between the collector and decoder,
in order to decode input data again ``GEDecode`` must be reinstantiated:

.. code:: ipython3

    decoder = GEDecode(device.BUFFER)
    decoder.process(True)


Save data
=========

The data can be saved in two differents formats *csv* and *edf*, each type of
data will be saved with their own sufix: **.wave** for waveforms, **.trend10s**
and **.trend60s** for trends.

Save data as CSV
----------------

.. code:: ipython3

    decoder.save_as_csv('data_out')


Save data as EDF+
-----------------

The *edf* format need extra patient information.

.. code:: ipython3

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
