import unittest
from old_calc import OldCalculator
from refactored_calc import RefactoredCalculator as OldCalculator


class TestOldCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = OldCalculator()

    def test_add(self):
        self.assertEqual(self.calc.calculate(2, 3, "add"), 5)

    def test_sub(self):
        self.assertEqual(self.calc.calculate(5, 2, "sub"), 3)

    def test_mul(self):
        self.assertEqual(self.calc.calculate(3, 4, "mul"), 12)

    def test_div(self):
        self.assertEqual(self.calc.calculate(10, 2, "div"), 5)
        with self.assertRaises(ValueError):
            self.calc.calculate(5, 0, "div")

    def test_invalid(self):
        with self.assertRaises(ValueError):
            self.calc.calculate(3, 4, "pow")

if __name__ == "__main__":
    unittest.main()