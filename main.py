# trying out loops and general program execution stuff
# I'm also gonna try importing some modules and use other than really basic functions here

import random
import sys

x = 0

while x < 5:
    print("This statement will be visible 5 times")
    x = x + 1

x = 5

while x > 1:
    print("This statement will be visible " + str(x) + " more times")
    x = x - 1
else:
    print("This statement will be visible " + str(x) + " more time")

# now let's try a basic game of rock, paper and scissors
# first, I read online that there is a random number generator module.
# trying to write it myself first, and then comparing it to an example source code.

x = 0  # reusing my variable

# decided to use a table here to represent all the different choices

weapon = ['Rock', 'Paper', 'Scissors']

playerWeapon = "N"

while True:  # endless loop of gameplay
    x = random.randint(1, 3)  # randomise a number that represents any of the three outcomes
    print("Choose your weapon: ")
    print("(R)ock, (P)aper, (S)cissors, (Q)uit")
    playerWeapon = input()
    if playerWeapon == "Q":
        sys.exit()  # terminates the program entirely
    elif playerWeapon == "R" and x == 1:
        print("Rock versus rock.. it's a TIE!")
    elif playerWeapon == "R" and x == 2:
        print("Rock versus paper... YOU LOST!")
    elif playerWeapon == "R" and x == 3:
        print("Rock versus scissors... You WON!")
    elif playerWeapon == "P" and x == 1:
        print("Paper versus rock.. You WON!")
    elif playerWeapon == "P" and x == 2:
        print("Rock versus paper... it's a TIE!")
    elif playerWeapon == "P" and x == 3:
        print("Paper versus scissors... You LOST!")
    elif playerWeapon == "S" and x == 1:
        print("Scissors versus rock.. You LOST!")
    elif playerWeapon == "S" and x == 2:
        print("Scissors versus paper... You WON!")
    elif playerWeapon == "S" and x == 3:
        print("Scissors versus scissors... it's a TIE!")

# okay so this works but it's a bit messy.. That's quite a lot of code for something that should be relatively simple.
# It's 2AM so I'm not in the mood for trying anything else right now but that's about as much as I can do today without falling asleep.
# TODO: Tie both weapons to numbers; check for a win/lose/tie condition based upon that
# TODO: score tracking
