def encrypt_vigenere(plain_text, key):
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """

    encrypted_text = ''
    key_repeated = (key * (len(plain_text) // len(key))) + key[:len(plain_text) % len(key)]
   # Iterate through each character in the plaintext.
    for i in range(len(plain_text)):
       # Check if the character is an alphabet letter.
        if plain_text[i].isalpha():
           # Calculate the shift based on the corresponding key letter.
            shift = ord(key_repeated[i].upper()) - ord('A')
           # Encrypt uppercase and lowercase letters separately.
            if plain_text[i].isupper():
               encrypted_text += chr((ord(plain_text[i]) + shift - ord('A')) % 26 + ord('A'))
            else:
               encrypted_text += chr((ord(plain_text[i]) + shift - ord('a')) % 26 + ord('a'))
        else:
           # If the character is not an alphabet letter, keep it unchanged.
           encrypted_text += plain_text[i]
   # Return the final encrypted text
    return encrypted_text


def decrypt_vigenere(cipher_text, key):
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    decrypted_text = ''
    # Repeat the key to match the length of the ciphertext
    key_repeated = (key * (len(cipher_text) // len(key))) + key[:len(cipher_text) % len(key)]
    # Iterate through each character in the ciphertext
    for i in range(len(cipher_text)):
        # Check if the character is an alphabet letter
        if cipher_text[i].isalpha():
            # Calculate the shift based on the corresponding key letter
            shift = ord(key_repeated[i].upper()) - ord('A')
            # Decrypt uppercase and lowercase letters separately
            if cipher_text[i].isupper():
                decrypted_text += chr((ord(cipher_text[i]) - shift - ord('A')) % 26 + ord('A'))
            else:
                decrypted_text += chr((ord(cipher_text[i]) - shift - ord('a')) % 26 + ord('a'))
        else:
            # If the character is not an alphabet letter, keep it unchanged
            decrypted_text += cipher_text[i]
    # Return the final decrypted text
    return decrypted_text