def encrypt_caesar(plaintext):
    """
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    encrypted_text = ""
    for letter in plaintext:
        if 'A' <= letter <= 'Z':
            encrypted_text += chr((ord(letter) - ord('A') + 3) % 26 + ord('A'))
        elif 'a' <= letter <= 'z':
            encrypted_text += chr((ord(letter) - ord('a') + 3) % 26 + ord('a'))
        else:
            encrypted_text += letter
    return encrypted_text


def decrypt_caesar(ciphertext):
    """
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    decrypted_text = ""
    for letter in ciphertext:
        if 'A' <= letter <= 'Z':
            decrypted_text += chr((ord(letter) - ord('A') - 3) % 26 + ord('A'))
        elif 'a' <= letter <= 'z':
            decrypted_text += chr((ord(letter) - ord('a') - 3) % 26 + ord('a'))
        else:
            decrypted_text += letter
    return decrypted_text
