"""Calculator testing"""
import unittest
from src.lab1.calculator import calc


class CalculatorTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(calc('3 + 4'), 7)

    def test_2(self):
        self.assertEqual(calc('3 * 4'), 12)

    def test_3(self):
        self.assertEqual(calc('3 / 4'), 0.75)

    def test_4(self):
        self.assertEqual(calc('3 // 4'), 0)

    def test_5(self):
        self.assertEqual(calc('5 - 4'), 1)

    def test_6(self):
        self.assertEqual(calc('3 % 4'), 3)

    def test_7(self):
        self.assertEqual(calc('3.5 + 4'), 7.5)

    def test_8(self):
        self.assertEqual(calc('3 / 0'), 'Error')

    def test_9(self):
        self.assertEqual(calc('fghdgf fdfgudf'), 'Error')
