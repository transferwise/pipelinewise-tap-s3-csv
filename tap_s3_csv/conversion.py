import csv
import io
import singer

from typing import Dict, List
from messytables import CSVTableSet, headers_guess, headers_processor, offset_processor, type_guess
from messytables.types import DateType, DecimalType, BoolType, IntegerType, DateUtilType

LOGGER = singer.get_logger()


def generate_schema(samples: List[Dict], table_spec: Dict) -> Dict:
    counts = {}

    table_set = CSVTableSet(_csv2bytesio(samples))

    row_set = table_set.tables[0]

    offset, headers = headers_guess(row_set.sample)
    row_set.register_processor(headers_processor(headers))
    row_set.register_processor(offset_processor(offset + 1))

    types = type_guess(row_set.sample, strict=True)

    for header, header_type in zip(headers, types):

        date_overrides = set(table_spec.get('date_overrides', []))

        if header in date_overrides:
            counts[header] = {
                'anyOf': [
                    {'type': ['null', 'string'], 'format': 'date-time'},
                    {'type': ['null', 'string']}
                ]
            }
        else:
            if isinstance(header_type, DateType) or isinstance(header_type, DateUtilType):
                counts[header] = {
                    'anyOf': [
                        {'type': ['null', 'string'], 'format': 'date'},
                        {'type': ['null', 'string']}
                    ]
                }
            else:
                counts[header] = {
                    'type': ['null', 'string']
                }

                if isinstance(header_type, IntegerType):
                    counts[header]['type'].append('integer')
                elif isinstance(header_type, DecimalType):
                    counts[header]['type'].append('number')
                elif isinstance(header_type, BoolType):
                    counts[header]['type'].append('boolean')

    return counts


def _csv2bytesio(data: List[Dict])-> io.BytesIO:
    """
    Converts a list of dictionaries to a csv BytesIO which is a csv file like object
    :param data: List of dictionaries
    :return:
    """
    sio = io.StringIO()

    header = set()

    for datum in data:
        header.update(list(datum.keys()))

    cw = csv.DictWriter(sio, fieldnames=header)

    cw.writeheader()
    cw.writerows(data)

    return io.BytesIO(sio.getvalue().strip('\r\n').encode('utf-8'))
