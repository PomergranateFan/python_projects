def caesar_decrypt(cipher_text, shift):
    """Decrypt ciphertext encrypted with Caesar cipher using the given shift"""
    plain_text = ""
    for c in cipher_text:
        if c.isalpha():
            shifted = chr((ord(c.upper()) - 65 - shift) % 26 + 65)
            plain_text += shifted
        else:
            plain_text += c
    return plain_text

