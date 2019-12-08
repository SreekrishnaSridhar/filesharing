import hashlib
import random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def priv_decrypt(ciphertext, key):
    cipher = PKCS1_OAEP.new(key=key)
    
    plaintext = cipher.decrypt(ciphertext)

    return plaintext

def pub_encrypt(plaintext, key):
    cipher = PKCS1_OAEP.new(key=key)
    
    ciphertext = cipher.encrypt(str(plaintext).encode('utf-8'))
    
    return ciphertext

## Returns random number random_one, k(session key), key_one(encryption), key_two(integrity)
def generateKeys():
    r1 = random.randint(100000, 1000000)
    r2 = random.randint(100000, 1000000)
    
    key = hashlib.sha256(str(r2).encode()).hexdigest()

    tempk = "0x"+key
    key2 = int(tempk, 16)+0x1

    key2 = hex(key2)

    key2 = key2.lstrip("0x")

    return r1, key, key2

def hashXOR(data, key, Cprev):
    byteStream = hashlib.sha256(key + Cprev).digest()

    outStream = bytes([a^b for a, b in zip(byteStream, data)])

    return outStream