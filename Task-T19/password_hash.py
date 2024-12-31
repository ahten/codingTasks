import hashlib
import bcrypt 



def string_hasher(input_string):

    salt = bcrypt.gensalt()
    encrypted_string = bcrypt.hashpw(input_string.encode(), salt)
    
    print (encrypted_string)
    hashed_string = hashlib.sha256 (encrypted_string.encode()).hexdigest()

    return hashed_string

hashed1 = string_hasher ("This is sensitive text")
hashed2 = string_hasher ("_password-123_")

print (f"\'_passowrd-123\' \t-->Hash Function-->\t {hashed1} , {hashed2}")