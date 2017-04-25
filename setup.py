#!/usr/bin/python3

""" setup.py for ran.

https://github.com/tlplu/ran
"""

import sys

from setuptools import setup

if sys.version_info < (3, 0):
    sys.exit('Ran requires python 3.')

setup(
    name='ran',

    version='0.1.0',

    description='Terminal based data logger for running workouts',
    long_description=open('README.rst').read(),

    url='https://github.com/tlplu/ran',

    author='tlplu',
    author_email='tlplu@protonmail.com',

    license='GPLv3',

    classifiers=[
        'Environment :: Console',
        'Operating System :: POSIX :: Linux',
        'Intended Audience :: End Users/Desktop',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ],

    keywords=['running', 'data', 'logger'],

    packages=['ran'],

    package_data={'': ['LICENSE', 'README.rst']},

    install_requires=[],

    entry_points={'console_scripts': ['ran = ran:main.main']},
)
