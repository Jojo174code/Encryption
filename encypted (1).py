





# define what file I want to encrypyt and maybe assign it to a variable 
# set a 16 bit key to a variable 
# split key into K(A),K(B), and K(C)
# preform XOR opeation between K(A) + K(B) = K(1), K(B) + K(C) = K(2), K(C) + K(A) = K(3) 
# set amount of rounds 
# start fistel encyption pocesss
# save encrypted contents to a file 
# be able to decrypt file also with key 



import tkinter as tk
from tkinter import filedialog
import base64
import os

# Function to allow the user to select a file within their system
def select_file(prompt):
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(title=prompt)  # Open file selection dialog with a custom prompt
    root.destroy()  # Destroy the root window to prevent hanging
    if file_path:
        return file_path
    else:
        print("No file selected for", prompt.lower() + ". Exiting.")
        exit()

# Calculate the XOR results based on the given relationships
def xor_operation(KA, KB, KC):
    K1 = KA ^ KB
    K2 = KB ^ KC
    K3 = KC ^ KA
    return K1 % 256, K2 % 256, K3 % 256

# Simple Feistel encryption and decryption functions
def feistel_crypt(data, keys, rounds, decrypt=False):
    if len(data) % 2 != 0:
        data += b'\x00'
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    sequence = range(rounds - 1, -1, -1) if decrypt else range(rounds)
    for i in sequence:
        temp = left
        left = bytes(a ^ keys[i % len(keys)] for a in right)
        right = temp
    return left + right

# Define the keys and rounds
KA, KB, KC = 1242, 3456, 7876
K1, K2, K3 = xor_operation(KA, KB, KC)
keys = [K1, K2, K3]
rounds = 3

# Select a file to encrypt and decrypt
selected_file = select_file("Select a file to encrypt and decrypt")

# Read the content of the selected file
with open(selected_file, 'rb') as file:
    original_data = file.read()

# Encrypt the data
encrypted_data = feistel_crypt(original_data, keys, rounds)

# Decrypt the data
decrypted_data = feistel_crypt(encrypted_data, keys, rounds, decrypt=True)

# Output to verify if encryption and decryption are correct
print("Original Data: ", original_data)
print("Encrypted Data: ", encrypted_data)
print("Decrypted Data: ", decrypted_data)

# Save the encrypted data to a new file
with open("encrypted_output.txt", 'wb') as outfile:
    outfile.write(encrypted_data)

# Save the decrypted data to verify it matches the original
with open("decrypted_output.txt", 'wb') as outfile:
    outfile.write(decrypted_data)

print("Processes complete. Encrypted and decrypted files are saved.")
