# @author: Ville Wilpola
# @date: 2022-2-4
# @desc: This file sets up the environment during the initial load. 
#   -> Down the line, this file will load user settings from local memory,
#   -> and dynamically use them during runtime. These can also been changed from
#   -> the settings of the game.

from decimal import Rounded
import pygame           # import pygame lib
import constants as c   # import all constants
# from classes.RoundedButton import (RoundedButton)
from classes.Typography import *
pygame.init()           # initialize pygame lib

def setup():
    screenSurface = pygame.display.set_mode((c.screen["WIDTH"], c.screen["HEIGHT"])) #pygame.RESIZABLE)
    pygame.display.set_caption("Flowga app")

    z = Typography(text="Welcome Dobby")

    bg = pygame.Surface((
        c.screen["WIDTH"],              # Dynamically assign width
        c.screen["HEIGHT"]              # Dynamically assign height
        ))
    bg.fill(c.white)                    # Fill bg

    screenSurface.blit(bg, (0,0))       #
    # screenSurface.blit(t.me, (0,0))
    z.body()
    pygame.display.update()             # Update the screen
    # t.drawBtn()

if __name__ == "__main__":
    pass
else:
    setup()
    # print('Working as intended...')