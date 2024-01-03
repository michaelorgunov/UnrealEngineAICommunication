# Attempts to efficiently bring AI model generation to Unreal Engine 5

## File manipulation Method:
- One can establish two way communication with UE5 through UE writing to a file and the Python script writing to a different file.
- Ideally, a mutex/lock would be implemented for this shared memory, but it has not been an issue for me so far (may be an issue when running an entire model).
### Unreal Engine:
- Create a C++ class (mine is called ```FileInteract```) that creates functions to write and read from files.
- In your desired character blueprint, collect the desired data for your model and write it to a file using String Array to File native function.

https://github.com/michaelorgunov/TensorflowRL/assets/98727592/65607975-d11a-4f35-a2f4-79c330344af1

### Python "server":
- Create your model and every time it iterates, read data from the UE file and write the desired character input into the other file that UE is reading data from.

https://github.com/michaelorgunov/TensorflowRL/assets/98727592/62aa0ed0-f16a-4339-833c-b2ff754fb694

### Overall, this method is fairly inefficient since it relies on write to perform character actions and challenging to scale since there will be two files for each character that is created. The more characters, the more delay and issues will arise.

## TCP Sockets:
- In progress. Idea is to create a server and then a UE c++ socket with functions to interact with blueprints. 
