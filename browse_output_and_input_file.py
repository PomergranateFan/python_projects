    def browse_input_file(self):
        """Open file dialog to select input file"""
        self.input_file_path = filedialog.askopenfilename()
        self.input_path_label.config(text=self.input_file_path)

    def browse_output_file(self):
        """Open file dialog to select output file"""
        self.output_file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        self.output_path_label.config(text=self.output_file_path)


