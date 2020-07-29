import os


def get_config():
    config = {}

    # --------------------------------------------------------------------------
    # Default configuration settings for integration tests.
    # --------------------------------------------------------------------------
    # The following values needs to be defined in environment variables with
    # valid details to an S3 bucket
    # --------------------------------------------------------------------------
    # S3 bucket
    config['aws_access_key_id'] = os.environ.get('TAP_S3_CSV_ACCESS_KEY_ID')
    config['aws_secret_access_key'] = os.environ.get('TAP_S3_CSV_SECRET_ACCESS_KEY')
    config['bucket'] = os.environ.get('TAP_S3_CSV_BUCKET')

    # --------------------------------------------------------------------------
    # The tests cases will change these values automatically whenever it's needed
    # --------------------------------------------------------------------------
    config['start_date'] = '2000-01-01'
    config['tables'] = None

    return config


def get_test_config():
    return get_config()