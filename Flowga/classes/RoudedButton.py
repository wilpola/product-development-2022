# @desc: This document contains the button class that will
# be used in main-menu and settings screens. The Button will be fully
# reusable, and customizable to fit different usecases.
import pygame
class RoundedButton(object):
    # initialize class with a constructor
    def __init__(self, name = 'test', title = 'test', surface = 'screenSurface', x = 100, y = 100):
        self.name = name
        self.title = title
        self.surface = surface
        self.x = x
        self.y = y
        
        color = (48, 141, 70)
        
        self.me = pygame.Surface((x, y))
        # self.me.fill(pygame.draw.rect(self.me, color, pygame.Rect(30, 30, 60, 60), border_radius=8))
        self.rect = pygame.draw.rect(self.me, color, pygame.Rect(30, 30, 60, 60), border_radius=8)

    # Add to the screen