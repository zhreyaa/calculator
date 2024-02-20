import unittest
from calculator import square_root, factorial, natural_logarithm, power, addition, subtraction, multiplication, division

class TestCalculatorFunctions(unittest.TestCase):
    
    def test_square_root(self):
        self.assertEqual(square_root(9), 3)
        self.assertAlmostEqual(square_root(2), 1.41421356, places=5)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)

    def test_natural_logarithm(self):
        self.assertAlmostEqual(natural_logarithm(1), 0.0)
        self.assertAlmostEqual(natural_logarithm(10), 2.30258509, places=5)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertAlmostEqual(power(2, 0.5), 1.41421356, places=5)

    def test_addition(self):
        self.assertEqual(addition(5, 3), 8)
        self.assertEqual(addition(-2, 3), 1)

    def test_subtraction(self):
        self.assertEqual(subtraction(5, 3), 2)
        self.assertEqual(subtraction(-2, 3), -5)

    def test_multiplication(self):
        self.assertEqual(multiplication(5, 3), 15)
        self.assertEqual(multiplication(-2, 3), -6)

    def test_division(self):
        self.assertEqual(division(10, 2), 5)
        self.assertEqual(division(5, 2), 2.5)
        self.assertEqual(division(10, 0), "Error: Division by zero!")


if __name__ == '__main__':
    unittest.main()

