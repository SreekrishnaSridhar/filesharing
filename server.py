from lib.fileStreamer import FileStreamer

# TODO: obtain from environment variable

if __name__ == '__main__':
    print('Booting fileshare server')

    fileStreamer = FileStreamer()

    fileStreamer.listen('localhost', 10000)

    # TODO: terminate if user presses ctrl-C and shutdown gracefully
    while True:
        # Wait for a connection
        print('Waiting for a connection')
        connection, client_address = fileStreamer.conn.accept()

        print('Received connection from client', connection, client_address)

        command = None
        while command != 'exit':            
            clientCommand = connection.recv(4096).decode('utf-8')

            print('Command from client', clientCommand)

            args = clientCommand.split(' ')

            command = args[0]

            fileName = None
            if len(args) == 2:
                fileName = args[1]
            
            # TODO: parse and process command
            if command == 'download':
                fileStreamer.sendFile(fileName)
            elif command == 'upload':
                fileStreamer.recvFile()
            else:
                print('Invalid client request')

