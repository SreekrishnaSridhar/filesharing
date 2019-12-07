from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def server(cipher_text_random_one,cipher_text_key):
    pr_key = RSA.import_key(open('private_pem.pem', 'r').read())
    decrypt = PKCS1_OAEP.new(key=pr_key)
    random_one_string = decrypt.decrypt(cipher_text_random_one)
    key_string = decrypt.decrypt(cipher_text_key)
    random_one = int(random_one_string)
    tempk = "0x"+key_string
    key_one = int(tempk,16)+0x1
    key_two = int(tempk,16)+0x2
    key_one = hex(key_one)
    key_two = hex(key_two)
    key_one = key_one.lstrip("0x")
    key_two = key_two.lstrip("0x")
    return random_one,key_one,key_two
    
    
