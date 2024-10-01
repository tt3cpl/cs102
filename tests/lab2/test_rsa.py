import unittest
from math import gcd
from random import randrange

from src.lab2.rsa123 import is_prime, multiplicative_inverse, generate_keypair


class TestRSAFunctions(unittest.TestCase):

    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(-5))

    def test_multiplicative_inverse(self):
        self.assertEqual(multiplicative_inverse(3, 11), 4)  
        self.assertEqual(multiplicative_inverse(7, 40), 23)  

        with self.assertRaises(Exception):
            multiplicative_inverse(2, 4) 

    def test_generate_keypair(self):

        public_key, private_key = generate_keypair(61, 53)
        self.assertEqual(len(public_key), 2)
        self.assertEqual(len(private_key), 2)
        self.assertGreater(public_key[0], 1)
        self.assertGreater(private_key[0], 1)


        self.assertTrue(is_prime(61))
        self.assertTrue(is_prime(53))

        with self.assertRaises(ValueError):
            generate_keypair(4, 9)
        with self.assertRaises(ValueError):
            generate_keypair(5, 5)

if __name__ == '__main__':
    unittest.main()
