# This is a simple bygame button that is reusable acress all of the screens
# within the game.

import pygame
import sys
pygame.init()

class Button():
    def __init__(self, loc, label="Label", x=100, y=100, w=100, h=35, bg="#333333", fntColor='#ffffff', radius = 5):
        super().__init__
        print('Button was imported')
        primaryFont = pygame.font.SysFont("Sans-serif", 22) 

        # Set up local content
        self.fntColor   = fntColor
        self.radius     = radius
        self.label      = label
        self.loc        = loc
        self.bg         = bg
        self.x          = x
        self.y          = y
        self.w          = w
        self.y          = y

        # This is a local copy of all the elements, if they were to change during 
        # the lifecycle of a given button component
        self.stored = { 
            "label": f"{label}",
            "loc": f"{loc}", 
            "bg": f"{bg}", 
            "x": f"{x}", 
            "y": f"{y}", 
            "w": f"{w}", 
            "fntColor": f"{fntColor}", 
            "buttonColor": f"{bg}" 
        }

        # "": f"{}",

        # Set up button "Rectangle"
        self.buttonSurface  = pygame.Rect(x, y, w, h)
        self.buttonColor    = self.bg
        self.pressed        = False            # This is to handle click events

        # Set up "Label"
        self.label      = primaryFont.render(self.label, True, self.fntColor)
        self.textArea   = self.label.get_rect(center = self.buttonSurface.center) 


    def handleClick(self):
        # Get mouse position
        mouse = pygame.mouse.get_pos()

        if self.buttonSurface.collidepoint(mouse):
            self.buttonColor = (240, 0, 100)

            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed == True:
                    self.pressed = False
                    self.clicked = True
                    print(self.stored["label"], "was printed")
                    
                    if self.stored["label"] == 'HELP':
                        pygame.quit()
                        sys.exit()

        else:
            self.buttonColor = self.stored["buttonColor"]
            self.fntColor = self.stored['fntColor']


    def DrawButton(self):
        pygame.draw.rect(self.loc, self.buttonColor, self.buttonSurface, border_radius = self.radius)
        self.loc.blit(self.label, self.textArea)
        self.handleClick()
        pygame.display.update()