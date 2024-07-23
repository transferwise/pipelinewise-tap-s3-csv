#!/usr/bin/env python

from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(name='pipelinewise-tap-s3-csv',
      version='2.1.1',
      description='Singer.io tap for extracting CSV files from S3 - PipelineWise compatible',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='TransferWise',
      url='https://github.com/transferwise/pipelinewise-tap-s3-csv',
      classifiers=[
          'License :: OSI Approved :: GNU Affero General Public License v3',
          'Programming Language :: Python :: 3 :: Only'
      ],
      py_modules=['tap_s3_csv'],
      install_requires=[
          'boto3==1.34.146',
          'pipelinewise-singer-python @ git+https://github.com/s7clarke10/pipelinewise-singer-python@4.0.0',
          # Public repository
          'singer-encodings @ git+https://github.com/s7clarke10/singer-encodings.git@v0.1.3',
          'voluptuous==0.14.2',
          'msgspec==0.18.0',
          'messytables @ git+https://github.com/s7clarke10/messytables@0.15.4',
          'more_itertools>=8.12,<10.2',
      ],
      extras_require={
          'dev': [
              'ipdb==0.13.13',
          ],
          'test': [
              'pytest>=7.1,<7.5',
              'pylint>=2.12,<3.3',
              'pytest-cov>=3.0,<4.2'
          ]
      },
      entry_points='''
          [console_scripts]
          tap-s3-csv=tap_s3_csv:main
      ''',
      packages=['tap_s3_csv'])
