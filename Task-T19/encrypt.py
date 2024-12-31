from cryptography.fernet import Fernet



def encrypt_text(text, key):
    """
    Encrypts a given text using the provided key.

    Parameters:
        text (str): The string of text to be encrypted.
        key (bytes): The key used to encrypt the text.

    Returns:
        bytes: The encrypted text.
    """
    fernet = Fernet(key)
    encrypted_text = fernet.encrypt(text.encode())
    return encrypted_text

def decrypt_text(encrypted_text, key):
    """
    Decrypts an encrypted text using the provided key.

    Parameters:
        encrypted_text (bytes): The encrypted text to be decrypted.
        key (bytes): The key used to decrypt the text.

    Returns:
        str: The decrypted text.
    """
    fernet = Fernet(key)
    decrypted_text = fernet.decrypt(encrypted_text).decode()
    return decrypted_text


key = Fernet.generate_key()

print("Generated Key:", key)

   
original_text = "Hello, this is a secret message!"
print("Original Text:", original_text)

# Encrypt the text
encrypted = encrypt_text(original_text, key)
print("Encrypted Text:", encrypted)

# Decrypt the text
decrypted = decrypt_text(encrypted, key)
print("Decrypted Text:", decrypted)