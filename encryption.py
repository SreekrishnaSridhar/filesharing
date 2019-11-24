import session
from session import keys
import hashlib

r1,k,k1,k2 = keys()

def filechunking(file):
    f = open(file,"r")
    text = f.read()
    f.close()
    chunk = 64
    data = [text[i:i+chunk] for i in range(0,len(text),chunk)]
    return data
    
def encryption(data):
    ##Using k1 for encryption
    iv = "This is the initialization vector"
    iv = hashlib.sha256(iv.encode()).hexdigest()
    cipher = []
    ##initial
    ivk1 = k1+iv
    initialhash = hashlib.sha256(ivk1.encode()).hexdigest()
    temp = ''.join(chr(ord(a)^ord(b)) for a,b in zip(initialhash,data[0]))
    cipher.append(temp)
    for i in range(1,len(data)):
        temp = ''
        cipherconcat = k1+cipher[i-1]
        hash = hashlib.sha256(cipherconcat.encode()).hexdigest()
        temp = ''.join(chr(ord(a)^ord(b)) for a,b in zip(hash,data[i]))
        cipher.append(temp)
    return cipher
    
    
    
def decryption(cipher):
    iv = "This is the initialization vector"
    iv = hashlib.sha256(iv.encode()).hexdigest()
    plain = []
    ivk1 = k1+iv
    initialhash = hashlib.sha256(ivk1.encode()).hexdigest()
    temp = ''.join(chr(ord(a)^ord(b)) for a,b in zip(initialhash,cipher[0]))
    plain.append(temp)
    for i in range(1,len(cipher)):
        temp = ''
        cipherconcat = k1+cipher[i-1]
        hash = hashlib.sha256(cipherconcat.encode()).hexdigest()
        temp = ''.join(chr(ord(a)^ord(b)) for a,b in zip(hash,cipher[i]))
        plain.append(temp)
    return plain
    
## Integrity check, use k2

def integrity(plain):
    iv = "This is the initialization vector"
    iv = hashlib.sha256(iv.encode()).hexdigest()
    finalhash = []
    ##initial
    ivk2 = k2+iv
    initialhash = hashlib.sha256(ivk2.encode()).hexdigest()
    temp = ''.join(chr(ord(a)^ord(b)) for a,b in zip(initialhash,plain[0]))
    finalhash.append(temp)
    for i in range(1,len(plain)):
        temp = ''
        cipherconcat = k2+finalhash[i-1]
        hash = hashlib.sha256(cipherconcat.encode()).hexdigest()
        temp = ''.join(chr(ord(a)^ord(b)) for a,b in zip(hash,plain[i]))
        finalhash.append(temp)
    return finalhash

    

        

        
    
    
