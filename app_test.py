import unittest
from app import add_numbers

# Assuming the add_numbers function is already defined in the same file
# or imported from another module.

class TestAddNumbers(unittest.TestCase):
    # Test valid integer inputs
    def test_valid_inputs(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 5), 4)
        self.assertEqual(add_numbers(0, 0), 0)
        self.assertEqual(add_numbers(-3, -7), -10)

    # Test invalid inputs (non-integer)
    def test_invalid_inputs(self):
        self.assertEqual(add_numbers(2.5, 3), "Inputs must be integers!")
        self.assertEqual(add_numbers("2", 3), "Inputs must be integers!")
        self.assertEqual(add_numbers(None, 3), "Inputs must be integers!")
        self.assertEqual(add_numbers(3, [1, 2]), "Inputs must be integers!")

    # Test when only one input is invalid
    def test_one_invalid_input(self):
        self.assertEqual(add_numbers(5, "ten"), "Inputs must be integers!")
        self.assertEqual(add_numbers("ten", 5), "Inputs must be integers!")
        self.assertEqual(add_numbers(5.5, 1), "Inputs must be integers!")

    # Test edge cases with large integer values
    def test_large_values(self):
        self.assertEqual(add_numbers(10**10, 10**10), 2 * 10**10)
        self.assertEqual(add_numbers(-10**10, 10**10), 0)

if __name__ == '__main__':
    unittest.main()