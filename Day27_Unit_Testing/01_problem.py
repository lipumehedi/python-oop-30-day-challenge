import unittest

class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


class TestCalculator(unittest.TestCase):

    def test_add(self):
        calc = Calculator()
        result = calc.add(2, 3)
        self.assertEqual(result, 5)
        
    def test_subtract(self):
        calc = Calculator()
        result = calc.subtract(5, 3)
        self.assertEqual(result, 2)


if __name__ == "__main__":
    unittest.main()