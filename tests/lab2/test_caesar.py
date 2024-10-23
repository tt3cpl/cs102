import unittest
import src.lab2.caesar123 
import random
import string

class CaesarTestCase(unittest.TestCase):
    def test_encrypt(self):
        cases = [
            ("", 0, ""),
            ("python", 0, "python"),
            ("PYTHON", 0, "PYTHON"),
            ("Python", 0, "Python"),
            ("Python3.6", 0, "Python3.6"),
            ("", 3, ""),
            ("PYTHON", 3, "SBWKRQ"),
            ("python", 3, "sbwkrq"),
            ("Python", 3, "Sbwkrq"),
            ("Python3.6", 3, "Sbwkrq3.6"),
        ]

        for i, (plaintext, shift, chiphertext) in enumerate(cases):
            with self.subTest(case=i, plaintext=plaintext, chiphertext=chiphertext):
                self.assertEqual(chiphertext, src.lab2.caesar123 .encrypt_caesar(plaintext, shift=shift))

    def test_decrypt(self):
        cases = [
            ("", 0, ""),
            ("python", 0, "python"),
            ("PYTHON", 0, "PYTHON"),
            ("Python", 0, "Python"),
            ("Python3.6", 0, "Python3.6"),
            ("", 3, ""),
            ("SBWKRQ", 3, "PYTHON"),
            ("sbwkrq", 3, "python"),
            ("Sbwkrq", 3, "Python"),
            ("Sbwkrq3.6", 3, "Python3.6"),
        ]

        for i, (chiphertext, shift, plaintext) in enumerate(cases):
            with self.subTest(case=i, chiphertext=chiphertext, plaintext=plaintext):
                self.assertEqual(plaintext, src.lab2.caesar123.decrypt_caesar(chiphertext, shift=shift))

    def test_randomized(self):
        shift = random.randint(8, 24)
        plaintext = "".join(random.choice(string.ascii_letters + " -,") for _ in range(64))
        ciphertext = src.lab2.caesar123.encrypt_caesar(plaintext, shift=shift)
        self.assertEqual(
            plaintext,
            src.lab2.caesar123.decrypt_caesar(ciphertext, shift=shift),
            msg=f"shift={shift}, ciphertext={ciphertext}",
        )