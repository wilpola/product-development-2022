# The purpose of this file is to only be fired when settings
# are being reset, or if the application is launched for the 
# very first time
# --> If settings.json is not found, run this file

import json, pygame
pygame.init()

class FirstLaunch():

    # Initialize constructor
    def __init__(self):
        super().__init__

        # Attempt to access settings.json
        try:
            with open("Python/settings.json", "r") as j:
                self.data = json.loads(j.read())
            j.close()
        # If file is not found, set data to empty Brackets
        except:
            self.data = {}

    def compileSettings(self):

        # Get native resolution
        nativeDimensions = pygame.display.get_desktop_sizes()[0]

        # save width
        self.width = nativeDimensions[0]
        self.data['width'] = self.width

        # Save height
        self.height = nativeDimensions[1]
        self.data['heigt'] = self.height

        # List of supported resolutions
        self.resolutionList = pygame.display.list_modes()
        self.data['resolutionList'] = self.resolutionList

        # Full screen status [ True / False ]
        # On first launch set to True
        self.fullscreen = True
        self.data['fullscreen'] = self.fullscreen

        # Volume Control [ 0 - 10 ]
        self.data['volume'] = 5

        # Animations
        # As we don't have any, this is set to False
        self.data['animations'] = False

        # Write changes to file
        self.writeSettings()
    
    def writeSettings(self):
        # Open the file 
        # --> if not found, create the file
        with open("Python/settings.json", "w") as j_e:
            # Sort keys before pushing
            json.dump(self.data, j_e, sort_keys=True) 
        # Close the file and save
        j_e.close()
