import unittest
from unittest.mock import patch
from customers_near_location import customers_near_location

class TestCustomersNearLocation(unittest.TestCase):
    @patch('customers_near_location.config.get_config')
    @patch('customers_near_location.customer_importer.import_customers')
    @patch('customers_near_location.customers_within_distance.get_customers_within_distance')
    @patch('customers_near_location.customer_output.output_customers')
    def test_get_customers_near_location(self, mock_output, mock_get_customers_within_distance, mock_import_customers, mock_get_config):
        mock_config = {
            'import_filename': 'filename',
            'output_filename': 'filename2',
            'coordinates': (0, 1),
            'distance_limit_km': 1,
        }
        mock_customers = []
        mock_filtered_customers = []

        mock_get_config.return_value = mock_config
        mock_import_customers.return_value = mock_customers
        mock_get_customers_within_distance.return_value = mock_filtered_customers

        customers_near_location.get_customers_near_location()

        mock_get_config.assert_called_once
        mock_import_customers.assert_called_once_with(mock_config['import_filename'])
        mock_get_customers_within_distance.assert_called_once_with(mock_customers, mock_config['coordinates'], mock_config['distance_limit_km'])
        mock_output.assert_called_once_with(mock_config['output_filename'], mock_filtered_customers)