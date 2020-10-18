import unittest
from unittest.mock import patch
from unittest.mock import mock_open
import json
from customers_near_location import customer_importer

class TestCustomerImporter(unittest.TestCase):

    def test_import_customers(self):
        def assertCustomerEqual(customer1, customer2):
            self.assertEqual(customer1.user_id, customer2.user_id)
            self.assertEqual(customer1.name, customer2.name)
            self.assertEqual(customer1.latitude, customer2.latitude)
            self.assertEqual(customer1.longitude, customer2.longitude)

        read_data = '{\"latitude\": \"52.986375\", \"user_id\": 12, \"name\": \"Christina McArdle\", \"longitude\": \"-6.043701\"}\n{\"latitude\": \"51.92893\", \"user_id\": 1, \"name\": \"Alice Cahill\", \"longitude\": \"-10.27699\"}'
        with patch('builtins.open', mock_open(read_data=read_data)) as m:
            
            result = customer_importer.import_customers('filename')

            expected_imported_customers = []
            expected_imported_customers.append(customer_importer.Customer('52.986375', 12, 'Christina McArdle', '-6.043701'))
            expected_imported_customers.append(customer_importer.Customer('51.92893', 1, 'Alice Cahill', '-10.27699'))

            m.assert_called_once_with('filename')
            assertCustomerEqual(result[0], expected_imported_customers[0])
            assertCustomerEqual(result[1], expected_imported_customers[1])