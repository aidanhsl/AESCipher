AES Encryption/Decryption Tool

This Python application provides a graphical user interface (GUI) to encrypt and decrypt messages using AES encryption. It leverages the pyAesCrypt library for encryption and decryption and Tkinter for the GUI.
Requirements

    Python 3.x
    pyAesCrypt library (pip install pyAesCrypt)

Code Overview

The application allows users to:

    Enter a message to encrypt and save it to a file.
    Select an encrypted file to decrypt and view the original message.

Files

    encrypted_message.txt: File where encrypted messages are stored.

How to Use

    Launch the Application:
        Run the script to open a simple Tkinter window.
    Encrypt a Message:
        Enter the message in the input field.
        Click the "Encrypt" button. The message will be encrypted with a preset password and stored in encrypted_message.txt.
    Decrypt a Message:
        Click the "Decrypt" button and select an encrypted file.
        The decrypted message will display in the application window.

Code Details
Libraries

    pyAesCrypt: Provides AES encryption/decryption.
    tkinter: Creates the GUI components.

Main Functions

    encrypt():
        Reads user input, encrypts it with AES, and saves it to a file.
    decrypt():
        Prompts the user to select a file, decrypts the content, and displays the original message.

Security Note

    The current implementation uses a hardcoded password ("secret"). For cryptographic purposes, change the hardcoded password to a hashed value after user input. 
