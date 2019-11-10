import socket
import sys

def connect(ip, port):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = (ip, port)
    print('connecting to server', ip, port)

    sock.connect(server_address)

    sock.close()

if __name__ == '__main__':
    connect('localhost', 10000)

    # TODO: authenticate server

    # TODO: exit on command or Ctrl-C
    while True:
        # TODO: take and parse user input
        userInput = input('command: ').split(' ')

        # TODO: send and handle command to server accordingly
        command = userInput[0]

        if len(userInput) == 2:
            fileName = userInput[1]

        if command == 'download':
            pass
        elif command == 'upload':
            pass
        else:
            # TODO: incorrect command display help
            print('Incorrect command')
        
        
