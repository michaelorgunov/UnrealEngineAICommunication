import numpy as np
import random
from Direction import Direction

class Brain:
    def __init__(self, size):
        self.step = 0
        self.directions = np.empty(size, dtype=object)
        self.randomize()   
        
    def randomize(self):
        for i in range(self.directions.size):
            self.directions[i] = random.choice(list(Direction))
    
    def clone(self):
        clone = np.copy(self.directions)            
        return clone
    
    def mutate(self):
        mutationRate = 0.01
        for i in range(self.directions.size):
            random = random.random(0,1)
            if (random < mutationRate):
                self.directions[i] = random.choice(list(Direction))