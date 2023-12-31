import socket
import time
from Pawn import Pawn
from Direction import Direction

def createConnection():
    # get the hostname
    print("Host Name: " + str(socket.gethostname()))

    host = '127.0.0.1'#socket.gethostname()
    port = 8085  

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    return conn

def sendMessage(MESSAGE, s):
    s.send(MESSAGE.encode()) 

def receiveMessage(s):
    BUFFER_SIZE = 1024
    data = s.recv(BUFFER_SIZE).decode()
    print(u"client received data:", data)
    return data

def closeConnection(s):
    s.close()

def server_program():
    pawn = Pawn()

    conn = createConnection()
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = receiveMessage(conn)
        if not data:
            # if data is not received break
            break
        print(data)
        distance, xpos, zpos, xvel, zvel, xacc, zacc = data.split(",")
        pawn.update(distance, xpos, zpos, xvel, zvel, xacc, zacc)
        move = pawn.move()
        
        sendMessage(move.value, conn) # send data to the client

    closeConnection(conn)  # close the connection


if __name__ == '__main__':
    server_program()