def caesar_encrypt(plain_text, shift):
    """Encrypt plaintext with Caesar cipher using the given shift"""
    cipher_text = ""
    for c in plain_text:
        if c.isalpha():
            shifted = chr((ord(c.upper()) - 65 + shift) % 26 + 65)
            cipher_text += shifted
        else:
            cipher_text += c
    return cipher_text

