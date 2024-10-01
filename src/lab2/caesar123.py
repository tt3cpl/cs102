import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    ciphertext = ""

    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                prom = ord('A')
            else:
                prom = ord('a')
            new_symb = chr((ord(char) - prom + shift) % 26 + prom)
            ciphertext += new_symb
        else:
            ciphertext += char

    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    plaintext = ""

    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                prom = ord('A')
            else:
                prom = ord('a')
            new_symb = chr((ord(char) - prom - shift) % 26 + prom)
            plaintext += new_symb
        else:
            plaintext += char

    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift



input_text = "PyTHon3.6"
ciphertext = encrypt_caesar(input_text)
print(ciphertext)


input_text = "SbWKrq3.6"
plaintext = decrypt_caesar(input_text)
print(plaintext)
