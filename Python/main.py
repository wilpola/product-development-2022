# This is the main game file from where all actions are called from
# @date: 03/11/2022

# Import modules
import json, sys, os, pygame

#import FirstLaunch file
from firstLaunch import FirstLaunch

# Initialize pygame components
pygame.init()
pygame.font.init()

# Get settings
try:    # Try to read settings from file
    with open("Python/settings.json", "r") as settings:
        data = json.loads(settings.read())
    settings.close()

except: # If not found, compile settings
    x = FirstLaunch()
    x.compileSettings()
    
# Initialize local variables
clock       = pygame.time.Clock()
primaryFont = pygame.font.SysFont("Roboto", 32)
logoFont    = pygame.font.SysFont("Roboto", 120) 

# Address fullscreen flag
if data['fullscreen'] == True:
    tempScreen = pygame.display.set_mode((data['width'], data['height']), pygame.FULLSCREEN)
else:
    tempScreen = pygame.display.set_mode((800, 600))

# Temporary pygame elements
pygame.display.set_caption("Flowga")
tempScreen.fill('#ffffff')

# Update the screen
pygame.display.update()

# Create Gameloop
game = True
while game:
    # Set refresh rate
    clock.tick(120)     # TODO: Make this dynamic

    # Eventlistener for the game loop
    for e in pygame.event.get():
        
        # On window close
        if e.type == pygame.QUIT:
            # TODO: Add confirmation sequence
            pygame.quit()
            sys.exit()
        
        # Key press events
        if e.type == pygame.KEYDOWN:
            # TODO: Remove before production
            if e.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()