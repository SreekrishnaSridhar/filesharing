from Crypto.PublicKey import RSA
private_key = RSA.generate(2048)
public_key = private_key.publickey()
private_pem = private_key.export_key().decode()
public_pem = public_key.export_key().decode()
with open('private_pem.pem','w') as pr:
    pr.write(private_pem)
with open('public_pem.pem','w') as pu:
    pu.write(public_pem)
