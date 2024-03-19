from Cryptodome.Cipher import AES
from tkinter import *
from tkinter import filedialog

def encrypt():
# Get the message from the user input
message = input_field.get().encode("utf-8")
# Pad the message to be a multiple of 16 bytes
message = message + b" " * (16 - len(message) % 16)
# Encrypt the message using AES
cipher = AES.new(password, AES.MODE_ECB)
encrypted_message = cipher.encrypt(message)
# Write the encrypted message to a file
with open("encrypted_message.txt", "wb") as file:
file.write(encrypted_message)
# Output a message to the user
output_label.config(text="Encrypted message has been saved to encrypted_message.txt.")

def decrypt():
# Open a file dialog to select the encrypted message file
file_path = filedialog.askopenfilename()
# Read the encrypted message from the selected file
with open(file_path, "rb") as file:
encrypted_message = file.read()
# Decrypt the message using AES
cipher = AES.new(password, AES.MODE_ECB)
decrypted_message = cipher.decrypt(encrypted_message)
# Output the decrypted message to the user
output_label.config(text="Decrypted message: " + decrypted_message.decode("utf-8").strip())

password = b"secret"

window = Tk()
window.title("AES Encryption/Decryption")

input_field = Entry(window)
input_field.pack()

encrypt_button = Button(window, text="Encrypt", command=encrypt)
encrypt_button.pack()
decrypt_button = Button(window)