
def vigenere_encrypt(plain_text, keyword):
    """Encrypt plaintext with Vigenere cipher using the given keyword"""
    cipher_text = ""
    key_index = 0
    for c in plain_text:
        if c.isalpha():
            shift = ord(keyword[key_index].upper()) - 65
            shifted = chr((ord(c.upper()) - 65 + shift) % 26 + 65)
            cipher_text += shifted
            key_index = (key_index + 1) % len(keyword)
        else:
            cipher_text += c
    return cipher_text
