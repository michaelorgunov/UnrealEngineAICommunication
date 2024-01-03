import numpy as np
import random
from Direction import Direction

class Brain:
    def __init__(self, size):
        self.step = 0
        self.directions = np.empty(size, dtype=object)
        self.randomize()   
        
    def randomize(self):
        types = []
        for direction in Direction:
            if direction != Direction.RESET:
                types.append(direction)
        for i in range(self.directions.size):
            self.directions[i] = random.choice(types)
    
    def clone(self):
        clone = np.copy(self.directions)            
        return clone
    
    def mutate(self):
        mutationRate = 0.01
        types = []
        for direction in Direction:
            if direction != Direction.RESET:
                types.append(direction)
                
        for i in range(self.directions.size):
            randomVal = random.uniform(0,1)
            if (randomVal < mutationRate):
                self.directions[i] = random.choice(types)