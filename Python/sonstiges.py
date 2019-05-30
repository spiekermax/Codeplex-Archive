# (c) Maximilian Spiekermann, 2016

import pygame
from maxamathics import devidable

class grid ():

    # Benötigte Variablen
    size = 0
    surface = None
    screenwidth = 0
    screenheight = 0
    # Optionale Variablen
    highlight = 5
    color = [60, 60, 60]

    def __init__ (self, size, surface, screenwidth, screenheight):
        self.size = size
        self.surface = surface
        self.screenwidth = screenwidth
        self.screenheight = screenheight

    def draw (self):
        # Horizontale
        for n in range (0, self.size):
            pygame.draw.line(self.surface, self.color, [0, n*self.screenheight/
            (self.size*self.screenwidth/self.screenheight)], [self.screenwidth,
            n*self.screenheight/(self.size*self.screenwidth/self.screenheight)], 1)
