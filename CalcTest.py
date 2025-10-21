import unittest
from Calc import Calculator  # The class we are going to implement

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    # def test_add(self):
    #     calc = Calculator()
    #     result = calc.add(2, 3)
    #     self.assertEqual(result, 5)  # Expect 2 + 3 = 5
    
    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)

    def test_divide(self):
        self.assertAlmostEqual(self.calc.divide(10, 2), 5.0)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)

# if __name__ == "__main__":
#     unittest.main()