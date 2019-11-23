import session
from session import keys
import hashlib


def filechunking(file):
    f = open(file,"r")
    text = f.read()
    f.close()
    chunk = 64
    data = [text[i:i+chunk] for i in range(0,len(text),chunk)]
    return data
    
