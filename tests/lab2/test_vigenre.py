import unittest
from src.lab2.vigenere123 import encrypt_vigenere, decrypt_vigenere

class TestVigenereCipher(unittest.TestCase):
    
    def test_encrypt_vigenere(self):
        self.assertEqual(encrypt_vigenere("PYTHON", "A"), "PYTHON")
        self.assertEqual(encrypt_vigenere("python", "a"), "python")
        self.assertEqual(encrypt_vigenere("ATTACKATDAWN", "LEMON"), "LXFOPVEFRNHR")
        self.assertEqual(encrypt_vigenere("HELLO WORLD!", "KEY"), "RIJVS UYVJN!")
        self.assertEqual(encrypt_vigenere("12345", "KEY"), "12345")

    def test_decrypt_vigenere(self):
        self.assertEqual(decrypt_vigenere("PYTHON", "A"), "PYTHON")
        self.assertEqual(decrypt_vigenere("python", "a"), "python")
        self.assertEqual(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"), "ATTACKATDAWN")
        self.assertEqual(decrypt_vigenere("RIJVS UYVJN!", "KEY"), "HELLO WORLD!")
        self.assertEqual(decrypt_vigenere("12345", "KEY"), "12345")

if __name__ == '__main__':
    unittest.main()
