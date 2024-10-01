import random
from math import gcd


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def multiplicative_inverse(e, phi):
    
    def egcd(a, b):
        if a == 0:
            return b, 0, 1
        g, x, y = egcd(b % a, a)
        return g, y - (b // a) * x, x
    
    g, x, y = egcd(e, phi)
    if g != 1:
        raise Exception('Multiplicative inverse does not exist.')
    else:
        return x % phi

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    # n = p * q
    n = p * q

    # phi = (p-1) * (q-1)
    phi = (p - 1) * (q - 1)

   
    e = random.randrange(1, phi)

   
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = multiplicative_inverse(e, phi)


    return ((e, n), (d, n))
