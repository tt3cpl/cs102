def encrypt_vigenere(plaintext, keyword):
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    keyword_repeated = (keyword * ((len(plaintext) // len(keyword)) + 1))[:len(plaintext)]
    
    for i in range(len(plaintext)):
        p = plaintext[i]
        k = keyword_repeated[i]

        if 'A' <= p <= 'Z':
            shift = ord(k.upper()) - ord('A')
            ciphertext += chr((ord(p) - ord('A') + shift) % 26 + ord('A'))
        elif 'a' <= p <= 'z':
            shift = ord(k.lower()) - ord('a')
            ciphertext += chr((ord(p) - ord('a') + shift) % 26 + ord('a'))
        else:
            ciphertext += p

    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    keyword_repeated = (keyword * ((len(ciphertext) // len(keyword)) + 1))[:len(ciphertext)]
    
    for i in range(len(ciphertext)):
        c = ciphertext[i]
        k = keyword_repeated[i]

        if 'A' <= c <= 'Z': 
            shift = ord(k.upper()) - ord('A')
            plaintext += chr((ord(c) - ord('A') - shift + 26) % 26 + ord('A'))
        elif 'a' <= c <= 'z':  
            shift = ord(k.lower()) - ord('a')
            plaintext += chr((ord(c) - ord('a') - shift + 26) % 26 + ord('a'))
        else:
            plaintext += c 

    return plaintext
