# imports for populate
import numpy
import random

from settings import *

class Being():
    def __init__(self, name):
        self.name = name
        print(name + " is living ...")

class Matrix(Being):
    def __init__(self, name):
        super().__init__(name)
        self.children = numpy.zeros ((COLS, ROWS),dtype=numpy.dtype('b'))
    
    def populateRandom(self):
        for x in range (COLS):
            for y in range (ROWS):
                self.children[x,y] = random.randint(0,1)
    
    def getNeighbours(self, cell):
        neighbours = 0
        for mod_x in range(-1, 1):
            for mod_y in range(-1, 1):
                if mod_x == 0 and mod_y == 0:
                    continue
                neighbourCell += self.getChildAt(cell[0]+mod_x, cell[1]+mod_y)

    def getChildAt(self, x, y):
        return self.children[x, y]

class Child(Being):
    def __init__(self, name):
        super().__init__(name)