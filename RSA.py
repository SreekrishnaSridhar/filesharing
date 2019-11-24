from Crypto.PublicKey import RSA
private_key = RSA.generate(1024)

def publickey():
    public_key = private_key.publickey()
    private_pem = private_key.export_key().decode()
    public_pem = public_key.export_key().decode()
    with open('public_pem.pem','w') as pu:
        pu.write(public_pem)
