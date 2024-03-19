import pyAesCrypt
from tkinter import *
from tkinter import filedialog

def encrypt():
# Get the message from the user input
    message = input_field.get()
# Encrypt the message using pyAesCrypt
    encrypted_message = pyAesCrypt.encrypt(message, password, buffer_size)
# Write the encrypted message to a file
    with open("encrypted_message.txt", "w") as file:
     file.write(encrypted_message)
# Output a message to the user
    output_label.config(text="Encrypted message has been saved to encrypted_message.txt.")

def decrypt():
# Open a file dialog to select the encrypted message file
    file_path = filedialog.askopenfilename()
# Read the encrypted message from the selected file
    with open(file_path, "r") as file:
     encrypted_message = file.read()
# Decrypt the message using pyAesCrypt
    decrypted_message = pyAesCrypt.decrypt(encrypted_message, password, buffer_size)
# Output the decrypted message to the user
    output_label.config(text="Decrypted message: " + decrypted_message)

password = "secret"
buffer_size = 64 * 1024

window = Tk()
window.title("AES Encryption/Decryption")

input_field = Entry(window)
input_field.pack()

encrypt_button = Button(window, text="Encrypt", command=encrypt)
encrypt_button.pack()
decrypt_button = Button(window, text="Decrypt", command=decrypt)
decrypt_button.pack()

output_label = Label(window)
output_label.pack()

window.mainloop()