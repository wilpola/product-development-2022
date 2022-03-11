import json, sys, pygame

class Screen():

    # Initialize constructor
    def __init__(self, caption="Screen", bg="#ffffff"):
        super().__init__

        # Get display data from settings
        with open("Python/settings.json", "r") as j:
            self.data = json.loads(j.read())
        j.close()

        # Set up local variables
        self.fullscreen = self.data['fullscreen']
        self.caption    = caption
        self.Active     = False
        self.bg         = bg

    # Function to Activate the screen
    def activateScreen(self):
        # Set the window Active
        self.Active = True

        # Set window caption
        pygame.display.set_caption(self.caption)

        # -- Check whether the window is supposed to be fullscreen --#
        # If fullscreen
        if self.fullscreen  == True:
            self.screen = pygame.display.set_mode((self.data["width"], self.data["height"]), pygame.FULLSCREEN, 32)

        # If not fullscreen
        if self.fullscreen  == False:
            self.screen = pygame.display.set_mode((self.data["width"], self.data["height"]), depth=32)

        # Set screen background
        self.screen.fill(self.bg)

    # Function to Deactivate the screen
    def deactivateScreen(self):
        # Set window Unactive
        self.Active = False

    # Check whether the Window is Active or not
    # --> Return [ True / False]
    def isActive(self):
        return self.Active
    
    # Run update sequence
    def updateScreen(self):
        # If the screen is Active
        if self.isActive():
            self.activateScreen()
        # If screen is not Active --> Hide it
        else:
            self.deactivateScreen()

        # Actually update the screen
        pygame.display.update()

    
    # Blitting function, to place buttons and other items on to the screen
    def blit(self, surf, loc):
        self.screen.blit(surf, loc)