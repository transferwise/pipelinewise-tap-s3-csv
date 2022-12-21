"""
Tap configuration related stuff
"""
from voluptuous import Schema, Required, Optional

CONFIG_CONTRACT = Schema([{
    Required('table_name'): str,
    Required('search_pattern'): str,
    Optional('key_properties'): [str],
    Optional('search_prefix'): str,
    Optional('date_overrides'): [str],
    Optional('string_overrides'): [str],
    Optional('guess_types'): bool,
    Optional('delimiter'): str,
    Optional('table_suffix'): str,
    Optional('remove_character'): str,
    Optional('s3_proxies'): object,
    Optional('encoding'): str,
    Optional('set_empty_values_null'): bool,
}])
