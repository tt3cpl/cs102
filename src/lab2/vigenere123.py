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

    keyword_index = 0
    for p in plaintext:
        if p.isalpha():  
            shift = ord(keyword_repeated[keyword_index]) - ord('A')
            encrypted_char = chr((ord(p) - ord('A') + shift) % 26 + ord('A'))
            ciphertext.append(encrypted_char)
            keyword_index += 1  
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

    keyword_index = 0
    for c in ciphertext:
        if c.isalpha():  
            shift = ord(keyword_repeated[keyword_index]) - ord('A')
            decrypted_char = chr((ord(c) - ord('A') - shift) % 26 + ord('A'))
            plaintext.append(decrypted_char)
            keyword_index += 1 
        else:
            plaintext.append(c)

    return ''.join(plaintext)