from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from session import keys
def public_key_encryption():
    pu = RSA.import_key(open('public_pem.pem','r').read())
    random_one, random_two, key_session, key_one, key_two = keys();
    cipher = PKCS1_OAEP.new(key=pu_key)
    random_one_string = str(random_one)
    cipher_text_random_one = cipher.encrypt(random_one_string)
    cipher_text_key = cipher.encrypt(key_session)
    return cipher_text_random_one,cipher_text_key
    
