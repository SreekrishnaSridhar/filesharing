from lib.fileStreamer import FileStreamer

# TODO: obtain from environment variable

if __name__ == '__main__':
    print('Booting fileshare server')

    fileStreamer = FileStreamer()

    fileStreamer.listen('localhost', 10005)

    # TODO: terminate if user presses ctrl-C and shutdown gracefully
    while True:
        # Wait for a connection
        print('Waiting for a connection')
        fileStreamer.accept()

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

