import socket
import sys

def connect(ip, port):
    # Create a TCP/IP connection
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = (ip, port)
    print('connecting to server', ip, port)

    conn.connect(server_address)

    return conn

def close(conn):
    conn.close()

if __name__ == '__main__':
    conn = connect('localhost', 10000)

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
            conn.send(userInput.encode('utf-8'))
        elif command == 'upload':
            conn.send(userInput.encode('utf-8'))
        else:
            # TODO: incorrect command display help
            print('Incorrect command')
        
        
