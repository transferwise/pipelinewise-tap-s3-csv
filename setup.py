#!/usr/bin/env python

from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(name='pipelinewise-tap-s3-csv',
      version='2.0.0',
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
          'boto3==1.23.10',
          'pipelinewise-singer-python==2.0.*',
          'singer-encodings==0.1.*',
          # Public repository
          'singer-encodings @ git+https://github.com/s7clarke10/singer-encodings@feature/remove_singer_dependency',
          'voluptuous==0.13.1',
          'ujson==5.2.0',
          'messytables==0.15.*',
          'more_itertools==8.12.*',
      ],
      extras_require={
          'dev': [
              'ipdb==0.13.9',
          ],
          'test': [
              'pytest==7.1.*',
              'pylint==2.12.*',
              'pytest-cov==3.0.*'
          ],
          'postinstall': [
              'singer-encodings==0.1.*',
          ],
      },
      entry_points='''
          [console_scripts]
          tap-s3-csv=tap_s3_csv:main
      ''',
      packages=['tap_s3_csv'])