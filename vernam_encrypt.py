def vernam_encrypt(plain_text, key):
    """Encrypt plaintext with Vernam cipher using the given key"""
    cipher_text = ""
    for i in range(len(plain_text)):
        shifted = chr(ord(plain_text[i]) ^ ord(key[i % len(key)]))
        cipher_text += shifted
    return cipher_text



