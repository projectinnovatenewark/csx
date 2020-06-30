""" 
In this lesson, we will go over some more function work as well as using a 
funcitons return value in other functions
"""

# Let's walk through how to use functions and return values with one another. We will
# write a program that specifies what type of pizza pie a user wants with separate functions
# for each of the following. One function should ask a user what size they want and only
# accept small, medium, or large. Another function should ask about toppings, but tell the
# user they don't have pepperoni (if they ask for pepperoni). Our last function should confirm
# the order with the user.

def sizeInquiry():
    """Ask a user what size pizza they want and return it if it is a valid response"""
    sizeOfPie = input("What size pie do you want? (small, medium, or large): ")
    acceptableInputs = ["small", "medium", "large"]
    if (sizeOfPie not in acceptableInputs):
        print("Try again and enter a valid pizza size.")
        return False
    else:
        return sizeOfPie

def toppingsInquiry():
    """Ask a user what toppings they want- make sure to let them know we dont have pepperoni if they ask!"""
    toppings = input("What toppings would you like to have with your pizza?: (separate your toppings with commas and no spaces in between) ")
    # Lets split the user's string into separate items in a list. We want to make sure they didnt try to order pepperoni!
    listOfToppings = toppings.split(",")

    if ("pepperoni" in listOfToppings):
        followUp = input("Sorry dog, we don't have pepperoni. Do you want to change your order? (y/n) ")
        if (followUp == "y"):
            return False
        if (followUp == "n"):
            listOfToppings.remove("pepperoni")
            toppingsString = ", ".join(listOfToppings)
            return toppingsString
    else:
        return toppings

def formatOrder(s, t):
    """Create a basic formatted string to output to our user"""
    userMessage = f"Your order is for a {s} pizza with {t}"
    return userMessage

def main():
    """Guide a user through ordering a pizza"""

    # The return value of a function call can be set equal to a variable.
    size = sizeInquiry()
    if (size is False):
        # If the input value was incorrect and returned False, then we want to return a main function call to start over.
        return main()

    toppings = toppingsInquiry()
    if (toppings is False):
        # If the input value was incorrect and returned False, then we want to return a main function call to start over.
        return main()

    message = formatOrder(size, toppings)
    print(message)

main()

####################################################################################################

unsorted_num_list = [10, 22, 8, 15, 7, 18, 3]

# Here is a long way to create a function and solve the problem above by sorting them.

# unsorted_num_list and putting the sorted items in a new list.
def sort_a_list(data_list):
    """
    This function removes the minimum of out input list, in this case it is 
    'unsorted_num_list' and appends it, (inserts at the 0 index position), 
    to the new list. This is used to sort the integers in the original list into a new list.
    """
    new_list = []

    while data_list:
        minimum = data_list[0]  # arbitrary number in list
        for x in data_list:
            print('x: ', x, 'minimum: ', minimum)
            if x < minimum:
                print('X is less than MIN. x: ', x, 'minimum: ', minimum)
                minimum = x
        new_list.append(minimum)
        data_list.remove(minimum)
        print('End while loop iteration. new_list: ', new_list, 'data_list: ', data_list)

    print(new_list)

sort_a_list(unsorted_num_list)

# This function does the same thing as the function above function.

# An important lesson about becoming a programmer is that you must understand underlying concepts.
# There's always tools to solve your problem quickly with imported functions, but what matters
# is that you understand how those functions work!
print(sorted(unsorted_num_list))

####################################################################################################

# Lets develop a small program using multiple functions to create a game. A user will input how
# many times they want to play the game. The game is to guess a number between one and ten.
# If they guess the number correctly, the program should tell the user they won. If they guess
# incorrectly, it should tell them they were wrong.

# Python has some pre-defined packages you can import functions from. We will explore this more in-
# depth later in the course. The "random" package has a function used to generate a random integer.

from random import randint # Remember import statements generally belong at the top of a file.

def inquireUserGames():
    """ask a user how many times they want to play"""
    timesToPlay = input("How many times would you like to play the 'Guess the Number' game?: ")
    numTimesToPlay = int(timesToPlay)
    userStartedGameString = f"You've signed on to play {timesToPlay} games!"
    # Let's return TWO variables to display some cool Python functionality. We can now
    # set two variables equal to the value of calling this function.
    return numTimesToPlay, userStartedGameString

def playTheGame():
    """ask user for a number between 1 and 10, generate a random number between 1 and 10, then see
    if those numbers match. If they do, congratulate the user! If not, tell 'em they guess wrong."""

    # Generate a random number between 1 and 10.
    randomNumber = randint(1, 10)
    # Get an input from the user.
    promptUserForNumber = input("Guess a number between 1 and 10: ")
    # Convert their input into an integer so you can check for equality between
    # the input and the random number generated.
    userNumber = int(promptUserForNumber)

    # Check if the random number and user number equal each other.
    if (randomNumber == userNumber):
        print("You guessed correctly! Number", userNumber, "was the correct guess.", "\n")
    else:
        print("Wrong Answer!!! Number", randomNumber, "doesnt equal", userNumber, "\n")

def initializeGame():
    """Lets initialize our game and call the inquireUserGames function."""
    # The first variable will equal the first returned value, and the second variable
    # will equal the second returned value.
    userGameCount, userWelcomeString = inquireUserGames()
    print("\n", userWelcomeString, "\n")

    # userGameCount will equal the user's input from their desired number of games to play.
    # This while loop will continue to run until userGameCount equals zero.
    while userGameCount:
        playTheGame()
        # Every time we run the playTheGame function we want to decrement the userGameCount
        # by one until it hits zero, at which point the while loop will stop running.
        userGameCount -= 1

# Lets call the initializeGame function to get things going!
initializeGame()

# TODO: Complete 2_funcs_with_loops_and_conditionstodo1