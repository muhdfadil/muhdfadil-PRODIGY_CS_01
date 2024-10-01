# Caesar Cipher Implementation

This project is a Python-based implementation of the Caesar Cipher encryption and decryption algorithm. The Caesar Cipher is a type of substitution cipher where each letter in the plaintext is shifted by a certain number of positions to generate the ciphertext. Users can input a message, choose a shift value, and specify whether they want to encrypt or decrypt the message.

## Features

- **Encrypt text**: Shift letters forward in the alphabet by a specified value.
- **Decrypt text**: Shift letters backward to restore the original message.
- **Custom shift value**: The user can define how many positions to shift the text.
- **Simple command-line interface**: Users interact with the program via the command line.

## How It Works

- The user inputs the text they want to encrypt or decrypt.
- A shift value (positive integer) is provided.
- The program processes the input text:
  - For encryption, letters are shifted forward.
  - For decryption, letters are shifted backward.
- The program returns the result (either encrypted or decrypted text).

## Example Usage

### Encryption
```bash
$ python3 caesar_cipher.py
Enter the text: hello fadil
Enter the shift value: 3
Choose mode ('encrypt' or 'decrypt'): encrypt
Result: khoor idglo
