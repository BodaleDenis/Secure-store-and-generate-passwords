from queue import Empty
import sys
sys.path.append("./")
from src.constexpr import *
from cryptography.fernet import Fernet
import random
import os
# Methods used in the backend process 
def password_generator():
    """
    Generate password by randomly combine uper/lowercase letters,
    special chars, numbers
    Returns:
        [string]: An 10 chars length string, which is the generated 
        password
    """
    generated_password = ''
    password_chars = [VOWELS, CONSONATES, SPECIAL_CHAR, NUMBERS]
    while len(generated_password) < 10 :
        random_list = random.choice(password_chars)
        element_from_list = random.choice(random_list)
        generated_password += element_from_list
    return generated_password

def store_login_data(website, password):
    """
    The logic behind Store button, it stores data in My Data file
    containing the required info

    Args:
        website (string): Website in which you use your password to be stored
        password (string): Password to be stored

    Returns:
        [string]: Returns {website} : {password} inside the file My Data
    """
    my_data_file = open('My Data', 'a+')
    append_content = website + " : " + password + '\n'
    my_data_file.write(append_content)
    return append_content

def file_encrypt(file_to_encrypt):
    """
    Encrypt using cryptography library the text inside the My Data
    And generate the key, the key must be kept away

    Args:
        file_to_encrypt (string): Path to the file

    Returns:
        [bool]: In case key already exists doesn't encrypt, else it encrypts {file_to_encrypt}
    """
    generated_key = Fernet.generate_key()
    if(os.path.exists(KEY_FILE)):
        print("Key already exists")
        return False
    else:
        with open(KEY_FILE, 'wb') as key_file:
            key_file.write(generated_key)
        with open(KEY_FILE, 'rb') as key_file:
            encryption_key = key_file.read()
        fernet_encrypter = Fernet(generated_key)
        with open(file_to_encrypt, 'rb') as file:
            orig_file_bytes = file.read()
        encrypted_text = fernet_encrypter.encrypt(orig_file_bytes)
        with open(file_to_encrypt, 'wb') as encrypted_file:
            encrypted_file.write(encrypted_text)

def file_decrypt(file_to_decrypt, key):
    """
    Decrypt file, using the key generated by encryption method
    The key file if existing will be removed

    Args:
        file_to_decrypt (string): Path to the file whom needs decryption
        key (string): Key used for decription and key who was used for encryption

    Returns:
        [bool]: False if key is null, otherwise if key math will decrypt
    """
    print("Key=",key)
    if key is None:
        print("Key value null")
        return False
    fernet_decrypter = Fernet(key)
    with open(file_to_decrypt, 'rb') as file:
        encrypted_bytes = file.read()
        print('encrypted_bytes=', encrypted_bytes)
    decrypted_bytes = fernet_decrypter.decrypt(encrypted_bytes)
    print('decrypted_bytes', decrypted_bytes)
    with open(file_to_decrypt, 'wb') as file:
        decrypted_file = file.write(decrypted_bytes)
    os.remove(KEY_FILE)