import unittest
from src.lab2.caesar123 import encrypt_caesar, decrypt_caesar

class TestCaesarCipher(unittest.TestCase):

    def test_encrypt_caesar(self):
        self.assertEqual(encrypt_caesar("PYTHON"), "SBWKRQ")
        self.assertEqual(encrypt_caesar("python"), "sbwkrq")
        self.assertEqual(encrypt_caesar("Python3.6"), "Sbwkrq3.6")
        self.assertEqual(encrypt_caesar(""), "")
        self.assertEqual(encrypt_caesar("123!@#"), "123!@#")

    def test_decrypt_caesar(self):
        self.assertEqual(decrypt_caesar("SBWKRQ"), "PYTHON")
        self.assertEqual(decrypt_caesar("sbwkrq"), "python")
        self.assertEqual(decrypt_caesar("Sbwkrq3.6"), "Python3.6")
        self.assertEqual(decrypt_caesar(""), "")
        self.assertEqual(decrypt_caesar("123!@#"), "123!@#")

if __name__ == '__main__':
    unittest.main()
