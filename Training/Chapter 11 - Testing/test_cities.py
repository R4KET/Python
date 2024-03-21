import unittest
from city_functions import format_city_country

class CitiesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Does a city and country like 'Santiago, Chile' work?"""
        formatted_name = format_city_country('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago, Chile')

    def test_city_country_population(self):
        """Does a city, country, and population like 'Santiago, Chile - population 5000000' work?"""
        formatted_name = format_city_country('santiago', 'chile', 5000000)
        self.assertEqual(formatted_name, 'Santiago, Chile - population 5000000')

if __name__ == '__main__':
    unittest.main()
