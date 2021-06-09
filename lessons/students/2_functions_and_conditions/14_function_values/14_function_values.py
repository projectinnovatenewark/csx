""" 
In this lesson, we will go over some more function work as well as using a 
functions return value in other functions.
"""

# TITLE: Section 1 - Reviewing Return Values

# To begin, let's review a concept from lesson 6: the ".pop()" method. The ".pop()" method is a
# built-in Python method that is used to remove elements from a list and return that element.
# After returning the element, you can also store it in a variable to be used later.
# TIP: Remember that the ".pop()" method will remove the last item in the list by default unless an
# TIP: index is passed as an argument.

teams = ["New York Liberty", "Chicago Sky", "Atlanta Dream"]
popped_team = teams.pop() # This removes the last item in the list and stores it in "popped_team".
print(popped_team)

# Similar to the example above, using a "return" statement in custom Python functions allows you to
# access the value of the executed function. Below is a simple example to jog your memory from
# Lesson 11:

def addTwo(num):
  num += 2
  return num # This is a "return" statement.

num_plus_two = addTwo(20) # Just as when using the ".pop()" method, the value of "addTwo()" will be
                          # stored in the variable "num_plus_two".
print(num_plus_two)

####################################################################################################

# TITLE: Section 2 - Using Custom Functions Together

# Creating one large function often does not produce the most readable code. Therefore, it is
# considered best practice to break the function up into smaller, "helper" functions. Let's walk
# through this concept using the control of the functions below.

# TODO: Hey Teacher, walk through the control with the class starting at "Control 1" marked by the
# TODO: "TODO" tag.

def inputWidth():
  # Control 3: Use the built in "input()" function to get the width from the user and return it.
  width = float(input("Please enter the width of your rectangle (Only input a float or integer): "))
  return width

def inputLength():
  # Control 5: Use the built in "input()" function to get the length from the user and return it.
  length = float(input("Please enter the length of your rectangle (Only input a float or integer): "))
  return length

def findArea():
  width = inputWidth() # Control 2: Call "inputWidth()" and store its value in the variable "width"
  length = inputLength() # Control 4: Call "inputWidth()" and store its value in the variable
                         # "length"

  area = width * length # Control 6: Calculate the area using the return values stored in "width"
                        # and "length"

  return area # Return "area" to be used later in the program.

# TODO: Start walking through the control on the line below.
rectangle_area = findArea() # Control 1: Call "findArea()" and store its value in the variable
                            # "rectangle_area".

print(f"The area of your rectangle is {rectangle_area} feet.")

###################################################################################################

# TITLE: Section 3 - Functions and Loops

# Let's develop a small program using multiple functions to create a game where a user guesses a
# number between one and ten. The program should then let the user input how many times they want to
# play the game and tell them whether they have won or lost after each round.

# The game will use the "random" package to produce a random number that the user is trying to
# guess, as seen below.

from random import randint # Remember import statements generally belong at the top of a file.

def inquireUserGames():
  """Ask a user how many times they want to play."""

  num_games = int(input("How many times would you like to play the 'Guess the Number' game?: "))
  num_games_string = f"You've signed on to play {num_games} games."

  return num_games, num_games_string # Just as you can define multiple variables at once, you can
                                     # also return multiple values from a single function.

def playTheGame():
  """Ask the user for a number between 1 and 10, generate a random number between 1 and 10, and
    check if those numbers match. If they do, congratulate the user! If not, tell them they were
    incorrect."""

  random_number = randint(1, 10) # Generate a random number between 1 and 10.
  
  user_guess = int(input("Guess a number between 1 and 10: "))

  # Check if the random number and user number equal each other.
  if random_number == user_guess:
    print(f"You guessed correctly. Number {user_guess} is correct.\n")
  else:
    print(f"Your guess is incorrect! Number {random_number} doesnt equal {user_guess}.\n")

def initializeGame():
  """Lets initialize our game and call the inquireUserGames function."""

  # Recall that in the function "inquireUserGames()" will return 2 values. We use a comma to
  # separate the returned values when storing them into variables.
  game_count, welcome_string = inquireUserGames()
  print(f"\n{welcome_string}\n")

  # The variable "game_count" will equal the user's input for their desired number of games to
  # play. The variable "welcome_string" will equal the output "You've signed on to play
  # {game_count} games!"
  while game_count: # This while loop will continue to run until "game_count" equals zero.
    playTheGame()
    # Every time we run the "playTheGame()" function we want to decrement the game_count
    # by one until it hits zero, at which point the while loop will stop running.
    game_count -= 1

initializeGame()

# TODO: Complete TODO 14 (10 min for students, 5 min for demo)
