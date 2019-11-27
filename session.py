import hashlib
import random
## Returns random number random_one, k(session key), key_one(encryption), key_two(integrity)
def keys():
    random_one = random.randint(100000, 1000000)
    random_two = random.randint(100000, 1000000)
    random_two = str(random_two)
    key = hashlib.sha256(random_two.encode()).hexdigest()
    tempk = "0x"+key
    key_one = int(tempk, 16)+0x1
    key_two = int(tempk, 16)+0x2
    key_one = hex(key_one)
    key_two = hex(key_two)
    key_one = key_one.lstrip("0x")
    key_two = key_two.lstrip("0x")
    return random_one, key, key_one, key_two
