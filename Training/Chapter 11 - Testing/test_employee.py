import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """A test case for the Employee class."""

    def setUp(self):
        """Create a sample employee instance."""
        self.employee = Employee('John', 'Doe', 60000)

    def test_give_default_raise(self):
        """Test giving the default raise amount."""
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 65000)

    def test_give_custom_raise(self):
        """Test giving a custom raise amount."""
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.annual_salary, 70000)

if __name__ == '__main__':
    unittest.main()