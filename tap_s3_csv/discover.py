import singer
from singer import metadata
from tap_s3_csv import s3

LOGGER = singer.get_logger()

def discover_streams(config):
    streams = []

    for table_spec in config['tables']:
        schema = discover_schema(config, table_spec)
        
        # exclude fields according to configuration
        fields_to_exclude = table_spec.get('exclude_properties', [])
        for field_name in fields_to_exclude:
            if field_name in schema['properties']:
                del schema['properties'][field_name]
            else:
                LOGGER.info('%s field not found in schema', field_name)
            
        streams.append({'stream': table_spec['table_name'], 'tap_stream_id': table_spec['table_name'], 'schema': schema, 'metadata': load_metadata(table_spec, schema)})
    return streams

def discover_schema(config, table_spec):
    sampled_schema = s3.get_sampled_schema_for_table(config, table_spec)

    # Raise an exception if schema cannot sampled. Empty schema will fail and target side anyways
    if not sampled_schema:
        raise ValueError("{} - {} file(s) has no data and cannot analyse the content to generate the required schema.".format(table_spec.get('search_prefix', ''), table_spec.get('search_pattern', '')))

    return sampled_schema

def load_metadata(table_spec, schema):
    mdata = metadata.new()

    mdata = metadata.write(mdata, (), 'table-key-properties', table_spec.get('key_properties', []))

    for field_name in schema.get('properties', {}).keys():
        if table_spec.get('key_properties', []) and field_name in table_spec.get('key_properties', []):
            mdata = metadata.write(mdata, ('properties', field_name), 'inclusion', 'automatic')
        else:
            mdata = metadata.write(mdata, ('properties', field_name), 'inclusion', 'available')

    return metadata.to_list(mdata)
