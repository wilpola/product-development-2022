"""beginner = [1, 2, 3, 4, 5]
intermediate = beginner + [6, 7, 8, 9, 10]
advanced = intermediate + [11, 12, 13, 14, 15]

print(beginner)
print(intermediate)
print(advanced)
"""
#class randomizer1:
 #   def __init__(self, length, training_type):
  #      self.length = length
   #     self.training_type = training_type

def training_program(length, training_type):
    # Dictionary with list. A string counts as key to list values.
    # After the lists are chosen, randomly picks numbers from list later
    
    import random
    fancy_moves = {
        "warmup": [1, 2, 3, 4, 5], 
        "strength": [6, 7, 8, 9, 10],
        "flexibility": [11, 12, 13, 14, 15],
        "relaxation": [16, 17, 18, 19, 20],
        "cooldown": [21, 22, 23, 24, 25]
        }
    choises = ["1", "2", "3"]

    def training(y, z, z2, z3):
        # Takes in chosen options, and picks random numbers based on those options

        #print(z, z2, z3)
        if y == "option1":
            harkka = (random.sample(z, 1) + random.sample(z2, 3) + random.sample(z3, 1))
            #print(harkka)
            return harkka

        if y == "option2":
            harkka = (random.sample(z, 4) + random.sample(z2, 4) + random.sample(z3, 2))
            #print(harkka)
            return harkka


        if y == "option3":
            harkka = (random.sample(z, 5) + random.sample(z2, 5) + random.sample(z3, 5))
            #print(harkka)
            return harkka


        
    y = length
    x = training_type

    z = fancy_moves["warmup"]
    z2_1 = fancy_moves["strength"]
    z2_2 = fancy_moves["flexibility"]
    z2_3 = fancy_moves["relaxation"]
    z3 = fancy_moves["cooldown"]

    # Depending on options chosen, calls training() with different values
    
    if x == "option1":
        print("str")
        return training(y, z, z2_1, z3)    
    elif x == "option2":
        print("flex")
        return training(y, z, z2_2, z3)
    elif x == "option3":
        print("relax")
        return training(y, z, z2_3, z3)







