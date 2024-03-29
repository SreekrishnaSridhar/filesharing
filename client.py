from Crypto.PublicKey import RSA

from lib.fileStreamer import FileStreamer
import lib.crypto as crypto

if __name__ == '__main__':
    fileStreamer = FileStreamer()

    fileStreamer.connect('localhost', 10000)

    print(fileStreamer.conn)

    # TODO: authenticate server
    r1, encryptKey, integrityKey = crypto.generateKeys()

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

            fileHash = fileStreamer.recvFile(fileName)

            print('File download complete')

            fileStreamer.sendMessage('Ack')

            receivedHash = fileStreamer.conn.recv(4096)

            if fileHash == receivedHash:
                print('File integrity verification successful', fileHash)
            else:
                print('Integrity verification failed. Expected {0}, Received {1}'.format(fileHash, receivedHash))
        elif command == 'upload':
            
            fileStreamer.sendMessage(userInput)

            confirm = fileStreamer.recvMessage()

            fileHash = fileStreamer.sendFile(fileName)

            print('File upload complete')

            confirm = fileStreamer.recvMessage()

            fileStreamer.conn.send(fileHash)
        else:
            # TODO: incorrect command display help
            print('Incorrect command')
        
        
