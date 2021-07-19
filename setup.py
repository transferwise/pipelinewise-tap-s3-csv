#!/usr/bin/env python

from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(name='pipelinewise-tap-s3-csv',
      version='1.2.2',
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
          'boto3==1.17.53',
          'singer-encodings==0.0.*',
          'pipelinewise-singer-python==1.*',
          'voluptuous==0.12.1',
          'ujson>=1.35,<4.1',
          'messytables==0.15.*',
          'more_itertools==8.8.*',
      ],
      extras_require={
          'dev': [
              'ipdb==0.13.7',
          ],
          'test': [
              'nose==1.3.*',
              'pylint>=2.4,<2.8',
          ]
      },
      entry_points='''
          [console_scripts]
          tap-s3-csv=tap_s3_csv:main
      ''',
      packages=['tap_s3_csv'])
