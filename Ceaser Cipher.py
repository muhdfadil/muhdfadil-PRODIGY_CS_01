import tkinter as tk

# Caesar Cipher Encryption Function
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                encrypted_text += chr(shifted)
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                encrypted_text += chr(shifted)
        else:
            encrypted_text += char  # Non-alphabetical characters remain the same
    return encrypted_text

# Caesar Cipher Decryption Function
def decrypt(text, shift):
    return encrypt(text, -shift)

# Function to handle encryption
def handle_encrypt():
    text = entry_text.get()
    shift = int(entry_shift.get())
    result = encrypt(text, shift)
    result_label.config(text=f"Encrypted Text: {result}")

# Function to handle decryption
def handle_decrypt():
    text = entry_text.get()
    shift = int(entry_shift.get())
    result = decrypt(text, shift)
    result_label.config(text=f"Decrypted Text: {result}")

# Create the main application window
root = tk.Tk()
root.title("Caesar Cipher")

# Create and place widgets
label_text = tk.Label(root, text="Enter your message:")
label_text.pack()

entry_text = tk.Entry(root, width=50)
entry_text.pack()

label_shift = tk.Label(root, text="Enter the shift value:")
label_shift.pack()

entry_shift = tk.Entry(root, width=10)
entry_shift.pack()

encrypt_button = tk.Button(root, text="Encrypt", command=handle_encrypt)
encrypt_button.pack(pady=5)

decrypt_button = tk.Button(root, text="Decrypt", command=handle_decrypt)
decrypt_button.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Start the application
root.mainloop()
