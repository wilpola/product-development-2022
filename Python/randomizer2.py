"""
Instructions:
-> create a deck with:
    4 cards for warmup, 
    20 cards for strenght, 
    20 cards for flexibility, 
    25 cards for balance, 
    15 cards for relax, 
    10 cards for cooldown,
    1 card for savasana.

Modify the randomizer so it will accept:

-Three lenghts of exercises.
-Four different training modes (Strenght, flexibility, balance, relaxation)
-Balance training shall include strenght, flexibility and balance cards.
-All the trainings shall start with warmup, then have the specific training cards,
 then have the cooldown cards, finally, they shall end in savasanas.

Main body Written by Niko Vainio,
Edited by Sebastian Acosta.

"""

# Importing modules first.
import random
from pygame.locals import *
import Cards1

# Function training_program() will be called by the main program.
def training_program(length, training_type):
    # Dictionary with list. A string counts as key to list values.
    # After the lists are chosen, randomly picks numbers from list later.
    
    decks= {
        "warmup": [0, 1, 2, 3, 4], 

        "strength": [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 
                    15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],

        "flexibility": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 
                    36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 
                    46, 47, 48, 49, 50],

        "balance": [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 
                    61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 
                    71, 72, 73, 74, 75],

        "relaxation": [76, 77, 78, 79, 80, 81, 82, 83, 84, 85,
                  86, 87, 88, 89, 90],

        "cooldown": [91, 92, 93, 94, 95, 96, 97, 98, 99, 100],

        "savasana": [101]
        }

    choices = ["1", "2", "3", "4"]

    # training() is called by the x (training type) variable, 
    # it then creates the training by organizing the cards in the correct order, 
    # taking random samples of the desired deck.

    # The y variable determines how many cards will be taken, 
    # hence it determines the duration of the training.

    # The decks give the numbers of the cards that will be used for the training.

    # Decks keywords =  warmup, deck is defined below (deck1 (strenght), 
    # deck2 (flexibility), deck3 (relaxation), deck4 (balance)), cooldown, savasana).

    def training(y, warmup, deck, cooldown, savasana):
        if y == "option1":
            training = (random.sample(warmup, 1) + random.sample(deck, 3) + 
            random.sample(cooldown, 1)) + savasana
            
            return training

        if y == "option2":
            training = (random.sample(warmup, 4) + random.sample(deck, 4) + 
            random.sample(cooldown, 2)) + savasana
            
            return training

        if y == "option3":
            training = (random.sample(warmup, 5) + random.sample(deck, 5) + 
            random.sample(cooldown, 5)) + savasana
            
            return training

    # This function is specifically created for the balance training option to work. 
    # Otherwise it works similarly to training().
    def mixed_deck(y, warmup, decks, cooldown, savasana):        
        if y == "option1":
            training = (random.sample(warmup, 1) + random.sample(decks[0], 1) + 
            random.sample(decks[1], 1) + random.sample(decks[2], 1) + 
            random.sample(cooldown, 1)) + savasana
            
            return training

        if y == "option2":
            training = (random.sample(warmup, 4) + random.sample(decks[0], 1) + 
            random.sample(decks[1], 1) + random.sample(decks[2], 2) + 
            random.sample(cooldown, 2)) + savasana
            
            return training

        if y == "option3":
            training = (random.sample(warmup, 4) + random.sample(decks[0], 2) + 
            random.sample(decks[1], 1) + random.sample(decks[2], 2) + 
            random.sample(cooldown, 5)) + savasana
            
            return training
            
    # This data is inputted in the main program. 
    y = length
    x = training_type

    #Variable names:
    warmup = decks["warmup"]
    deck_1 = decks["strength"]
    deck_2 = decks["flexibility"]
    deck_3 = decks["relaxation"]
    deck_4 = decks["balance"]
    cooldown = decks["cooldown"]
    savasana = decks["savasana"]

    # Depending on options chosen, calls training() or mixed_deck() with different values.
    if x == "option1":
        print("strenght")
        return training(y, warmup, deck_1, cooldown, savasana)    

    elif x == "option2":
        print("flexibility")
        return training(y, warmup, deck_2, cooldown, savasana)

    elif x == "option3":
        print("relaxation")
        return training(y, warmup, deck_3, cooldown, savasana)

    elif x == "option4":
        print("balance")
        return mixed_deck(y, warmup, [deck_1, deck_2, deck_3], cooldown, savasana)


# Next line is for testing purposes.
#training_program(input("short = option1\nmedium = option2\nlong = option3\nChoose length :"), input("str = option1\nflex = option2\nrelax = option3\nbalance = option4\nChoose your training: "))


    






