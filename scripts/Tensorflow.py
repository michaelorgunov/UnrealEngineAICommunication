#
def extractData(filename):
    ABSOLUTE = "../Content/Files/"
    filePath = ABSOLUTE + filename
    file = open(filePath, 'r')
    distance, xpos, zpos, xvel, zvel, xacc, zacc = file.read().split()
    return (distance, xpos, zpos, xvel, zvel, xacc, zacc)
    

def interface():
    data = extractData("dataLength1.txt")
    print(data)

if __name__ == '__main__':
    interface()