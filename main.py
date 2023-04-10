import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


from caesar_encrypt import caesar_encrypt
from caesar_decrypt import caesar_decrypt


from vigenere_decrypt import vigenere_decrypt
from vigenere_encrypt import vigenere_encrypt


from vernam_encrypt import vernam_encrypt
from vernam_decrypt import vernam_decrypt


from appilcation_class import Application

root = tk.Tk()
app = Application(master=root)
app.mainloop()

