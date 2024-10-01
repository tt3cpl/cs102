import unittest
from src.lab2.vigenere123 import encrypt_vigenere, decrypt_vigenere

class TestVigenereCipher(unittest.TestCase):
    
    def test_encrypt_vigenere(self):
        self.assertEqual(encrypt_vigenere("PYTHON", "A"), "PYTHON")
        self.assertEqual(encrypt_vigenere("python", "a"), "python")
        self.assertEqual(encrypt_vigenere("ATTACKATDAWN", "LEMON"), "LXFOPVEFRNHR")
        self.assertEqual(encrypt_vigenere("HELLO WORLD!", "KEY"), "RIJVS UYVJN!")
        self.assertEqual(encrypt_vigenere("12345", "KEY"), "12345")
        self.assertEqual(encrypt_vigenere("spaces and punctuation!", "keyword"), "skmctt cxo wqequejbqmc!")
        self.assertEqual(encrypt_vigenere("", "KEY"), "")
        self.assertEqual(encrypt_vigenere("mixed CASE and 123", "MixEd"), "xmqjI EEKD me 123")

    def test_decrypt_vigenere(self):
        self.assertEqual(decrypt_vigenere("PYTHON", "A"), "PYTHON")
        self.assertEqual(decrypt_vigenere("python", "a"), "python")
        self.assertEqual(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"), "ATTACKATDAWN")
        self.assertEqual(decrypt_vigenere("RIJVS UYVJN!", "KEY"), "HELLO WORLD!")
        self.assertEqual(decrypt_vigenere("12345", "KEY"), "12345")
        self.assertEqual(decrypt_vigenere("skmctt cxo wqequejbqmc!", "keyword"), "spaces and punctuation!")
        self.assertEqual(decrypt_vigenere("", "KEY"), "")
        self.assertEqual(decrypt_vigenere("xmqjI EEKD me 123", "MixEd"), "mixed CASE and 123")

if __name__ == '__main__':
    unittest.main()
