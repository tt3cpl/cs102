def encrypt_caesar(plaintext, shift: int = 3):
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
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():  
            shift_amount = shift % 26  
            
            if char.isupper():
                shifted_char = chr(((ord(char) - ord('A') + shift_amount) % 26) + ord('A'))
            else:
                shifted_char = chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a'))
        else:
            shifted_char = char
        ciphertext += shifted_char
    return ciphertext



def decrypt_caesar(ciphertext, shift: int = 3):
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
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():  
            shift_amount = shift % 26  
            
            if char.isupper():
                shifted_char = chr(((ord(char) - ord('A') - shift_amount) % 26) + ord('A'))
            else: 
                shifted_char = chr(((ord(char) - ord('a') - shift_amount) % 26) + ord('a'))
        else:
            shifted_char = char  

        plaintext += shifted_char
    return plaintext

