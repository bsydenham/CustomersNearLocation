import unittest
from unittest.mock import patch, mock_open, call
import json
from customers_near_location import customer_importer
from customers_near_location import customer_output

class TestCustomerOutput(unittest.TestCase):
    def test_output_customers(self):
        customers = []
        customers.append(customer_importer.Customer('52.986375', 1, 'Customer1', '-6.043701'))
        customers.append(customer_importer.Customer('52.966', 2, 'Customer2', '-6.463'))

        with patch('builtins.open', mock_open()) as m:
            customer_output1 = customer_output.CustomerOutput(1, 'Customer1')
            customer_output2 = customer_output.CustomerOutput(2, 'Customer2')
            
            customer_output.output_customers('filename', customers)

        m.assert_called_with('filename', 'w')
        m().write.assert_has_calls([
            call(json.dumps(customer_output1.__dict__) + '\n'),
            call(json.dumps(customer_output2.__dict__) + '\n')
        ])