import hashlib
from session import keys

R1, k, K1, K2 = keys()

def filechunking(file):
    file = open(file, "r")
    text = file.read()
    file.close()
    chunk = 64
    data = [text[i:i+chunk] for i in range(0, len(text), chunk)]
    return data
def encryption(data):
    ##Using K1 for encryption
    initialvector = "This is the initialization vector"
    initialvector = hashlib.sha256(initialvector.encode()).hexdigest()
    cipher = []
    ##initial
    initial_vectorone = K1+initialvector
    initialhash = hashlib.sha256(initial_vectorone.encode()).hexdigest()
    temp = ''.join(chr(ord(a)^ord(b)) for a, b in zip(initialhash, data[0]))
    cipher.append(temp)
    for i in range(1, len(data)):
        temp = ''
        cipherconcat = K1+cipher[i-1]
        hash_temp = hashlib.sha256(cipherconcat.encode()).hexdigest()
        temp = ''.join(chr(ord(a)^ord(b)) for a, b in zip(hash_temp, data[i]))
        cipher.append(temp)
    return cipher
def decryption(cipher):
    initialvector = "This is the initialization vector"
    initialvector = hashlib.sha256(initialvector.encode()).hexdigest()
    plain = []
    initial_vectorone = K1+initialvector
    initialhash = hashlib.sha256(initial_vectorone.encode()).hexdigest()
    temp = ''.join(chr(ord(a)^ord(b)) for a, b in zip(initialhash, cipher[0]))
    plain.append(temp)
    for i in range(1, len(cipher)):
        temp = ''
        cipherconcat = K1+cipher[i-1]
        hash_temp = hashlib.sha256(cipherconcat.encode()).hexdigest()
        temp = ''.join(chr(ord(a)^ord(b)) for a, b in zip(hash_temp, cipher[i]))
        plain.append(temp)
    return plain
## Integrity check, use K2
def integrity(plain):
    initialvector = "This is the initialization vector"
    initialvector = hashlib.sha256(initialvector.encode()).hexdigest()
    finalhash = []
    ##initial
    initial_vectortwo = K2+initialvector
    initialhash = hashlib.sha256(initial_vectortwo.encode()).hexdigest()
    temp = ''.join(chr(ord(a)^ord(b)) for a, b in zip(initialhash, plain[0]))
    finalhash.append(temp)
    for i in range(1, len(plain)):
        temp = ''
        cipherconcat = K2+finalhash[i-1]
        hash_temp = hashlib.sha256(cipherconcat.encode()).hexdigest()
        temp = ''.join(chr(ord(a)^ord(b)) for a, b in zip(hash_temp, plain[i]))
        finalhash.append(temp)
    return finalhash
