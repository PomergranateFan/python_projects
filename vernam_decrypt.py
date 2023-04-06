def vernam_decrypt(cipher_text, key):
    """Decrypt ciphertext encrypted with Vernam cipher using the given key"""
    plain_text = ""
    for i in range(len(cipher_text)):
        shifted = chr(ord(cipher_text[i]) ^ ord(key[i % len(key)]))
        plain_text += shifted
    return plain_text


