import socket

def createConnection():
    print("Host Name: " + str(socket.gethostname()))
    host = '127.0.0.1' #socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    conn = socket.socket()  # instantiate
    conn.connect((host, port))  # connect to the server
    return conn

def sendMessage(MESSAGE, s):
    s.send(MESSAGE.encode()) 
    #s.close()

def receiveMessage(s):
    BUFFER_SIZE = 1024
    data = s.recv(BUFFER_SIZE).decode()
    print(u"client received data:", data)
    return data

def closeConnection(s):
    s.close()


def client_program():
    client_socket = createConnection()

    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        sendMessage(message, client_socket) # send message
        
        data = receiveMessage(client_socket) # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input
    
    closeConnection(client_socket) # close the connection


if __name__ == '__main__':
    client_program()