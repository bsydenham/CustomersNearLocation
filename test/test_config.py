import unittest
from unittest.mock import patch
import configparser
from customers_near_location import config

class TestConfig(unittest.TestCase):

    def test_config(self):
        with patch('configparser.ConfigParser') as configparser:
            config_dict = {
                    'import_filename': 'customers.txt',
                    'output_filename': 'output.txt',
                    'location_lat': '53.339428',
                    'location_lon': '-6.257664',
                    'distance_limit_km': '100',
            }
            
            configparser.items.return_value = config_dict
            result = config.get_config(configparser)

            configparser.read.assert_called_once_with('config.ini')
            self.assertEqual(result['import_filename'], 'customers.txt')
            self.assertEqual(result['output_filename'], 'output.txt')
            self.assertEqual(result['coordinates'], (float('53.339428'), float('-6.257664')))
            self.assertEqual(result['distance_limit_km'], int('100'))
            