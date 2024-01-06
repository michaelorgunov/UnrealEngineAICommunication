# Proof of concepts to efficiently bring AI models to Unreal Engine 5

## The AI Model:
- Heavily inspired by Code Bullet's Genetic Algorithm, the algorithm determines character fitness based on distance to the "gem" as well as the time it took to get to the "gem" if it was reached.

https://youtu.be/BOZfhUcNiqk?si=y3Z8dgIwf48W7BMg

## The environment:
- I created a simple 2D game that the AI can control. The game's primary focus is to create a simple environment in which I can experiment with data communication as well as AI algorithms.
- Using the freely available SunnyLand game art, I created the character and map.

https://ansimuz.itch.io/sunny-land-pixel-game-art

## File manipulation Method:
- One can establish two way communication with UE5 through UE writing to a file and the Python script writing to a different file.
- Ideally, a mutex/lock would be implemented for this shared memory, but it has not been an issue for me so far (may be an issue when running an entire model).
- Overall, this method is fairly inefficient since it relies on write to perform character actions and challenging to scale since there will be two files for each character that is created. The more characters, the more delay and issues will arise. Due to this, I did not continue with this since I got my desired outcome of being able to control the character.
### Unreal Engine:
- Create a C++ class (mine is called ```FileInteract```) that creates functions to write and read from files.
- In your desired character blueprint, collect the desired data for your model and write it to a file using String Array to File native function.

https://github.com/michaelorgunov/TensorflowRL/assets/98727592/65607975-d11a-4f35-a2f4-79c330344af1

### Python "server":
- Create your model and every time it iterates, read data from the UE file and write the desired character input into the other file that UE is reading data from.

https://github.com/michaelorgunov/TensorflowRL/assets/98727592/62aa0ed0-f16a-4339-833c-b2ff754fb694

## TCP Sockets:
- Using raw TCP, we can establish a two way communication between UE5 and an external Python server. While there are many tools built into UE5 for networking, I wanted to create my own. There were many challenges encountered with this approach, primarily dealing with undocumented UE source code, UE blueprints not waiting on the receive function before sending, and data processing.
### Unreal Engine:
- Created C++ class with initialize, receive, send, and data conversion functions to be used within each character. The ```NetworkHelper``` class that I created is then initialized ```OnPlay``` in the character blueprint. The remaining logic is connected to that, and is not dependent on tick. The refresh rate of character movement can thus be manually set in the blueprint. In this example, the genetic algorithm is updating in UE every 0.2 seconds. From experimentation, this was the most effective time period for this algorithm.

https://github.com/michaelorgunov/UnrealEngineAICommunication/assets/98727592/6b4473a2-a50d-486f-9976-f43fd493f284

### Python server:
- Handles incoming requests and with each accepted request, it creates a new thread. With a unique socket for each character, the threads can receive character data and send back movement commands as well as position reset codes.
![image](https://github.com/michaelorgunov/UnrealEngineAICommunication/assets/98727592/34ad91e2-08f2-4731-8188-26e0de3a844c)

## Conclusion:
- This project has been personally rewarding and insightful. I learned a lot about Unreal Engine 5 game development, UE Blueprints, UE C++ development, the genetic algorithm, as well as TCP communication. The most rewarding part was that this project combined skills that I learned in courses at Texas A&M as well as personal experiments with Tensorflow. This felt like an application of the building blocks that I have been gathering.
- In the future, I hope to expand this project to Tensorflow, using my TCP communication network as a base for future projects. The interface between Unreal Engine and external software that I developed will accelerate future works.
