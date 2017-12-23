
import pygame
from pygame.locals import *

from settings import *
from matrix import *

import sys

class Surface():
    def __init__(self, window):
        self.display = window
        self.display.fill(WHITE)

    def drawGrid(self):
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line (self.display, BLACK,(x,0),(x,HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.display, BLACK, (0,y), (WIDTH,y))

    def drawCells(self, matrix):
        for x in range(COLS):
            for y in range(ROWS):
                if matrix.getChildAt(x, y) == 1:
                    pygame.draw.rect(self.display, ORANGE, (x*TILESIZE,y*TILESIZE,TILESIZE,TILESIZE))
                else:
                    pygame.draw.rect(self.display, WHITE, (x*TILESIZE,y*TILESIZE,TILESIZE,TILESIZE))

class Game():
    def __init__(self):
        pygame.init()
        window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.playing = True
        self.world = Matrix("gaia")
        self.view = Surface(window)
        self.world.populateRandom()
    
    def quit(self):
        pygame.quit()
        sys.exit()
    
    def run(self):
        clock = pygame.time.Clock()

        while self.playing:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    self.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.quit()
                    if event.key == pygame.K_LEFT:
                        drawGrid
                    
                self.view.drawCells(self.world)
                self.view.drawGrid()

                pygame.display.update()
        
        self.quit()

if __name__=='__main__':
    game = Game()
    game.run()
