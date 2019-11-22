from lib.fileStreamer import FileStreamer

if __name__ == '__main__':
    fileStreamer = FileStreamer()

    fileStreamer.connect('localhost', 10000)

    # TODO: authenticate server

    # TODO: exit on command or Ctrl-C
    while True:
        # TODO: take and parse user input
        userInput = input('command: ')

        # TODO: send and handle command to server accordingly
        args = userInput.split(' ')
        command = args[0]

        if len(args) == 2:
            fileName = args[1]

        if command == 'download':
            fileStreamer.sendMessage(userInput)

            fileStreamer.recvFile()
        elif command == 'upload':
            fileStreamer.sendMessage(userInput)

            fileStreamer.sendFile(fileName)
        else:
            # TODO: incorrect command display help
            print('Incorrect command')
        
        
