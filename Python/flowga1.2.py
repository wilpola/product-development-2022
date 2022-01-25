import pygame
import sys
from pygame.locals import *
import randomizer1
pygame.init()

# app window
widescreen = 1024
heigthscreen = 800
surfacescreen = pygame.display.set_mode((widescreen, heigthscreen))
pygame.display.set_caption("Flowga")


# Colors
musta = (0,0,0)   # black color
puna = (255,0,0)  # red color
vihr = (0,255,0)  # green color
sini = (0,0,255)  # blue color
testvihr = (0, 200, 200)
testjoku = (100,100,100,20)

# Objects size, mainly rectangles
tausta = pygame.Surface((1024,800))
suorakaide1 = pygame.Surface((300,50))
suorakaide2 = pygame.Surface((300,50))
suorakaide3 = pygame.Surface((300,50))
suorakaide4 = pygame.Surface((320,60))
card_deal = pygame.Surface((60, 100))

#  Text, font, color
fonttioption1 = pygame.font.SysFont('arial', 40)
tekstibutton1 = fonttioption1.render('Short Training', True, sini)
tekstibutton2 = fonttioption1.render('Middle Training', True, testjoku)
tekstibutton3 = fonttioption1.render('Long Training', True, puna)


#Text for cards, later replaced with pictures?
card_text = fonttioption1.render('0', True, testvihr)




tausta.fill(testvihr)
suorakaide1.fill(puna)
suorakaide2.fill(vihr)
suorakaide3.fill(sini)
suorakaide4.fill(testjoku)
card_deal.fill(testjoku)


surfacescreen.blit(tausta, (0,0))
surfacescreen.blit(suorakaide1, (550,200))
surfacescreen.blit(suorakaide2, (550,300))
surfacescreen.blit(suorakaide3, (550,400))
surfacescreen.blit(suorakaide4, (540,195))


pygame.display.flip()


# area for collision, used to recognize mouse collision later
option_area1 = suorakaide1.get_rect()
option_area2 = suorakaide2.get_rect()
option_area3 = suorakaide3.get_rect()
chosen_area = suorakaide4.get_rect()

option_area1.left = 550
option_area1.top = 200
option_area2.left = 550
option_area2.top = 300
option_area3.left = 550
option_area3.top = 400

chosen_area.left = 540      # Chosen area coordinates, used for "highlighting" what option is in collision with mouse
chosen_area.top = 195

#list of cards will be filled with random "cards".
#card positions are locked positions to make things easier
list_of_cards = []
card_position = [(50,50), (150,50), (250,50), (350,50), (450,50),
                 (50,250), (150,250), (250,250), (350,250), (450,250),
                 (50,450), (150,450), (250,450), (350,450), (450,450)]

kello = pygame.time.Clock()     # Do we need it? Used it for testing earlier, but decided to leave it here for now....


counter = 0         # counter for picking first option, length of training.
card_count = 0      # I forgot does this do anything or not.......
training_time = ""  # placeholder for Length. determines 5, 10 or 15 cards
training_type = ""  # placeholder for type. determines which lists are used for randomizer

#############################################################################################

while True:
    
    # check if the user has closed the display-window or pressed esc
    for tapahtuma in pygame.event.get():  # all the events in the event queue
        if tapahtuma.type == pygame.QUIT: # if the user closed the window
            pygame.quit() # the display-window closes
            sys.exit()    # the whole python program exits
        if tapahtuma.type == KEYDOWN:     # if the user pressed down any key
            if tapahtuma.key == K_ESCAPE: # if the key was esc
                pygame.quit() # the display-window closes
                sys.exit()    # the whole python program exits


###########################################################################################

    #Mouse position and mouse click
        if option_area1.collidepoint(pygame.mouse.get_pos()):   # Option 1, top one
            chosen_area.left = 540
            chosen_area.top = 195
            if counter == 2 and tapahtuma.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()   # For now, we don't have anything after "start game", so for placeholder it exits the game/app
                sys.exit()
            elif counter == 1 and tapahtuma.type == pygame.MOUSEBUTTONDOWN:
                training_type = "option1"
                for i in randomizer1.training_program(training_time, training_type): # Calls randomizer, which was imported
                    list_of_cards.append(i)
                #print(training_time)
                counter += 1
                tekstibutton1 = fonttioption1.render('Start training', True, sini)
                tekstibutton2 = fonttioption1.render('Reroll', True, testjoku)
                tekstibutton3 = fonttioption1.render('Back to main menu', True, puna)
                
            elif counter == 0 and tapahtuma.type == pygame.MOUSEBUTTONDOWN:
                counter += 1
                training_time = "option1"
                tekstibutton1 = fonttioption1.render('Strength', True, sini)
                tekstibutton2 = fonttioption1.render('Flexibility', True, testjoku)
                tekstibutton3 = fonttioption1.render('Relaxation', True, puna)
                
        if option_area2.collidepoint(pygame.mouse.get_pos()):   # option 2, middle
            chosen_area.left = 540
            chosen_area.top = 295
            if counter == 2 and tapahtuma.type == pygame.MOUSEBUTTONDOWN:
                list_of_cards.clear()
                for i in randomizer1.training_program(training_time, training_type):
                    list_of_cards.append(i)
         
            elif counter == 1 and tapahtuma.type == pygame.MOUSEBUTTONDOWN:
                training_type = "option2"
                for i in randomizer1.training_program(training_time, training_type):
                    list_of_cards.append(i)
                counter += 1
                tekstibutton1 = fonttioption1.render('Start training', True, sini)
                tekstibutton2 = fonttioption1.render('Reroll', True, testjoku)
                tekstibutton3 = fonttioption1.render('Back to main menu', True, puna)
            elif counter == 0 and tapahtuma.type == pygame.MOUSEBUTTONDOWN:
                counter += 1
                training_time = "option2"
                tekstibutton1 = fonttioption1.render('Strength', True, sini)
                tekstibutton2 = fonttioption1.render('Flexibility', True, testjoku)
                tekstibutton3 = fonttioption1.render('Relaxation', True, puna)

        if option_area3.collidepoint(pygame.mouse.get_pos()):   # option 3, lowest
            chosen_area.left = 540
            chosen_area.top = 395
            if counter == 2 and tapahtuma.type == pygame.MOUSEBUTTONDOWN:
                counter = 0
                list_of_cards.clear()
                tekstibutton1 = fonttioption1.render('Short Training', True, sini)
                tekstibutton2 = fonttioption1.render('Middle Training', True, testjoku)
                tekstibutton3 = fonttioption1.render('Long Training', True, puna)       
            elif counter == 1 and tapahtuma.type == pygame.MOUSEBUTTONDOWN:
                training_type = "option3"
                for i in randomizer1.training_program(training_time, training_type):
                    list_of_cards.append(i)
                counter += 1
                tekstibutton1 = fonttioption1.render('Start training', True, sini)
                tekstibutton2 = fonttioption1.render('Reroll', True, testjoku)
                tekstibutton3 = fonttioption1.render('Back to main menu', True, puna)
            elif counter == 0 and tapahtuma.type == pygame.MOUSEBUTTONDOWN:
                counter += 1
                training_time = "option3"
                tekstibutton1 = fonttioption1.render('Strength', True, sini)
                tekstibutton2 = fonttioption1.render('Flexibility', True, testjoku)
                tekstibutton3 = fonttioption1.render('Relaxation', True, puna)
                

##############################################################################################


    surfacescreen.blit(tausta, (0,0))
    surfacescreen.blit(suorakaide4, chosen_area)
    surfacescreen.blit(suorakaide1, option_area1)
    surfacescreen.blit(suorakaide2, option_area2)
    surfacescreen.blit(suorakaide3, option_area3)
    surfacescreen.blit(tekstibutton1,(570, 200))
    surfacescreen.blit(tekstibutton2,(570, 300))
    surfacescreen.blit(tekstibutton3,(570, 400))

    for i in range(0, len(list_of_cards)):                      # Loop for creating cards on screen
        surfacescreen.blit(card_deal, card_position[i])
        x = str(list_of_cards[i])
        card_text = fonttioption1.render(x, True, puna)
        surfacescreen.blit(card_text, (card_position[i][0] + 10, card_position[i][1] + 20))
    pygame.display.flip()
    kello.tick(200)
