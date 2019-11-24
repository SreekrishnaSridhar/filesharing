import hashlib
import random
## Returns random number r1, k(session key), k1(encryption), k2(integrity)
def keys():
    r1 = random.randint(100000,1000000)
    r2 = random.randint(100000,1000000)
    r2 = str(r2)
    k = hashlib.sha256(r2.encode()).hexdigest()
    tempk = "0x"+k
    k1 = int(tempk,16)+0x1
    k2 = int(tempk,16)+0x2
    k1  = hex(k1)
    k2 = hex(k2)
    k1 = k1.lstrip("0x")
    k2 = k2.lstrip("0x")
    return r1,k,k1,k2
    
