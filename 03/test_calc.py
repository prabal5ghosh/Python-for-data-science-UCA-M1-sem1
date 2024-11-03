# test_calc.py

import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_plus(self):
        self.assertEqual(calc.plus(1, 1), 2)
        self.assertEqual(calc.plus(1, 0), 1)
        self.assertEqual(calc.plus(1, -1), 0)
        self.assertEqual(calc.plus(-1, -1), -2)

    def test_divide(self):
        self.assertEqual(calc.divide(4, 2), 2)
        with self.assertRaises(ZeroDivisionError):
            calc.divide(4, 0)
        with self.assertRaises(TypeError):
            calc.divide(4, '2')

    def test_square(self):
        self.assertEqual(calc.square(2), 4)

if __name__ == "__main__":
    unittest.main()
