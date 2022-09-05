import os
from setuptools import setup, find_packages

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name = 'pycollect',
    version = '1.0',
    packages = find_packages(),

    author = 'Yeison Cardona',
    author_email = 'yencardonaal@unal.edu.co',
    maintainer = 'Yeison Cardona',
    maintainer_email = 'yencardonaal@unal.edu.co',

    # url = '',
    download_url = 'https://bitbucket.org/gcpds/pycollect',

    install_requires = ['pyserial',
                        'pyedflib',
                        'pandas>=0.23.1',
                        ],

    include_package_data = True,
    license = 'BSD License',
    description = "PyCollect is a software package for collecting data from the GE patient monitors.",

    classifiers = [
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Medical Science Apps',
        'Topic :: Scientific/Engineering :: Visualization',

    ],

)
