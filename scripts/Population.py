import numpy as np
import random
from Brain import Brain
from Direction import Direction
from Pawn import Pawn
import math

class Population:
    def __init__(self, size):
        self.pawns = []
        self.generation = 1
        self.bestPawn = 1
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
        print("GENERATION COMPLETE: " + str(self.generation) + " BEST PAWN STEPS: " + str(self.pawns[self.bestPawn].brain.step) + " REACHED GOAL: " + str(self.pawns[self.bestPawn].reachedGoal) + " FITNESS: " + str(self.pawns[self.bestPawn].fitness))
        mutationRate = .05 * math.e ** (-.2 * self.generation) 
        print("MUTATION RATE FOR GENERATION " + str(self.generation) + " = " + str(mutationRate))

        newGeneration.append(self.pawns[self.bestPawn].retrieveChild())
        
        for pawn in self.pawns[1:]:
            parent = self.selectParent()
            child = parent.retrieveChild()
            child.brain.mutate(mutationRate)
            newGeneration.append(child)
        self.pawns = newGeneration
        self.generation += 1
            
        
    def selectParent(self):
        randomNum = random.uniform(0, int(self.calculateFitnessSum()))
        runningSum = 0
        for pawn in self.pawns:
            runningSum += pawn.fitness
            if runningSum > randomNum:
                return pawn
            
        return None
    
    def mutate(self):
        mutationRate = 0#.05 * math.e ** (-.3 * self.generation) 
        print("MUTATION RATE FOR GENERATION " + str(self.generation) + " = " + str(mutationRate))
        for pawn in self.pawns:
            pawn.brain.mutate(mutationRate)
            
    def setBestPawn(self):
        max = 0.0
        maxIndex = 0
        for i in range(len(self.pawns)):
            if self.pawns[i].fitness > max:
                max = self.pawns[i].fitness
                maxIndex = i
        self.bestPawn = maxIndex
        
    def retrievePawnAtIndex(self, index):
        return self.pawns[index]
    
    def realive(self):
        for pawn in self.pawns:
            pawn.dead = False
            pawn.brain.step = 0
            pawn.nextMove = Direction.NONE
            pawn.reachedGoal = False
        
