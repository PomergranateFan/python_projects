class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.input_file_path = ""
        self.output_file_path = ""
        self.input_label = tk.Label(self, text="Input File:")
        self.input_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.input_path_label = tk.Label(self, text=self.input_file_path, width=50)
        self.input_path_label.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
        self.browse_input_button = tk.Button(self, text="Browse", command=self.browse_input_file)
        self.browse_input_button.grid(row=0, column=2, padx=5, pady=5)
        self.output_label = tk.Label(self, text="Output File:")
        self.output_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.output_path_label = tk.Label(self, text=self.output_file_path, width=50)
        self.output_path_label.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
        self.browse_output_button = tk.Button(self, text="Browse", command=self.browse_output_file)
        self.browse_output_button.grid(row=1, column=2, padx=5, pady=5)

        self.encrypt_decrypt_label = tk.Label(self, text="Encrypt/Decrypt:")
        self.encrypt_decrypt_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

        self.cipher_variable = tk.StringVar(self)
        self.cipher_variable.set("Caesar")
        self.cipher_dropdown = tk.OptionMenu(self, self.cipher_variable, "Caesar", "Vigenere", "Vernam")
        self.cipher_dropdown.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        self.key_label = tk.Label(self, text="Key:")
        self.key_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.key_entry = tk.Entry(self, width=50)
        self.key_entry.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

        self.encrypt_button = tk.Button(self, text="Encrypt", command=self.encrypt)
        self.encrypt_button.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)
        self.decrypt_button = tk.Button(self, text="Decrypt", command=self.decrypt)
        self.decrypt_button.grid(row=4, column=2, padx=5, pady=5, sticky=tk.W)
        self.quit_button = tk.Button(self, text="Quit", fg="red", command=self.master.destroy)
        self.quit_button.grid(row=5, column=2, padx=5, pady=5)

