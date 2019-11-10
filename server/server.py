import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def initialize(ip, port):
    # Bind the socket to the port
    server_address = (ip, port)
    print('Starting up on', server_address)

    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)

    # TODO: terminate if user presses ctrl-C and shutdown gracefully
    while True:
        # Wait for a connection
        print('Waiting for a connection')
        connection, client_address = sock.accept()

        command = ''
        while command != 'exit':
            print('Received connection from client', connection, client_address)
            command = connection.recv(4096).decode('utf-8')

            print('Command from client', command)
            # TODO: parse and process command

if __name__ == '__main__':
    print('Booting fileshare server')

    initialize('localhost', 10000)