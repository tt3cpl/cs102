
import src.lab2.rsa123
import random
import unittest




class RSATestCase(unittest.TestCase):
    def test_is_prime(self):
        self.assertFalse(src.lab2.rsa123.is_prime(1))
        self.assertTrue(src.lab2.rsa123.is_prime(2))
        self.assertTrue(src.lab2.rsa123.is_prime(3))
        self.assertFalse(src.lab2.rsa123.is_prime(4))
        self.assertTrue(src.lab2.rsa123.is_prime(5))
        self.assertFalse(src.lab2.rsa123.is_prime(6))
        self.assertTrue(src.lab2.rsa123.is_prime(7))
        self.assertFalse(src.lab2.rsa123.is_prime(8))
        self.assertTrue(src.lab2.rsa123.is_prime(3571))

    def test_gcd(self):
        self.assertEqual(0, src.lab2.rsa123.gcd(0, 0))
        self.assertEqual(1, src.lab2.rsa123.gcd(3, 7))
        self.assertEqual(3, src.lab2.rsa123.gcd(12, 15))
        self.assertEqual(9, src.lab2.rsa123.gcd(0, 9))
        self.assertEqual(12, src.lab2.rsa123.gcd(12, 0))
        self.assertEqual(14, src.lab2.rsa123.gcd(42, 56))
        self.assertEqual(18, src.lab2.rsa123.gcd(461952, 116298))
        self.assertEqual(32, src.lab2.rsa123.gcd(7966496, 314080416))
        self.assertEqual(526, src.lab2.rsa123.gcd(24826148, 45296490))

    def test_multiplicative_inverse(self):
        self.assertEqual(23, src.lab2.rsa123.multiplicative_inverse(7, 40))
        self.assertEqual(1969, src.lab2.rsa123.multiplicative_inverse(42, 2017))
        self.assertEqual(0, src.lab2.rsa123.multiplicative_inverse(40, 1))
        self.assertEqual(169, src.lab2.rsa123.multiplicative_inverse(121, 288))
        self.assertEqual(734969, src.lab2.rsa123.multiplicative_inverse(142169, 1694640))
        self.assertEqual(1804547, src.lab2.rsa123.multiplicative_inverse(9678731, 11181456))

    def test_generate_keypair(self):
        random.seed(1234567)
        self.assertEqual(((121, 323), (169, 323)), src.lab2.rsa123.generate_keypair(17, 19))
        self.assertEqual(((142169, 1697249), (734969, 1697249)), src.lab2.rsa123.generate_keypair(1229, 1381))
        self.assertEqual(
            ((9678731, 11188147), (1804547, 11188147)), src.lab2.rsa123.generate_keypair(3259, 3433)
        )