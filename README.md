# Encryption


This Python script y is designed to encrypt and decrypt files using a simple Feistel cipher implementation. Here’s how it works and how you can use it:




How It Works:

1) Key Generation:

  --It generates keys by defining three initial key segments (KA, KB, KC).

  --These segments are combined through XOR operations to produce three new keys (K1, K2, K3), used for the encryption and decryption processes.

2) Feistel Cipher Implementation:

  --The feistel_crypt function performs encryption or decryption using the Feistel structure. This function divides the data into two halves and processes it over several rounds, applying XOR operations with the keys to transform the data.
  
3) File Handling:

  --The script utilizes tkinter for a graphical user interface to allow file selection through a dialog box.
  
  --It reads the selected file, performs encryption, then decryption, and saves the results to new files.
  
4) Round Configuration:

  --The number of rounds the Feistel cipher runs is predefined (rounds = 3). More rounds generally increase security but also processing time.



How to Use It:

1) Setup:

  --Ensure Python and tkinter are installed on your system.
  --Place the script in a directory where you have read/write permissions because it needs to read and write files.
  
2) Run the Script:

  --Execute the script. A file dialog will open, asking you to select a file to encrypt and decrypt.
  --Choose a file using the dialog. The script will then automatically encrypt and decrypt the file, showing the original, encrypted, and decrypted data in the console.
  
3) Output:

  --After processing, the script saves the encrypted data to encrypted_output.txt and the decrypted data to decrypted_output.txt in the same directory as the script.
  
4) Verification:

  --You can verify the success of the encryption and decryption by comparing the original file contents with the decrypted output. If the process is correct, the decrypted data should match the original data.




