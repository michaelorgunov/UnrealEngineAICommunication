import socket
import unreal

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

def initializeUnreal():
    level_to_load = "C:/Users\Michael/Documents/Unreal Projects/TensorflowRL/Content/Dynamic/Maps/2DTestMap"  # Replace this with your level path
    unreal.EditorLoadingAndSavingUtils.load_map(level_to_load)
    world = unreal.EditorUtilityLibrary.get_editor_world()
    if world:
        actor_iterator = unreal.EditorActorLibrary.get_all_level_actors()
        player_starts = [actor for actor in actor_iterator if actor.get_class().get_name() == "PlayerStart"]
        if player_starts:
            # Your logic to choose a specific PlayerStart and spawn the character
            pass  # Placeholder for your code to proceed
        else:
            unreal.log_warning("No PlayerStart found in the level.")
    else:
        unreal.log_error("Could not retrieve the game world.")
        
        
        
        
        
    # # Get all PlayerStart actors in the level
    # player_starts = unreal.EditorUtilityLibrary.get_all_actor_of_class(unreal.PlayerStart)
    # if player_starts:
    #     # Assuming you want to spawn the character at the first PlayerStart
    #     player_start = player_starts[0]  # Change this logic as per your requirements

    #     # Spawn the player character at the PlayerStart location
    #     player_character_class = unreal.MyPlayerCharacter  # Replace with your character class
    #     player_character = unreal.EditorLevelLibrary.spawn_actor_from_class(player_character_class, player_start.get_actor_location(), player_start.get_actor_rotation())

    #     # Begin the game loop or start gameplay
    #     # Your code here to initiate the game loop or start gameplay



def client_program():
    # client_socket = createConnection()

    # message = input(" -> ")  # take input

    # while message.lower().strip() != 'bye':
    #     sendMessage(message, client_socket) # send message
        
    #     data = receiveMessage(client_socket) # receive response

    #     print('Received from server: ' + data)  # show in terminal

    #     message = input(" -> ")  # again take input
    
    # closeConnection(client_socket) # close the connection

    initializeUnreal()

if __name__ == '__main__':
    client_program()