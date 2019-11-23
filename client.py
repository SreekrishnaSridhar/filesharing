from lib.fileStreamer import FileStreamer

if __name__ == '__main__':
    fileStreamer = FileStreamer()

    fileStreamer.connect('localhost', 10005)

    print(fileStreamer.conn)
    # TODO: authenticate server

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
        
        
