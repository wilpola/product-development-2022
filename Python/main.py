# This is the main game file from where all actions are called from
# @date: 03/11/2022

# Import modules
import json, sys, os, pygame, random

from pygame import mixer

#import FirstLaunch file
from firstLaunch import FirstLaunch
from components.Screen import Screen
from components.Button import Button
# from components.test import testScreen

# Initialize pygame components
pygame.init()
pygame.font.init()
pygame.mixer.init()

mixer.music.load('Python/assets/main_menu_v3.ogg')
mixer.music.play(-1)

activeCard = 0

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
# x = testScreen(caption="hello there", background="#ffffff")
mainMenuScreen = Screen("Main Menu | Flowga", bg='#ffffff')

# Music for the menu sequence etc.
menuMusic = mixer.music.load('Python/assets/main_menu_v3.ogg')
mixer.music.play(-1)    # set music to loop [ -1  = LOOP ]

pygame.mixer.music.set_volume(data['volume'])


mainMenuScreen.activateScreen() # Set MainMenu active when game is launched

# Create start screen
startScreen = Screen("Start your workout | Flowga", bg="#4a4a4a")
lengthScreen = Screen("Start your workout | Flowga", bg="#4a4a4a")
statsScreen = Screen('Stats | Flowga', bg="#4a4a4a")

# Create mainMenu screen
settingsScreen = Screen("Settings | Flowga", bg='#ffffff')

asanaPrint = True
workoutList = []

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
    y = (data['height']  / 2 - 150),
    w=200,
    h=300
)

intermediateButton = Button(
    mainMenuScreen.screen, 
    'Intermediate', 
    x = (data['width'] / 2 - 100),
    y = (data['height']  / 2 - 150),
    w=200,
    h=300
)

experiencedButton = Button(
    mainMenuScreen.screen, 
    'Experienced', 
    x = (data['width'] / 2 + (data['width'] / 6) - 100),
    y = (data['height']  / 2 - 150),
    w=200,
    h=300
)

cardScreen = Screen(' Card Screen | Flowga')
backButton = Button(
    mainMenuScreen.screen, 
    'back', 
    x = (data['width'] / 2 - 100),
    y = (data['height']  - 200),
    w=200
)

shortButton = Button(
    mainMenuScreen.screen, 
    'Short', 
    x = (data['width'] / 3 - 100), 
    y = (data['height']  / 2 - 150 ), 
    w=200,
    h=300
)

mediumButton = Button(
    mainMenuScreen.screen, 
    'Medium', 
    x = (data['width'] / 2 - 100),
    y = (data['height']  / 2 - 150),
    w=200,
    h=300
)

longButton = Button(
    mainMenuScreen.screen, 
    'Long', 
    x = (data['width'] / 2 + (data['width'] / 6) - 100),
    y = (data['height']  / 2 - 150),
    w=200,
    h=300
)
screen_center = data['width'] / 2
vol_down = Button(mainMenuScreen.screen, '<', screen_center + 10, 140, 40, 40, "#4a4a4a", "#ffffff", radius=8)
vol_up = Button(mainMenuScreen.screen, '>', screen_center + 150, 140, 40, 40, "#4a4a4a", "#ffffff", radius=8)


# cardScreen buttons
prev_btn = Button(mainMenuScreen.screen, '<', x = 5, y = data['height'] / 2 - 25, w = 50, h = 50, radius = 0)
next_btn = Button(mainMenuScreen.screen, '>', data['width'] - 55, y = data['height'] / 2 - 25, w = 50, h = 50, radius = 0)
end_wo = Button(mainMenuScreen.screen, "End workout", 40, 40, 150, bg="#DD4D2E")

# main_card = Button(mainMenuScreen.screen, 'card_id', screen_center - 160, data['height'] / 2 - 380, 340, 500, radius=15)

workoutDifficulty = ""
workoutLenght = ""

# s = pygame.Surface(data['width'], data['height'])
def createRandom(wd, wl):
    if wd == 'easy':
        cardScreen.activateScreen()
        lengthScreen.deactivateScreen()
        print(wd, wl)
    
    if wd == 'intermediate':
        cardScreen.activateScreen()
        lengthScreen.deactivateScreen()
        print(wd, wl)
    
    if wd == 'experienced':
        cardScreen.activateScreen()
        lengthScreen.deactivateScreen()
        print(wd, wl)

def workoutGenerator(data):
    l = 0
    i = 0
    if workoutLenght == 'short':
        l = 5
        x = random.choices(data, k=l)
    
    elif workoutLenght == 'medium':
        l = 10
        x = random.choices(data, k=l)

    elif workoutLenght == 'long':
        l = 15
        x = random.choices(data, k=l)
    
    else:
        print('oops... something went wrong')
    
    while i < len(x):
        workoutList.append(x[i])
        print(x[i]['asana_id'])
        i += 1

    return workoutList

# Update the screen
def updateScreen():
    pygame.display.update()

# Create Gameloop
game = True
while game:
    # Set refresh rate
    clock.tick(240)     # TODO: Make this dynamic

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

            if statsButton.isHovered() and e.type == pygame.MOUSEBUTTONUP:
                # x.activateScreen()
                statsScreen.activateScreen()
                mainMenuScreen.deactivateScreen()

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
                startScreen.deactivateScreen()
                lengthScreen.activateScreen()
                workoutDifficulty = "easy"

            if (intermediateButton.isHovered() and 
                    e.type == pygame.MOUSEBUTTONUP):
                startScreen.deactivateScreen()
                lengthScreen.activateScreen()
                workoutDifficulty = "intermediate"
                
            if (experiencedButton.isHovered() and
                    e.type == pygame.MOUSEBUTTONUP):
                startScreen.deactivateScreen()
                lengthScreen.activateScreen()
                workoutDifficulty = "experienced"
                    

            if (backButton.isHovered() and 
                    e.type == pygame.MOUSEBUTTONUP):

                startScreen.deactivateScreen()
                mainMenuScreen.activateScreen()

    # -- Start Screen sequence -- #
    if lengthScreen.isActive():

        header  = primaryFont.render("Choose length of the workout", True, (244, 244, 244), lengthScreen.bg)
        choise1 = primaryFont.render(workoutDifficulty, True, (244, 244, 244), lengthScreen.bg)
        hwidth  = header.get_width()
        cwidth  = choise1.get_width()
  
        lengthScreen.blit(header,(data['width'] / 2 - (hwidth / 2), 50))
        lengthScreen.blit(choise1,(data['width'] / 2 - (cwidth / 2), 100))
        pygame.display.update()

        shortButton.DrawButton()
        mediumButton.DrawButton()
        longButton.DrawButton()
        backButton.DrawButton()


        for e in pygame.event.get():
            bye()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    lengthScreen.deactivateScreen()
                    startScreen.activateScreen()
            
            if (shortButton.isHovered() and 
                    e.type == pygame.MOUSEBUTTONUP):
                workoutLenght = 'short'
                createRandom(workoutDifficulty, workoutLenght)

            if (mediumButton.isHovered() and 
                    e.type == pygame.MOUSEBUTTONUP):
                workoutLenght = 'medium'
                createRandom(workoutDifficulty, workoutLenght)

            if (longButton.isHovered() and 
                    e.type == pygame.MOUSEBUTTONUP):
                workoutLenght = 'long'
                createRandom(workoutDifficulty, workoutLenght)

            if (backButton.isHovered() and 
                    e.type == pygame.MOUSEBUTTONUP):

                lengthScreen.deactivateScreen()
                startScreen.activateScreen()

    # -- End of Start Screen sequence -- #

    # Settings Content
    if settingsScreen.isActive():
        screen_center = data['width'] / 2
        header = primaryFont.render("Settings", True, ("#333333"), settingsScreen.bg)
        hwidth = header.get_width()
        settingsScreen.blit(header,(screen_center - (hwidth / 2), 50))


        # Listing the settings
        volume = data['volume']

        # Actual settings
        vol_text = primaryFont.render('Volume', True, ("#333333"), settingsScreen.bg)
        vol_width = vol_text.get_width()
        vol_value_text = primaryFont.render(str(int(data['volume'] * 100)) + '%', True, ("#333333"), settingsScreen.bg)
        # vol_value_bg = vol_value_text.get_rect()
        # vol_value_bg.center = (screen_center)

        vol_down.DrawButton()
        vol_up.DrawButton()

        settingsScreen.blit(vol_text, (400, 150))
        settingsScreen.blit(vol_value_text, (screen_center + 80, 150))

        backButton.DrawButton()


        def openSettings():
            with open('Python/settings.json', "r") as s:
                s = json.loads(s.read())
            s.close()

        def updateVolume():
            # open settings
            with open("Python/settings.json", "w") as s_e:
                json.dump(data, s_e, sort_keys=True)
            s_e.close()


            pygame.mixer.music.set_volume(data['volume'])

        for e in pygame.event.get():
            bye()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    settingsScreen.deactivateScreen()
                    mainMenuScreen.activateScreen()

            
            if (vol_up.isHovered() and e.type == pygame.MOUSEBUTTONUP):
                # settingsScreen.fill()
                if data['volume'] >= 1:
                    data['volume'] = 1
                    print('Max_volume')
                    updateVolume()
                    settingsScreen.fill()
                else:
                    data['volume'] += 0.1
                    data['volume'] = round(data['volume'], 1)
                    print(data['volume'])
                    pygame.mixer.music.set_volume(data['volume'])
                    updateVolume()
                    settingsScreen.fill()

                updateScreen()

            if (vol_down.isHovered() and e.type == pygame.MOUSEBUTTONUP):
                # settingsScreen.fill()
                if data['volume'] <= 0:
                    data['volume'] = 0
                    data['volume'] = round(data['volume'], 1)
                    print(data['volume'])
                    print('Deafened')
                    updateVolume()
                    settingsScreen.fill()
                else:
                    settingsScreen.fill()
                    data['volume'] -= 0.1
                    data['volume'] = round(data['volume'], 1)
                    pygame.mixer.music.set_volume(data['volume'])
                    updateVolume()

            if (backButton.isHovered() and e.type == pygame.MOUSEBUTTONUP):
                settingsScreen.deactivateScreen()
                mainMenuScreen.activateScreen()

                updateScreen()
    # -- END OF Settings Screen -- #
    
    # CardScreen
    if cardScreen.isActive():
        # cardScreen.fill()
        header = primaryFont.render("Cards", True, ("#333333"), cardScreen.bg)
        hwidth = header.get_width()

        cardScreen.blit(header,(data['width'] / 2 - (hwidth / 2), 50))


        try:
            with open("Python/asanas.json", "r") as a:
                asana = json.loads(a.read())
            a.close()
        # If file is not found, set data to empty Brackets
        except:
            asana = {"text":"Asanas vere not found"}

        if asanaPrint == True:
            print(" ")
            asanaPrint = False
            workoutGenerator(asana)
            
            y = 250

        main_card = Button(cardScreen.screen, f"Asana #{str(workoutList[activeCard]['asana_id'])}", screen_center - 150, data['height'] / 2 - 300, 300, 400, radius=15, font = 'L')
        card_id = primaryFont.render(f"{activeCard + 1} / {len(workoutList)}", True, "#333333", "#ffffff")
        card_id_width = card_id.get_width()
        card_rect = card_id.get_rect()

        cardScreen.blit(card_id, (data['width'] / 2 - card_id_width / 2, data['height'] - 250))
        end_wo.DrawButton()
        prev_btn.DrawButton()
        next_btn.DrawButton()
        main_card.DrawButton()

        z = 0
        for i in range(3):
            x = f"card_{i}"
            x = Button(cardScreen.screen, f"{str(workoutList[i]['asana_id'])}", screen_center - 340 / 2 + z, data['height'] - 200, h = 100)
            x.DrawButton()
            z += 120

        
        for e in pygame.event.get():
            bye()
        
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    cardScreen.deactivateScreen()
                    lengthScreen.activateScreen()
                    asanaPrint = True
                    workoutList = []

            if (end_wo.isHovered() and e.type == pygame.MOUSEBUTTONUP):
                cardScreen.deactivateScreen()
                mainMenuScreen.activateScreen()
                asanaPrint = True
                workoutList = []

            if end_wo.isHovered():
                end_wo = Button(cardScreen.screen, '<-- End workout', 40, 40, 150, bg="#DD4D2E")
                pygame.display.flip()
            else:
                end_wo = Button(cardScreen.screen, 'End workout', 40, 40, 150, bg="#DD4D2E")
                pygame.display.flip()

            if (next_btn.isHovered() and e.type == pygame.MOUSEBUTTONUP):
                cardScreen.fill()

                if activeCard == len(workoutList) - 1:
                    activeCard = 0
                
                    card_id = primaryFont.render(f"{activeCard + 1} / {len(workoutList)}", True, "#333333", "#ffffff")
                    cardScreen.blit(card_id, (data['width'] / 2 - card_id_width / 2, data['height'] - 250))



                else:
                    activeCard += 1
                    
                    card_id = primaryFont.render(f"{activeCard + 1} / {len(workoutList)}", True, "#333333", "#ffffff")
                    cardScreen.blit(card_id, (data['width'] / 2 - card_id_width / 2, data['height'] - 250))

            if (prev_btn.isHovered() and e.type == pygame.MOUSEBUTTONUP):
                cardScreen.fill()


                if activeCard == 0:
                    activeCard = len(workoutList) - 1
                    
                    card_id = primaryFont.render(f"{activeCard + 1} / {len(workoutList)}", True, "#333333", "#ffffff")
                    cardScreen.blit(card_id, (data['width'] / 2 - card_id_width / 2, data['height'] - 250))
                    cardScreen.fill()
                    x.DrawButton()

                else:
                    activeCard -= 1
                    
                    card_id = primaryFont.render(f"{activeCard + 1} / {len(workoutList)}", True, "#333333", "#ffffff")
                    cardScreen.blit(card_id, (data['width'] / 2 - card_id_width / 2, data['height'] - 250))
                    x.DrawButton()

            else:
                pass

        
            
            # cardScreen.fill()


            
    # -- END OF Settings Screen -- #

    # StatsScreen
    if statsScreen.isActive():
        backButton.DrawButton()

        header = primaryFont.render("Stats", True, "#efefef", "#4a4a4a")
        hwidth = header.get_width()

        statsScreen.blit(header,(data['width'] / 2 - (hwidth / 2), 50))

        noticeFont = pygame.font.SysFont('Sans-serif', 40)

        noticeText = noticeFont.render("This section is under construction", True, "#efefef", '#4a4a4a' )
        noticeWidth = noticeText.get_width()

        checkText = primaryFont.render("Please check back later.", True, "#ffffff", "#4a4a4a")
        checkWidth = checkText.get_width()

        # Blit the text to the screen
        statsScreen.blit(noticeText, (data["width"] / 2 - (noticeWidth / 2), 300))
        statsScreen.blit(checkText, (data["width"] / 2 - (checkWidth / 2), 360))

        pygame.display.update()

        if backButton.isHovered() and e.type == pygame.MOUSEBUTTONUP:
            mainMenuScreen.activateScreen()
            statsScreen.deactivateScreen()

        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    mainMenuScreen.activateScreen()
                    statsScreen.deactivateScreen()