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
    # print(u"client sent data:", MESSAGE)
    # print("socket send: " + str(s.getpeername()) + " DATA: " + MESSAGE)
    s.send(MESSAGE.encode()) 
    # if MESSAGE == "RESET":
    #     print("SENDING RESET to " + str(s))
    

def receiveMessage(s):
    BUFFER_SIZE = 1024
    data = s.recv(BUFFER_SIZE).decode()
    # print("client received data: " + str(data) + " PORT: " + str(s.getpeername()[1]))
    return data

def closeConnection(s):
    s.close()

def handle_client(client, pawn):
    while True:
        # print("client ->" + str(client.getpeername()[1]))
        try: 
            data = receiveMessage(client)
            if data:
                # if len(data.split(",")) > 7:
                if data[-1:] == ',':
                    data = data[:-1]
                if data[0] == ",":
                    data = data[1:]
                distance, xpos, zpos, xvel, zvel, xacc, zacc = data.split(',')[:7]
                pawn.update(distance, xpos, zpos, xvel, zvel, xacc, zacc)
                # print("ENTERING SEND: " + str(pawn.nextMove))
                
                if pawn.dead:
                    # print("PAWN DEAD. Distance: " + str(distance))
                    sendMessage(Direction.NONE.value, client)
                    receiveMessage(client)
                    break
                sendMessage(pawn.nextMove.value, client)
        except Exception as e:
            print("Error occurred:" + str(e) + " data: " + str(data))
            break
        
def server_program():
    # pawnCount is number of characters that must connect 
    pawnCount = 60
    counter = 0
    GENERATION_COUNT = 45
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
        # print(pawnIndexToSocket)       
         
        if len(pawnIndexToSocket) == pawnCount:
            print("Established enough connections to begin... ")
            break
    
    threadList = []
    for i in range(1, len(pawnIndexToSocket)+1):
        clientThread = threading.Thread(target=handle_client, args=(pawnIndexToSocket[i], population.retrievePawnAtIndex(i-1)))
        # print("INDEX: " + str(i) + ":" + str(pawnIndexToSocket[i].getpeername()[1]))
        clientThread.start()
        threadList.append(clientThread)
            
    while True:
        # Join all threads before continuing
        for thread in threadList:
            thread.join()
            threadList.remove(thread)
            # print("JOINED THREAD: " + str(len(threadList)))
            
            
        if (len(threadList) == 0):
            # cutoff if generation completed
            if (population.generation >= GENERATION_COUNT):
                print("REACHED TARGET GENERATION. BEST PAWN STEPS: " + str(population.pawns[population.bestPawn].brain.step) + " REACHED GOAL: " + str(population.pawns[population.bestPawn].reachedGoal) + " FITNESS: " + str(population.pawns[population.bestPawn].fitness))
                break

            # If all dead, reset position and perform algorithm
            if (population.allDead()):
                for i in range(1, len(pawnIndexToSocket)+1):
                    # print("RESETTING POSITION: " + str(pawnIndexToSocket[i].getpeername()[1]))
                    sendMessage(Direction.RESET.value, pawnIndexToSocket[i])
                    # sendMessage("," + str(Direction.RESET.value), pawnIndexToSocket[i])

                print("ALL ARE DEAD")                
                time.sleep(1)
                population.calculateFitness()
                population.naturalSelection()
                population.realive()
                
                for pawns in population.pawns:
                    if pawns.brain.step != 0:
                        print("PAWN NOT RESET: " + str(pawns.brain.step))
                # print("RESURRECTED ALL PAWNS")
                # for pawn in population.pawns:
                #     print("PAWN STEP: " + str(pawn.brain.step))
                
                # Create new generation
                for i in range(1, len(pawnIndexToSocket)+1):
                    clientThread = threading.Thread(target=handle_client, args=(pawnIndexToSocket[i], population.retrievePawnAtIndex(i-1)))
                    # print("INDEX: " + str(i) + ":" + str(pawnIndexToSocket[i].getpeername()[1]))
                    clientThread.start()
                    threadList.append(clientThread)
            # else:
            #     print("NOT ALL DEAD: ")
            #     for pawn in population.pawns:
            #         if pawn.dead == False:
            #             print("PAWN NOT DEAD: " + str(pawn))
                
    #TODO:  CLOSE ALL CONNECTIONS
    closeConnection(server)  # close the connection


if __name__ == '__main__':
    server_program()