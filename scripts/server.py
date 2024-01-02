import socket
import threading
import time
from Pawn import Pawn
from Direction import Direction
from Population import Population

def createConnection():
    # get the hostname
    print("Host Name: " + str(socket.gethostname()))

    host = '127.0.0.1'#socket.gethostname()
    port = 8085  

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together
    server_socket.listen()

    return server_socket

def sendMessage(MESSAGE, s):
    print(u"client sent data:", MESSAGE)
    print("socket send: " + str(s.getpeername()))
    s.send(MESSAGE.encode()) 
    

def receiveMessage(s):
    BUFFER_SIZE = 1024
    data = s.recv(BUFFER_SIZE).decode()
    print("client received data:" + str(data) + " PORT: " + str(s.getpeername()))
    return data

def closeConnection(s):
    s.close()



def handle_client(client, pawn):
    client.settimeout(1)  # Set a timeout for socket operations
    while True:
        if pawn.dead:
            print("PAWN DEAD")
            break
        # print("client ->" + str(client.getpeername()[1]))

        try:
            
            data = receiveMessage(client)
            if data:
                distance, xpos, zpos, xvel, zvel, xacc, zacc = data.split(',')
                pawn.update(distance, xpos, zpos, xvel, zvel, xacc, zacc)
                sendMessage(pawn.nextMove.value, client)
        except socket.timeout:
            # Handle timeout (no data received within the timeout period)
            print("TIMEOUT: " + str(client.getpeername()[1]))
            pass
        except Exception as e:
            print("Error occurred:", e)
            break
        
def server_program():
    # pawnCount is number of characters that must connect 
    pawnCount = 80
    counter = 0
    
    population = Population(pawnCount)
    pawnIndexToSocket = {} # Dictionary containing a created index and an identifier for transfers
    
    server = createConnection()
    
    
    while True:
        # listen(#) is the # of non-accepted connected are allowed
        print('Server is listening...')

        counter += 1
        client, address = server.accept()  # accept new connection
        pawnIndexToSocket[counter] = client # add connection to list

        print("Connection from: " + str(address) + " " + str(counter) + "/" + str(pawnCount))
        print(pawnIndexToSocket)       
         
        if len(pawnIndexToSocket) == pawnCount:
            print("Established enough connections to begin... ")
            break
        
    for i in range(1, len(pawnIndexToSocket)+1):
        clientThread = threading.Thread(target=handle_client, args=(pawnIndexToSocket[i], population.retrievePawnAtIndex(i-1)))
        print("INDEX: " + str(i) + ":" + str(pawnIndexToSocket[i].getpeername()[1]))
        clientThread.start()
        # data = receiveMessage(client)
        # if not data:
        #     # if data is not received break
        #     break
        
        # distance, xpos, zpos, xvel, zvel, xacc, zacc = data.split(",")

        # if (population.allDead()):
        #     population.calculateFitness()
        #     population.naturalSelection()
        #     population.mutate()
        #     if (population.generation < 2):
        #         population.update(distance, xpos, zpos, xvel, zvel, xacc, zacc)
        # else:
        #     population.update(distance, xpos, zpos, xvel, zvel, xacc, zacc)
            
        # move = population.pawns[0].move()
        
        # sendMessage(move.value, client) # send data to the client

    #TODO:  CLOSE ALL CONNECTIONS
    #closeConnection(server)  # close the connection


if __name__ == '__main__':
    server_program()