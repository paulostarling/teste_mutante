import unittest

from calculator import calculator


class TestCalculator(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(calculator(1, 4, '+'), 5, "Precisa ser 5")

    def test_subtraction(self):
        self.assertEqual(calculator(-1, 1, '-'), -2, "Precisa ser 1")

    def test_multiplcation(self):
        self.assertEqual(calculator(-5, -2, '*'), 10,  "Precisa ser 1")

    def test_division(self):
        self.assertEqual(calculator(10, 2, '/'), 5,  "Precisa ser 5")
        self.assertNotEqual(calculator(12, 5, '/'), 2,  "Precisa ser 2.4")

    def test_case_invalid_operator(self):
        self.assertEqual(calculator(-1, -1, 'a'), 'You have not typed a valid operator',  "Precisa ser inválido")

if __name__ == '__main__':
    unittest.main()
