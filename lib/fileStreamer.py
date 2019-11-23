import sys
import socket
import os

FILE_DIR = os.getenv('FILE_DIR') or ''


class FileStreamer():
    def __init__(self):
        # Create a TCP/IP connection
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.buffer = b''

    def listen(self, ip, port):
        # Bind the socket to the port        
        print('Starting server up on', ip, port)

        self.conn.bind((ip, port))

        # Listen for incoming connections
        self.conn.listen(1)
        
    def connect(self, ip, port):
        # Connect the socket to the port where the server is listening
        print('connecting to server', ip, port)
        self.conn.connect((ip, port))

    def accept(self):
        self.conn, address = self.conn.accept()
        print('Received connection from client', address)

    def sendMessage(self, message):
        self.conn.send(message.encode('utf-8'))             

    def recvMessage(self):
        return self.conn.recv(4096).decode('utf-8')

    def sendFile(self, fileName):
        # TODO: Read file and chunk to byte limit size
        filePath = FILE_DIR + fileName

        # TODO: Send file chunk by chunk
        with open(filePath, 'rb') as fileObj:
            for line in fileObj:
                self.conn.send(line)
        
        self.conn.send('EOF'.encode('utf-8'))

    def recvFile(self, fileName):
        # TODO: receive file until end character
        filePath = FILE_DIR + fileName

        with open(filePath, 'wb') as fileObj:
            line = '-' # Stop reading from buffer when line is empty
            while line:
                line = self.conn.recv(4096)
                if line[-3:] == b'EOF':
                    line = line[:-3]
                    fileObj.write(line)
                    break
                fileObj.write(line)
        
    def close(self, conn):
        conn.close()
