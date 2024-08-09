2.1.2 (2024-08-09)
-------------------
**Changes**
  - Updating to a pypi version of singer-python (realit-singer-python)

2.1.1 (2024-07-23)
-------------------
**Changes**
  - Update pylint requirement from >=2.12,<3.1 to >=2.12,<3.3 #66

2.1.0 (2024-07-23)
-------------------
**Changes**
  - Patching boto3, voluptuous, messytables, pylint
  - Replace ujson with msgspec
  - Changing json serialisation with updated pipelinewise-singer-python (using msgspec)

2.0.13 (2023-10-07)
-------------------
**Changes**
  - Moving to local copy of messytables to resolve Python 3.10 issues
  - messytable https://github.com/okfn/messytables/pull/196

2.0.12 (2023-10-07)
-------------------
**Bumping Versions**
  - boto3==1.28.30
  - pytest>=7.1,<7.5
  - more_itertools>=8.12,<10.2
  - ujson==5.8.0
  - pytest-cov>=3.0,<4.2

2.0.11 (2023-05-23)
-------------------
**Changes**
  - Will output an empty file if there is just a header row and no records can be sampled.

2.0.10 (2023-05-23)
-------------------
**Bumping Versions**
  - boto3==1.26.138
  - ipdb==0.13.13
  - more_itertools>=8.12,<9.2
  - pylint>=2.12,<2.18
  - pytest-cov>=3.0,<4.1
  
2.0.9 (2023-05-23)
------------------
**Changes**
  - Using a List rather than a Set when obtaining a unique list of columns in the spreadsheet. This
  allows the column order to be retained as per the original csv file.

2.0.8 (2022-12-22)
------------------

**Changes**
  - Providing an optional set_empty_values_null setting. When set true will emit null (the JSON equivalent of None) instead of an empty string.

2.0.7 (2022-11-01)
------------------

**Changes**
  - Providing an optional s3_proxies dict config to set the use of a proxy server. Set to {} to avoid using a proxy server for s3 traffic.

2.0.6 (2022-10-05)
------------------

**Changes**
  - Bump boto3 from 1.23.10 to 1.24.26
  - Bump ujson from 5.2.0 to 5.4.0 because of vunerabilities

2.0.5 (2022-10-04)
------------------

The tap-s3-csv enhancements deal with scenarios where the csv files are not loading correctly due to various quality issues or assumption about the data being read e.g. data-types.

**Changes**
  - Allows strings to be overridden to have a string data-type regardless of what has been discovered
  - Supports the reading of UTF-8-BOM (Byte Order) - Microsoft saved csv files
  - Support a suffix being added to streams / tables to make them unique e.g. a date or provider_id
  - Provides option to warn rather error if a file isn't discovered for the search criteria
  - Support the ability to remove a character from the csv file being read e.g. strip out all double-quotes.

2.0.0 (2022-02-10)
------------------

**Changes**
  - Dropped support for python 3.6
  - Bump ujson from 4.3.0 to 5.1.0

1.2.3 (2022-01-14)
------------------
**Fix**
  - Set `time_extracted` when creating singer records.

**Changes**
  - Migrate CI to github actions
  - bump dependencies

1.2.2 (2021-07-19)
------------------
**Fix**
  - Make use of `start_date` when doing discovery
  - Discovery to run on more recent files to be able to detect new columns.

1.2.1 (2021-04-22)
------------------
- Bumping dependencies

1.2.0 (2020-08-04)
------------------
- Add `aws_profile` option to support Profile based authentication to S3
- Add option to authenticate to S3 using `AWS_PROFILE`, `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` and `AWS_SESSION_TOKEN` environment variables

1.1.0 (2020-02-20)
------------------
- Make logging configurable

1.0.7 (2020-01-07)
------------------
- Updated generated json schema to be more in sync with fast sync in PipelineWise

1.0.6 (2019-12-04)
------------------
- New data type guesser by `messytables`

1.0.5 (2019-09-10)
------------------
- Add `aws_endpoint_url` to support non-aws S3 account

1.0.4 (2019-08-16)
------------------
- License classifier and project description update

1.0.3 (2019-05-13)
------------------
- Raise exception when file(s) cannot sample

1.0.2 (2019-05-09)
------------------
- Better error messages when no files found

1.0.0 (2019-05-08)
------------------
- Initial release
