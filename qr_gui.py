import qrcode
import tkinter as tk
from tkinter import messagebox

def generate_qr():
    message = "Hello indu !welcome to my qrcode  sare na  byee ."
    qr = qrcode.make(message)
    qr.save("my_qrcode.png")
    messagebox.showinfo("Success", "QR Code saved as 'my_qrcode.png'")

root = tk.Tk()
root.title("QR Code Generator")

generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack(padx=20, pady=20)

root.mainloop()
