import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def initialize():
    # Bind the socket to the port
    server_address = ('localhost', 10000)
    print('Starting up on', server_address)

    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)

    # TODO: terminate if user presses ctrl-C and shutdown gracefully
    while True:
        # Wait for a connection
        print('Waiting for a connection')
        connection, client_address = sock.accept()

        print('Received connection from client', connection, client_address)


if __name__ == '__main__':
    print('Booting fileshare server')

    initialize()