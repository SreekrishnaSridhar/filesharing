import hashlib

## Integrity check, use K2
def integrity(plain,K2):
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
