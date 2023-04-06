    def encrypt(self):
        """Encrypt input file and save to output file"""
        cipher_text = ""
        with open(self.input_file_path, "r") as f:
            plain_text = f.read().strip()
        key = self.key_entry.get()
        cipher_type = self.cipher_variable.get()

        if cipher_type == "Caesar":
            cipher_text = caesar_encrypt(plain_text, int(key))
        elif cipher_type == "Vigenere":
            cipher_text = vigenere_encrypt(plain_text, key)
        elif cipher_type == "Vernam":
            cipher_text = vernam_encrypt(plain_text, key)

        with open(self.output_file_path, "w") as f:
            f.write(cipher_text)
        messagebox.showinfo("Encryption", "Encryption successful!")

