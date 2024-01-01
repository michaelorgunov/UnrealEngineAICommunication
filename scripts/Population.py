import numpy as np
import random
from Brain import Brain
from Direction import Direction
from Pawn import Pawn

class Population:
    def __init__(self, size):
        self.pawns = []
        self.generation = 1
        self.bestPawn = Pawn()
        for i in range(size):
            self.pawns.append(Pawn())
    
    def update(self):
        for pawn in self.pawns:
            pawn.update()
            
    def calculateFitness(self):
        for pawn in self.pawns:
            pawn.calculateFitness()
        
    def calculateFitnessSum(self):
        fitnessSum = 0
        for pawn in self.pawns:
            fitnessSum += pawn.fitness
        return fitnessSum
           
    def allDead(self):
        for pawn in self.pawns:
            if pawn.dead == False:
                return False
        return True
    
    def naturalSelection(self):
        newGeneration = []
        self.setBestPawn()
        self.calculateFitnessSum()
        
        newGeneration.append(self.pawns[self.bestPawn].retrieveChild())
        
        for pawn in self.pawns[1:]:
            parent = self.selectParent()
            newGeneration.append(parent.retrieveChild())
        self.pawns = newGeneration.clone() # MAYBE ISSUE
        self.generation += self.generation
            
        
    def selectParent(self):
        random = random.randint(0, self.calculateFitnessSum())
        runningSum = 0
        for pawn in self.pawns:
            runningSum += pawn.fitness
            if runningSum > random:
                return pawn
            
        return None
    
    def mutate(self):
        for pawn in self.pawns:
            pawn.brain.mutate()
            
    def setBestPawn(self):
        max = 0.0
        maxIndex = 0
        for i in range(self.pawns.size):
            if self.pawns[i].fitness > max:
                max = self.pawns[i].fitness
                maxIndex = i
        self.bestPawn = maxIndex
        
    def retrievePawnAtIndex(self, index):
        return self.pawns[index]