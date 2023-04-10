def vigenere_decrypt(cipher_text, keyword):
    """Decrypt ciphertext encrypted with Vigenere cipher using the given keyword"""
    plain_text = ""
    key_index = 0
    for c in cipher_text:
        if c.isalpha():
            shift = ord(keyword[key_index].upper()) - 65
            shifted = chr((ord(c.upper()) - 65 - shift) % 26 + 65)
            plain_text += shifted
            key_index = (key_index + 1) % len(keyword)
        else:
            plain_text += c
    return plain_text

