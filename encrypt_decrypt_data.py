from cryptography.fernet import Fernet

key = Fernet.generate_key()

fernet = Fernet(key)
textInput = input("Enter the Text to be encoded : ")
encryptedText = fernet.encrypt(textInput.encode())
decryptedText = fernet.decrypt(encryptedText).decode()

print("Original Text : "+ textInput)
print("Encrypted Text : "+ str(encryptedText))
print("Decrypted Text : "+ str(decryptedText))