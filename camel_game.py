# -*- coding: utf-8 -*-

import random 

# camel game 
""" Welcome Message & Intro """
print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down! Survive your")
print("desert trek and out run the natives.")

""" Constants & Variables """
done = False
miles_traveled = 0
thirst = 0
camel_tiredness = 0
native_dist = 20
canteen_drinks = 5

""" Decision Menu """
print("")
while not done:     
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")
    print("")
    user_choice = input("Your Choice? ")
    user_choice = user_choice.upper()
    if user_choice == 'Q':
        done = True
    elif user_choice == 'E':
        print("Miles traveled: ", miles_traveled)
        print("Drinks in canteen: ", canteen_drinks)
        print("The natives are", native_dist, "miles behind you.\n")
    elif user_choice == 'D':
        print("Your camel is rested.")
        camel_tiredness = 0
        native_dist -= random.randrange(7,15)
        print("The natives are", native_dist, "miles behind you.\n")
    elif user_choice == 'C':
        miles = random.randrange(10,21)
        print("You traveled", miles, "miles.")
        miles_traveled += miles
        thirst += 1
        camel_tiredness += random.randrange(1,4)
        native_dist -= random.randrange(7,15)
        native_dist += miles
        print("The natives are",native_dist, "miles behind you.\n")
    elif user_choice == 'B':
        miles = random.randrange(5,13)
        print("You traveled", miles, "miles.")
        thirst += 1
        camel_tiredness += 1
        native_dist -= random.randrange(7,15)
        native_dist += miles
        print("The natives are",native_dist, "miles behind you.\n")
    elif user_choice == 'A':
        if canteen_drinks > 0:
            canteen_drinks -= 1
            thirst = 0
            print("You drink from your canteen.\n")
        else:
            print("Your canteen is empty!\n")
    if thirst > 3 and thirst < 6:
        print("You're thirsty.\n")
    if thirst >= 6:
        print("You died of thirst!")
        done = True
    if camel_tiredness >= 5 and camel_tiredness < 8:
        print("Your camel is getting tired.\n")
    if camel_tiredness >= 8:
        print("Your camel has died!\n")
        done = True
    if native_dist <= 0:
        print("The natives have caught you!")
        done = True
    if native_dist < 16:
        print("The natives are getting close!\n")
    if miles_traveled >= 200:
        print("You made it across the desert!")
        done = True
    if random.randrange(20) == 19:
        print("You found an Oasis!")
        print("You fill your canteen.")
        print("you rest your camel.\n")
        canteen_drinks = 5
        camel_tiredness = 0