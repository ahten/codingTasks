Task 1 - Password Hash

Objective: 
+ Learn how to hashing. Use the library bcrypt to hashing.

Dependencies:
+ py-bycrpty (pip3 install py-bcrypt)

Task Details:

+ 1. Follow the instructions in the Additional Reading document to set up your
virtual environment, and then activate it according to the steps provided.
+ 2. Create a file called password_hash.py.
+ 3. Referring to the code example provided earlier as a starting point, use the
bcrypt Python library (hint: import bcrypt) to assist you in defining a
function that hashes a password string provided by the user.
+ 4. Your function should encode the user’s string first before any hashing takes
place.
+ 5. Make use of the bcrypt library to hash the password while generating a
random salt.
+ 6. Add a requirements.txt file for your mentor, containing all of the
dependencies for your program.
+ 7. Deactivate your virtual environment once you have completed the task.

---

Task 2 - Encrypt 

Objective: 
+ Learn how to encrypt the text value

Task Details:

+ 1. Follow the instructions in the Additional Reading document and create a
folder for your virtual environment. Then activate the virtual environment.
+ 2. Do some research on symmetric encryption.
+ 3. Create a file called encrypt.py.
+ 4. By taking advantage of the cryptography Python library, define your
function with two parameters: text (the string of text to be encrypted) and
key (the key used to encrypt the text).
+ + ○ Hint: from cryptography.fernet import Fernet
+ 5. The function above should use the key provided to encrypt the text
provided and then return the encrypted text.
+ 6. Using the same library and logic above, create another function that will
decrypt any encrypted text using the same key that it was encrypted with.
+ 7. Deactivate your virtual environment once you have completed the task and
remember to delete the virtual environment folder (you can always create a
new one).

