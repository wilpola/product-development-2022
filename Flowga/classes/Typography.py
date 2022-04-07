import pygame
import time

# initialize fonts for the object
pygame.font.init()      

class Typography(object):
    # Get set up with params
    def __init__(self, text="", color="#333333"):
        self.fontFamily = 'Sans-serif'
        self.text = text

    def FontFamily(self):
        return self.fontFamily

    def h1(self):
        return pygame.font.SysFont(self.fontFamily, 32)
    
    def h2(self):
        return pygame.font.SysFont(self.fontFamily, 26)
    
    def h3(self):
        return pygame.font.SysFont(self.fontFamily, 22)
    
    def h4(self):
        return pygame.font.SysFont(self.fontFamily, 18)
    
    def h5(self):
        return pygame.font.SysFont(self.fontFamily, 15)
    
    def body(self):
        x = pygame.font.SysFont(self.fontFamily,  19)
        return x.render(f"{self.text}", True, (255, 0, 255))