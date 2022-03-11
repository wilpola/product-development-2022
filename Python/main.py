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

# -- Settings Retrieval -- #
# Make sure that settings have been compiled before
# running the game
settings = False
while not settings:
    if os.path.exists("Python/settings.json"):
        settings = True
    else:
        x = FirstLaunch()
        x.compileSettings()

with open("Python/settings.json", "r") as s_file:
    data = json.loads(s_file.read())
s_file.close()
# -- End of Settings Retrieval -- #
    
# Initialize local variables
clock       = pygame.time.Clock()
primaryFont = pygame.font.SysFont("Roboto", 32)
logoFont    = pygame.font.SysFont("Roboto", 120) 

# Create separate screens
# Create mainMenu screen
mainMenuScreen = Screen("Main Menu | Flowga", bg='#ffffff')
mainMenuScreen.activateScreen() # Set MainMenu active when game is launched

# Create start screen
startScreen = Screen("Start your workout | Flowga", bg="#4a4a4a")

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

easyButton = Button(
    mainMenuScreen.screen, 
    'Beginner', 
    x = (data['width'] / 3 - 100), 
    y = (data['height']  / 2 ), 
    w=200
)

intermediateButton = Button(
    mainMenuScreen.screen, 
    'Intermediate', 
    x = (data['width'] / 2 - 100),
    y = (data['height']  / 2),
    w=200
)

experiencedButton = Button(
    mainMenuScreen.screen, 
    'Experienced', 
    x = (data['width'] / 2 + (data['width'] / 6) - 100),
    y = (data['height']  / 2),
    w=200
)

backButton = Button(
    mainMenuScreen.screen, 
    'back', 
    x = (data['width'] / 2 - 100),
    y = (data['height']  - 200),
    w=200
)

# Update the screen
def updateScreen():
    pygame.display.update()

# Create Gameloop
game = True
while game:
    # Set refresh rate
    clock.tick(120)     # TODO: Make this dynamic

    # Call screen updater
    updateScreen()
    mouse = pygame.mouse.get_pos()

    def bye():
        if e.type == pygame.QUIT:
            # TODO: Add confirmation sequence
            pygame.quit()
            sys.exit()

    # MainMenu Content
    if mainMenuScreen.isActive():
        logo = logoFont.render("Flowga", True, (0, 220, 140), mainMenuScreen.bg)
        version = primaryFont.render("alpha-1.2", True, (100, 100, 120), mainMenuScreen.bg)
        lWidth = logo.get_width()

        mainMenuScreen.blit(logo, (data['width'] / 2 - lWidth / 2, 150))
        mainMenuScreen.blit(version, (data['width'] / 2 - 140, 220))
        
        startButton.DrawButton()
        statsButton.DrawButton()
        optionsButton.DrawButton()
        quitButton.DrawButton()

    # Main Menu Eventlistener
        for e in pygame.event.get():
            bye()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_1:
                    mainMenuScreen.deactivateScreen()
                    settingsScreen.activateScreen()
            
            # Click events
            if startButton.isHovered() and e.type == pygame.MOUSEBUTTONUP:
                mainMenuScreen.deactivateScreen()
                startScreen.activateScreen()

            if optionsButton.isHovered() and e.type == pygame.MOUSEBUTTONUP:
                mainMenuScreen.deactivateScreen()
                settingsScreen.activateScreen()

            if quitButton.isHovered() and e.type == pygame.MOUSEBUTTONUP:
                pygame.quit()
                sys.exit()

    # -- END OF MAIN MENU -- #

    # -- Start Screen sequence -- #
    if startScreen.isActive():

        header = primaryFont.render("Choose a difficulty", True, (244, 244, 244), startScreen.bg)
        hwidth = header.get_width()
  
        startScreen.blit(header,(data['width'] / 2 - (hwidth / 2), 50))
        pygame.display.update()

        easyButton.DrawButton()
        intermediateButton.DrawButton()
        experiencedButton.DrawButton()
        backButton.DrawButton()


        for e in pygame.event.get():
            bye()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    startScreen.deactivateScreen()
                    mainMenuScreen.activateScreen()
            
            if (easyButton.isHovered() and 
                    e.type == pygame.MOUSEBUTTONUP):
                pass

            if (intermediateButton.isHovered() and 
                    e.type == pygame.MOUSEBUTTONUP):
                pass

            if (backButton.isHovered() and 
                    e.type == pygame.MOUSEBUTTONUP):

                startScreen.deactivateScreen()
                mainMenuScreen.activateScreen()

    # -- End of Start Screen sequence -- #

    # Settings Content
    if settingsScreen.isActive():
        header = primaryFont.render("Settings", True, ("#333333"), settingsScreen.bg)
        hwidth = header.get_width()
        settingsScreen.blit(header,(data['width'] / 2 - (hwidth / 2), 50))
        for e in pygame.event.get():
            bye()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    settingsScreen.deactivateScreen()
                    mainMenuScreen.activateScreen()
    # -- END OF Settings Screen -- #
