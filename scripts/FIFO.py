import time
from Pawn import Pawn
from Direction import Direction

#
def extractData(filename):
    ABSOLUTE = "../Content/Files/"
    filePath = ABSOLUTE + filename
    file = open(filePath, 'r')
    distance, xpos, zpos, xvel, zvel, xacc, zacc = file.read().split()
    return (distance, xpos, zpos, xvel, zvel, xacc, zacc)
    
def writeData(filename, message):
    ABSOLUTE = "../Content/Files/"
    filePath = ABSOLUTE + filename
    with open(filePath, 'w') as file:
        file.write(message)
        
    
def interface():
    pawn = Pawn()
    while True:
        try:
            data = extractData("dataOut.txt")
        except:
            data = extractData("dataOut.txt")
            
        distance, xpos, zpos, xvel, zvel, xacc, zacc = data
        pawn.update(distance, xpos, zpos, xvel, zvel, xacc, zacc)
        move = pawn.move()
        # print(move.value)
        writeData("dataInput.txt", move.value)
        time.sleep(.3)

if __name__ == '__main__':
    interface()