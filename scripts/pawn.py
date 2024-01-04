#https://www.youtube.com/watch?v=BOZfhUcNiqk&list=PL0GAfTAM4-tM4hxBJudlLvYSAuLaY4jvs&index=22&t=2s
import numpy as np
import random
from Brain import Brain
from Direction import Direction

class Pawn:
    def __init__(self):
        self.brain = Brain(500)
        self.nextMove = Direction.NONE
        self.posx = []
        self.posz = []
        self.velx = []
        self.velz = []
        self.accx = []
        self.accz = []
        self.key = ""
        self.fitness = 0
        self.dead = False
        self.reachedGoal = False
        self.distance = 0
    
    def update(self, distance, posx, posz, velx, velz, accx, accz):
        if (not self.reachedGoal and not self.dead):
            self.nextMove = self.move()
            self.distance = float(distance)
            self.posx.append(float(posx))
            self.posz.append(float(posz))
            self.velx.append(float(velx))
            self.velz.append(float(velz))
            self.accx.append(float(accx))
            self.accz.append(float(accz))
            if (float(posx) < -10 or float(posx) > 2390 or float(posz) < -1600):
                self.dead = True
                # print("PAWN DIED")
            elif (self.distance < 100):
                self.reachedGoal = True
                self.dead = True
                # print("PAWN DIED BY REACHING GOAL")

    def move(self):
        if (self.brain.step == self.brain.size):
            self.dead = True
            # print("KILLED BY STEP COUNTER. STEP: " + str(self.brain.step) + " SIZE: " + str(self.brain.size))
        if (not self.reachedGoal or not self.dead):
            if (self.brain.directions.size > self.brain.step):
                move = self.brain.directions[self.brain.step]
                
                self.brain.step += 1
                return move
        else:
            return Direction.NONE
        
    def calculateFitness(self):
        if self.reachedGoal:
            self.fitness = 1.0/(self.brain.step * self.brain.step)
        else:
            self.fitness = 1.0/(self.distance*self.distance)
        
    def retrieveChild(self):
        child = Pawn()
        child.brain = self.brain.clone()
        return child
    
    def updateMove(self, move):
        self.nextMove = move