#!/usr/bin/env python3
'''
    This script will by run by PIP or the user when installing our package to the raspi.
    It should set up any dependencies, etc. and allows our package to A. be used as a Python library on the raspi, and B. be able to be run with python3 -m nemojag
'''

from setuptools import setup

setup(name='NemoJag',
      version='0.1',
      description='This software will be used to control the NemJag ROV.',
      author='Joseph R. Freeston, Torsten Diesel',
      url='https://www.github.com/thunderblood101/nemojag-2022',
      packages=['nemojag'],
      install_requires=[   # Any libraries we need go here;
          'Flask'          #     It will then install them automatically when this script is run! :)
      ]
     )