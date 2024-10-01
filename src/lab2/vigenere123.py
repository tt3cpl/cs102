def encrypt_vigenere(plaintext, keyword):
    """
    Encrypts plaintext using the Vigenère cipher with the provided keyword.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    plaintext = plaintext.upper()
    keyword = keyword.upper()
    ciphertext = []
    keyword_repeated = (keyword * (len(plaintext) // len(keyword) + 1))[:len(plaintext)]

    for p, k in zip(plaintext, keyword_repeated):
        if p.isalpha():
            shift = ord(k) - ord('A')
            encrypted_char = chr((ord(p) - ord('A') + shift) % 26 + ord('A'))
            ciphertext.append(encrypted_char)
        else:
            ciphertext.append(p)

    return ''.join(ciphertext)


def decrypt_vigenere(ciphertext, keyword):
    """
    Decrypts ciphertext using the Vigenère cipher with the provided keyword.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    ciphertext = ciphertext.upper()
    keyword = keyword.upper()
    plaintext = []
    keyword_repeated = (keyword * (len(ciphertext) // len(keyword) + 1))[:len(ciphertext)]

    for c, k in zip(ciphertext, keyword_repeated):
        if c.isalpha():
            shift = ord(k) - ord('A')
            decrypted_char = chr((ord(c) - ord('A') - shift) % 26 + ord('A'))
            plaintext.append(decrypted_char)
        else:
            plaintext.append(c)

    return ''.join(plaintext)

