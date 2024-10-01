def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    ciphertext = ""
    key_length = len(keyword)
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                prom = ord('A')
            else:
                prom = ord('a')
            step = ord(keyword[key_index % key_length].upper()) - ord('A')
            new_symb = chr((ord(char) - prom + step) % 26 + prom)
            ciphertext += new_symb
            key_index += 1
        else:
            ciphertext += char

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    plaintext = ""
    key_length = len(keyword)
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                prom = ord('A')
            else:
                prom = ord('a')
            step = ord(keyword[key_index % key_length].upper()) - ord('A')
            new_symb = chr((ord(char) - prom - step) % 26 + prom)
            plaintext += new_symb
            key_index += 1
        else:
            plaintext += char

    return plaintext



input_text = "ATTACKATDAWN"
key = "LEMONLEMONLE"
encoded = encrypt_vigenere(input_text, key)
print(encoded)

decoded = decrypt_vigenere(encoded, key)
print(decoded) 
