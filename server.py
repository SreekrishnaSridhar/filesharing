from Crypto.PublicKey import RSA

from lib.fileStreamer import FileStreamer
import lib.crypto as crypto

if __name__ == '__main__':
    print('Booting fileshare server')

    fileStreamer = FileStreamer()

    # TODO: obtain from environment variable
    fileStreamer.listen('localhost', 10005)

    # Wait for a connection
    print('Waiting for a connection')
    fileStreamer.accept()

    privKey = RSA.import_key(open('rsa.pem', 'r').read())

    authPayloadEncrypted = fileStreamer.conn.recv(4096)
    
    authPayload = crypto.priv_decrypt(authPayloadEncrypted, privKey)

    r1, encryptKey, integrityKey = authPayload.decode('utf-8').split(',')

    fileStreamer.sendMessage(r1)

    fileStreamer.establishKeys(encryptKey, integrityKey)

    command = None
    while command != 'exit':            
        clientCommand = fileStreamer.recvMessage()

        print('Command from client', clientCommand)

        args = clientCommand.split(' ')

        command = args[0]

        fileName = 'default.txt'
        
        if len(args) == 2:
            fileName = args[1]
        
        # TODO: parse and process command
        if command == 'download':
            fileStreamer.sendFile(fileName)

            print('File download complete')
        elif command == 'upload':
            fileStreamer.sendMessage('Ack')

            fileStreamer.recvFile(fileName)

            print('File upload complete')
        else:
            print('Invalid client request')

