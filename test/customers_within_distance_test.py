import unittest
import sys
sys.path.append(".")
from customers_near_location import customer_importer
from customers_near_location import customers_within_distance

class TestCustomersWithinDistance(unittest.TestCase):
    
    def setUp(self):
        self.DISTANCE = 100
        self.LOCATION = (53.339428, -6.257664)

    def test_get_customers_within_distance_filters(self):
        customers = []
        customers.append(customer_importer.Customer('52.986375', 1, 'customer1', '-6.043701'))
        customers.append(customer_importer.Customer('51.92893', 2, 'customer1', '-10.27699'))
        
        filtered_customers = customers_within_distance.get_customers_within_distance(customers, self.LOCATION, self.DISTANCE)

        self.assertEqual(len(filtered_customers), 1)
        self.assertEqual(filtered_customers[0].user_id, 1)
    
    def test_get_customers_within_distance_sorts_asc(self):
        customers = []
        customers.append(customer_importer.Customer('52.986375', 2, 'customer2', '-6.043701'))
        customers.append(customer_importer.Customer('52.966', 1, 'customer1', '-6.463'))

        filtered_customers = customers_within_distance.get_customers_within_distance(customers, self.LOCATION, self.DISTANCE)

        self.assertEqual(len(filtered_customers), 2)
        self.assertEqual(filtered_customers[0].user_id, 1)
        self.assertEqual(filtered_customers[1].user_id, 2)