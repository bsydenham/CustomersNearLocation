import configparser

def get_config(config_parser: configparser.ConfigParser) -> dict:
    config_parser.read('config.ini')
    config_dict = dict(config_parser.items('DEFAULT'))
    config = {
        'import_filename': 'customers.txt',
        'output_filename': 'output.txt',
        'coordinates': (float(config_dict['location_lat']), float(config_dict['location_lon'])),
        'distance_limit_km': int(config_dict['distance_limit_km']),
    }

    return config
