# @author: Ville Wilpola
# @date: 2022-2-4
# @desc: This file sets up the environment during the initial load. 
#   -> Down the line, this file will load user settings from local memory,
#   -> and dynamically use them during runtime. These can also been changed from
#   -> the settings of the game.

import pygame           # import pygame lib
import constants as c   # import all constants
pygame.init()           # initialize pygame lib


def setup():
    screenSurface = pygame.display.set_mode((c.screen["WIDTH"], c.screen["HEIGHT"])) #pygame.RESIZABLE)
    pygame.display.set_caption("Flowga app")

    bg = pygame.Surface((
        c.screen["WIDTH"],              # Dynamically assign width
        c.screen["HEIGHT"]              # Dynamically assign height
        ))
    bg.fill(c.white)                    # Fill bg

    screenSurface.blit(bg, (0,0))       # 
    pygame.display.update()             # Update the screen

if __name__ == "__main__":
    pass
else:
    setup()
    # print('Working as intended...')