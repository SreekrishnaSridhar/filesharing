import sys
import socket
import os

import lib.crypto as crypto

FILE_DIR = os.getenv('FILE_DIR') or ''
CHUNK_SIZE = 32
IV = b'initialization vector'

class FileStreamer():
    encryptKey = None
    sessionKey = None

    def __init__(self):
        # Create a TCP/IP connection
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.buffer = b''
    
    def establishKeys(self, k1, k2):
        self.encryptKey = k1.encode('utf-8')
        self.sessionKey = k2.encode('utf-8')

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
        filePath = FILE_DIR + fileName

        # Send file as encrypted chunks
        with open(filePath, 'rb') as fileObj:
            chunk = '-'
            prevChunk = IV
            while chunk[-3:] != b'EOF':
                chunk = fileObj.read(CHUNK_SIZE)

                if len(chunk) < CHUNK_SIZE:
                    chunk += b'EOF'

                encryptedChunk = crypto.hashXOR(chunk, self.encryptKey, prevChunk)

                prevChunk = encryptedChunk
                
                print(chunk, len(chunk))
                print('Send length', len(encryptedChunk))
                print(encryptedChunk)

                self.conn.send(encryptedChunk)

    def recvFile(self, fileName):
        # TODO: receive file until end character
        filePath = FILE_DIR + fileName

        with open(filePath, 'wb') as fileObj:
            chunk = '-' # Stop reading from buffer when line is empty
            prevChunk = IV
            while chunk:
                encryptedChunk = self.conn.recv(CHUNK_SIZE)

                chunk = crypto.hashXOR(encryptedChunk, self.encryptKey, prevChunk)

                print(chunk)

                prevChunk = encryptedChunk

                if chunk[-3:] == b'EOF':
                    chunk = chunk[:-3]

                    fileObj.write(chunk)

                    break

                fileObj.write(chunk)
        
    def close(self, conn):
        conn.close()
