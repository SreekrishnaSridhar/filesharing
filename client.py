from Crypto.PublicKey import RSA

from lib.fileStreamer import FileStreamer
import lib.crypto as crypto

if __name__ == '__main__':
    fileStreamer = FileStreamer()

    fileStreamer.connect('localhost', 10005)

    print(fileStreamer.conn)

    # TODO: authenticate server
    r1, encryptKey, integrityKey = crypto.generateKeys()
    print(r1, encryptKey, integrityKey)

    publicKey = RSA.import_key(open('rsa.pem.pub','r').read())
    
    authPayload = str(r1) + ',' + str(encryptKey) + ',' + str(integrityKey)
    authPayloadEncrypted = crypto.pub_encrypt(authPayload, publicKey)

    fileStreamer.conn.send(authPayloadEncrypted)

    r1Server = fileStreamer.recvMessage()

    if str(r1) != str(r1Server):
        print('Server authentication failed')
        exit(1)
    else:
        print('Server authentication succesful with auth token', r1)
        fileStreamer.establishKeys(encryptKey, integrityKey)
    
    # TODO: exit on command or Ctrl-C
    while True:
        # TODO: take and parse user input
        userInput = input('command: ')

        # TODO: send and handle command to server accordingly
        args = userInput.split(' ')

        command = args[0]

        filename = 'default.txt'

        if len(args) == 2:
            fileName = args[1]

        if command == 'download':
            fileStreamer.sendMessage(userInput)

            fileStreamer.recvFile(fileName)

            print('File download complete')
        elif command == 'upload':
            
            fileStreamer.sendMessage(userInput)

            confirm = fileStreamer.recvMessage()

            fileStreamer.sendFile(fileName)

            print('File upload complete')
        else:
            # TODO: incorrect command display help
            print('Incorrect command')
        
        
