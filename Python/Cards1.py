"""
Module for the cards to be created.

Keywords:
    mirrored = The card has a movement that needs to be done once for the
    right side and once for the left.
    follower = The card follows another card.
    conflictive = The card has other cards that must NOT follow it.
    front = the front face of the card, which will have the picture.
    back = the back face of the card, which will have the instructions.

If the card is mirrored it will show twice, mirrored.
If a card must be followed by another card, set it so with the followed
attribute.

Cards will be arranged in decks and shuffled by the randomizer, and 
then showed by the main program.

Code written by Sebastian Acosta.
"""

# Importing modules first.
import random

# The class is created, with the attributes defined in it.
class Card:

    def __init__(self, mirrored = False, follower = False, 
                 conflictive = False, front = True):
        self.value = 0
        self.face = "Add picture url"
        self.back = "Add card description"
        self.mirrored = mirrored
        self.follower = follower
        self.conflictive = conflictive
        self.front = front

        # We put what the attributes mean for the program.
        if self.mirrored == True:
            pass                        # The card has to be shown twice, take two spots in the 
                                        # randomizer and the picture is showed mirrored.
        else:
            pass

        if self.follower == True:
            pass                    #The program needs to set that this card always comes 
                                    # after the cards that this card follows.
        else: 
            pass

        if self.conflictive == True:
            pass                    #The program needs to make sure the conflicting cards won't 
                                    # follow each other.
        else:
            pass

        if self.front == True:
            self.show= self.face
        else: 
            self.show = self.back


        # Now we program the tasks the cards need to complete.

        # For example, they have to get flipped if the 
        #  User press on them to see the back of the card.
        def turn(self):
            if front == True:
                front = False
            else:
                front = True


        # Now we do all the cards, I have to learn yet if 
        #  this is the best way of creating them.
        # The idea is that each card has their set of attributes
        #  and all of them are easy to call.

card0 = Card()

card0.value = 0
card0.face = "This is where the url for the first warm up card should come."
card0.back = "This is the description for the first warm up card."

card1 = Card()

card1.value = 1
card1.face = "This is where the url for the second warm up card should come."
card1.back = "This is the description for the second warm up card."

test_deck = [card0, card1]

for card in test_deck:
    arguments = [card, card.value, card.front, card.mirrored, card.follower, card.conflictive, card.face, card.back]
    string = "{} - value {}, front: {}, mirrored: {}, follower: {}, conflictive: {}, face: {}, back: {}.".format(*arguments)

    print (string)
