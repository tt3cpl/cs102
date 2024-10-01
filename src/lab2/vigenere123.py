def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    ciphertext = ""
    key_length = len(key)
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            prom = ord('A')
            step = ord(key[key_index % key_length].upper()) - prom
            new_symb = chr((ord(char.upper()) - prom + step) % 26 + prom)
            ciphertext += new_symb
            key_index += 1
        else:
            ciphertext += char

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    plaintext = ""
    key_length = len(key)
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            prom = ord('A')
            step = ord(key[key_index % key_length].upper()) - prom
            new_symb = chr((ord(char.upper()) - prom - step) % 26 + prom)
            plaintext += new_symb
            key_index += 1
        else:
            plaintext += char

    return plaintext


input_text = "ATTACKATDAWN"
key = "LEMONLEMONLE"
encoded = encrypt_vigenere(input_text, key)
print(encoded)


input_text = "LXFOPVEFRNHR"
key = "LEMONLEMONLE"
decoded = decrypt_vigenere(input_text, key)
print(decoded)
