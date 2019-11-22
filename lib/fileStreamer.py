import sys
import socket
import os

FILE_DIR = os.getenv('FILE_DIR') or ''


class FileStreamer():
    def __init__(self):
        # Create a TCP/IP connection
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        

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

    def sendMessage(self, message):
        self.conn.send(message.encode('utf-8'))        

    def sendFile(self, fileName):
        # TODO: Read file and chunk to byte limit size
        filePath = FILE_DIR + fileName

        with open(filePath, 'rb') as fileObj:
            for line in fileObj:
                print(line)

        # TODO: Send file chunk by chunk
        pass

    def recvFile(self):
        # TODO: receive file until end character

        pass
    def close(self, conn):
        conn.close()
