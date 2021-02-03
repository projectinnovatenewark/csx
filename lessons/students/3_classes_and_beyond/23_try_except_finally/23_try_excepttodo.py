"""
Modify the example from week 3 lesson 3's game function
"""

# This example is from a previous lesson. We want it to ask a user how many times they want
# to play the game, play the game that many times, and tell them when they guess correctly
# along the way. One thing though- the example from the lessons doesn't account for if a user
# inputs something thats NaN (not a number). Implement a try-except to address if the user
# gets a ValueError from entering a non-number. This should probably happen in the inquireUserGames
# function as well as the playTheGame function to ensure that any time a user input is made,
# your function can account for non-number entries. You may use either a try-except-finally
# or a try-except-else to work through the solution.

# Original Lesson Solution:
from random import randint

def inquireUserGames():
    """ask a user how many times they want to play"""
    timesToPlay = input("How many times would you like to play the 'Guess the Number' game?: ")
    numTimesToPlay = int(timesToPlay)
    userStartedGameString = "You've signed on to play {} games!".format(timesToPlay)

    return numTimesToPlay, userStartedGameString

def playTheGame():
    """ask user for a number between 1 and 10, generate a random number between 1 and 10, then see
    if those numbers match. If they do, congratulate the user! If not, tell 'em they guess wrong"""

    randomNumber = randint(1, 10)
    promptUserForNumber = input("Guess a number between 1 and 10: ")
    userNumber = int(promptUserForNumber)

    if (randomNumber == userNumber):
        print("You guessed correctly! Number", userNumber, "was the correct guess.", "\n")
    else:
        print("Wrong Answer!!! Number", randomNumber, "doesnt equal", userNumber, "\n")

def initializeGame():
    """Lets initialize our game and call the inquireUserGames function."""

    userGameCount, userWelcomeString = inquireUserGames()
    print("\n", userWelcomeString, "\n")

    while userGameCount:
        playTheGame()
        userGameCount -= 1

initializeGame()
