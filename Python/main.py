# This is the main game file from where all actions are called from
# @date: 03/11/2022

# Import modules
import json, sys, os, pygame

#import FirstLaunch file
from firstLaunch import FirstLaunch
from components.Screen import Screen
from components.Button import Button

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

# Create separate screens
# Create mainMenu screen
mainMenuScreen = Screen("Main Menu | Flowga", bg='#4a4a4a')
mainMenuScreen.activateScreen() # Set MainMenu active when game is launched

# Create mainMenu screen
settingsScreen = Screen("Settings | Flowga", bg='#ffffff')

# Create Buttons

startButton = Button(
    mainMenuScreen.screen, 
    'Start', 
    x = (data['width'] / 2 - 50),
    y = (data['height']  / 2)
)
statsButton = Button(
    mainMenuScreen.screen, 
    'Stats', 
    x = (data['width'] / 2 - 50),
    y = (data['height']  / 2 + 60)
)
optionsButton = Button(
    mainMenuScreen.screen, 
    'Options', 
    x = (data['width'] / 2 - 50),
    y = (data['height']  / 2 + 120)
)
quitButton = Button(
    mainMenuScreen.screen, 
    'Quit', 
    x = (data['width'] / 2 - 50),
    y = (data['height']  / 2 + 180)
)

def updateScreen():
    startButton.DrawButton()
    statsButton.DrawButton()
    optionsButton.DrawButton()
    quitButton.DrawButton()

    
    # Update the screen
    pygame.display.update()

# Create Gameloop
game = True
while game:
    # Set refresh rate
    clock.tick(120)     # TODO: Make this dynamic

    # Call screen updater
    updateScreen()

    # MainMenu Content
    if mainMenuScreen.isActive():
        logo = logoFont.render("Flowga", True, (0, 220, 140))
        version = primaryFont.render("v1.2", True, (100, 100, 120))
        lWidth = logo.get_width()

        mainMenuScreen.blit(logo, (data['width'] / 2 - lWidth / 2, 150))
        mainMenuScreen.blit(version, (data['width'] / 2 + 110, 215))
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_1:
                    mainMenuScreen.deactivateScreen()
                    settingsScreen.activateScreen()

    # Settings Content
    if settingsScreen.isActive():
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_1:
                    settingsScreen.deactivateScreen()
                    mainMenuScreen.activateScreen()
    # Eventlistener for the game loop
    for e in pygame.event.get():

        # Track mouse location
        
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
