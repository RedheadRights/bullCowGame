# Justin Plane
#This is a game called Bulls and Cows
# Last Edited: 9/14/18

import time
import sys

# Declares Variables
bulls = int(0)
cows = int(0)
tries = int(0)
word = str('')
guessCount = int(0)
NUMBER_OF_GUESSES = int(0)
NUMBER_OF_LETTERS = int(0)

# Defines methods
def fancyText(statement):
    for letter in statement:
        sys.stdout.write(letter)
        time.sleep(.020)
        reload(bullCowGame.py)
    print(' ')
    time.sleep(.5)

# Intro to player
welcome = str("Welcome to Bulls and Cows, a fun word game!")
goal = str("Your goal as the player is to guess the word I'm thinking of.")
youWill = str("You will have 6 guesses to figure it out... with a catch.")
bull = str("Bulls are the correct letter in the correct order.")
cow = str("Cows are the correct letter in the wrong order.")
iWill = str("I will tell you how many bulls and cows you have after each guess.")

fancyText(welcome)
fancyText(goal)
fancyText(youWill)
fancyText(bull)
fancyText(cow)
fancyText(iWill)
print()
fancyText("Good Luck!")
input("Press enter to start")

# Game code starts here





