import codecs
import csv
from singer_encodings import compression
from singer_encodings.csv import SDC_EXTRA_COLUMN  # pylint:disable=no-name-in-module

def get_row_iterator(iterable, options=None):
    """Accepts an interable, options and returns a csv.DictReader object
    which can be used to yield CSV rows."""
    options = options or {}

    file_stream = codecs.iterdecode(iterable, encoding=options.get('encoding', 'utf-8'))

    # Replace any NULL bytes in the line given to the DictReader
    reader = csv.DictReader((line.replace('\0', '') for line in file_stream), fieldnames=None, restkey=SDC_EXTRA_COLUMN, delimiter=options.get('delimiter', ','))

    headers = set(reader.fieldnames)
    if options.get('key_properties'):
        key_properties = set(options['key_properties'])
        if not key_properties.issubset(headers):
            raise Exception('CSV file missing required headers: {}'
                            .format(key_properties - headers))

    if options.get('date_overrides'):
        date_overrides = set(options['date_overrides'])
        if not date_overrides.issubset(headers):
            raise Exception('CSV file missing date_overrides headers: {}'
                            .format(date_overrides - headers))
    return reader
