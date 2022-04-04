# @desc: this is the Main Menu sequence, that will become the main sequence of the entire game.
# When the user clicks start from the main menu sequence, the game() loop will be activated.

import pygame
import sys
import os


# initialize pygame and its fonts
pygame.init()
pygame.font.init()

def MainMenu():         # The outer program layer

    clock = pygame.time.Clock()

    w = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption("Flowga")

    # defining a font 
    font = pygame.font.SysFont('Sans-serif',32) 
    
    # rendering a text written in 
    # this font 
    
    optionsBtn= font.render('Options' , True , (240, 0, 100)) 
    optionsBtn_width = optionsBtn.get_width()
    
    quitBtn = font.render('Quit' , True , (240, 0, 100))
    quitBtn_width = quitBtn.get_width()

    def updateScreen():

        w.fill((230,230,250)) # lavender
        w.blit(optionsBtn , (1000/2 - (optionsBtn_width / 2), 500 )) 
        w.blit(quitBtn, (1000/2 - (quitBtn_width / 2), 570)) 

        quitBtn.get_rect()
        pygame.display.update()

    def btnHover(mouse): 
        # set collide for buttons
        pass
        


    running = True
    while running:
        clock.tick(120) # Refresh the application 120 times per second

        # Listen for events within the loop
        for e in pygame.event.get():
            # if use Exits, close pygame instance --> close python application
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            else:
                continue

        # --------------------------------------------------- #
        # This is where the main code will go

        updateScreen()

        mouse = pygame.mouse.get_pos() 



        # End of main code
        # --------------------------------------------------- #\

MainMenu()