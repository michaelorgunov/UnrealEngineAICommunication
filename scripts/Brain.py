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
brain = Brain(400)

