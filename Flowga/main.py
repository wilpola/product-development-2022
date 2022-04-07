import sys
import pygame                   # import pygame lib
import constants as c           # import all the defined constants
from setup import setup         # import the setup function

pygame.init()                   # initialize the pygame package

setup()
x = pygame.display.get_desktop_sizes()
y = pygame.display.list_modes()
print(f'x: {x[0][0]}')
print(f'y: {y}')

running = True

clock = pygame.time.Clock()

while running:                      # main loop
    clock.tick(c.screen["FPS"])
    
    for e in pygame.event.get():    # Get all the events
        if e.type == pygame.QUIT:   
            pygame.quit()           # Close pygame corretly
            sys.exit()              # Exit the python program
        else:
            continue                # rerun the loop



