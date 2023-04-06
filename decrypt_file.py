    def decrypt(self):
        """Decrypt input file and save to output file"""
        plain_text = ""
        with open(self.input_file_path, "r") as f:
            cipher_text = f.read().strip()
        key = self.key_entry.get()
        cipher_type = self.cipher_variable.get()

        if cipher_type == "Caesar":
            plain_text = caesar_decrypt(cipher_text, int(key))
        elif cipher_type == "Vigenere":
            plain_text = vigenere_decrypt(cipher_text, key)
        elif cipher_type == "Vernam":
            plain_text = vernam_decrypt(cipher_text, key)

        with open(self.output_file_path, "w") as f:
            f.write(plain_text)
        messagebox.showinfo("Decryption", "Decryption successful!")

