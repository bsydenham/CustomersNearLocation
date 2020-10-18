import unittest
import pathlib
from customers_near_location import customers_near_location

class TestIntegration(unittest.TestCase):
    def test_integration(self):
        f = pathlib.Path('output.txt')
        if f.is_file():
            f.unlink()

        customers_near_location.get_customers_near_location()

        f = pathlib.Path('output.txt')

        self.assertIs(f.is_file(), True)