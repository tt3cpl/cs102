def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """

    ciphertext = []
    keyword_length = len(keyword)
    j = 0

    for char in plaintext:
        if char.isalpha():
            shift = (ord(keyword[j % keyword_length].upper()) - ord('A'))
            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            ciphertext.append(encrypted_char)
            j += 1
        else:
            ciphertext.append(char)

    return ''.join(ciphertext)


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """


    plaintext = []
    keyword_length = len(keyword)
    j = 0

    for char in ciphertext:
        if char.isalpha():
            shift = (ord(keyword[j % keyword_length].upper()) - ord('A'))
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift + 26) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - shift + 26) % 26 + ord('a'))
            plaintext.append(decrypted_char)
            j += 1
        else:
            plaintext.append(char)

    return ''.join(plaintext)