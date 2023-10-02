"""Testing"""
import unittest
from src.lab2.caesar import encrypt_caesar
from src.lab2.caesar import decrypt_caesar
from src.lab2.vigenre import encrypt_vigenere
from src.lab2.vigenre import decrypt_vigenere
from src.lab2.rsa import gcd
from src.lab2.rsa import multiplicative_inverse
from src.lab2.rsa import is_prime


class Lab2TestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(encrypt_caesar('PYTHON'), 'SBWKRQ')

    def test_2(self):
        self.assertEqual(encrypt_caesar('python'), 'sbwkrq')

    def test_3(self):
        self.assertEqual(encrypt_caesar('Python3.6'), 'Sbwkrq3.6')

    def test_4(self):
        self.assertEqual(decrypt_caesar('SBWKRQ'), 'PYTHON')

    def test_5(self):
        self.assertEqual(decrypt_caesar('sbwkrq'), 'python')

    def test_6(self):
        self.assertEqual(decrypt_caesar('Sbwkrq3.6'), 'Python3.6')

    def test_7(self):
        self.assertEqual(encrypt_vigenere("PYTHON", "A"), 'PYTHON')

    def test_8(self):
        self.assertEqual(encrypt_vigenere("python", "a"), 'python')

    def test_9(self):
        self.assertEqual(encrypt_vigenere("", ""), 'Error')

    def test_10(self):
        self.assertEqual(encrypt_vigenere("ATTACKATDAWN", "LEMON"), 'LXFOPVEFRNHR')

    def test_11(self):
        self.assertEqual(decrypt_vigenere("PYTHON", "A"), 'PYTHON')

    def test_12(self):
        self.assertEqual(decrypt_vigenere("python", "a"), 'python')

    def test_13(self):
        self.assertEqual(decrypt_vigenere("", ""), 'Error')

    def test_14(self):
        self.assertEqual(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"), 'ATTACKATDAWN')

    def test_15(self):
        self.assertEqual(gcd(12, 15), 3)

    def test_16(self):
        self.assertEqual(gcd(3, 7), 1)

    def test_17(self):
        self.assertEqual(gcd(0, 0), 0)

    def test_18(self):
        self.assertEqual(is_prime(0), False)

    def test_19(self):
        self.assertEqual(is_prime(1), True)

    def test_20(self):
        self.assertEqual(is_prime(2), True)

    def test_21(self):
        self.assertEqual(is_prime(11), True)

    def test_22(self):
        self.assertEqual(is_prime(-8), False)

    def test_23(self):
        self.assertEqual(multiplicative_inverse(7, 40), 23)

    def test_24(self):
        self.assertEqual(multiplicative_inverse(0, 0), 'Error')

    def test_25(self):
        self.assertEqual(multiplicative_inverse(25, 72), 49)

    def test_26(self):
        self.assertEqual(encrypt_caesar(''), '')

    def test_27(self):
        self.assertEqual(decrypt_caesar(''), '')

    def test_28(self):
        self.assertEqual(multiplicative_inverse(40, 1), 0)

    def test_29(self):
        self.assertEqual(multiplicative_inverse(42, 2017), 1969)
