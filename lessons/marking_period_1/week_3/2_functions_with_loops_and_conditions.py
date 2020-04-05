"""
Here we will show a couple of examples of functions that use loops and conditionals
"""

unsorted_num_list = [10, 22, 8, 15, 7, 18, 3]

# Here is a long way to create a function and solve the problem above by sorting thec

# unsorted_num_list and putting the sorted items in a new list.
def sort_a_list(data_list):
    new_list = []

    # FIXME: INCLUDE A LOGIC MODEL FOR THIS.
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

##################################################################################################

# lets try a for loop within a for loop. we want the outputs to be "red cherry",
# "big coconut", and "tasty mango".

adjective = ["red", "big", "tasty"]
fruits = ["cherry", "coconut", "mango"]

for word in adjective:
    for fruit in fruits:
        print(word, fruit)

# TODO: Oops! That doesnt give us exactly what we expected! let's change the adjective and fruit
# TODO: lists to a single dictionary and get the desired outcome.

# TODO: Switch the above data sets to a dictionary and change the loop to achieve your
# TODO: desired outcome.

##################################################################################################

# Lets develop a small program using multiple functions to create a game. A user will input how
# many times they want to play the game. The game is to guess a number between one and ten.
# If they guess the number correctly, the program should tell the user they won. If they guess
# incorrectly, it should tell them they were wrong.

# Python has some pre-defined packages you can import functions from. We will explore this more in-
# depth later in the course. The "random" package has a function used to generate a random integer.
from random import randint

def inquireUserGames():
    """ask a user how many times they want to play"""
    timesToPlay = input("How many times would you like to play the 'Guess the Number' game?: ")
    numTimesToPlay = int(timesToPlay)
    userStartedGameString = "You've signed on to play {} games!".format(timesToPlay)
    # Let's return TWO variables to display some cool Python functionality. We can now
    # set two variables equal to the value of calling this function.
    return numTimesToPlay, userStartedGameString

def playTheGame():
    """ask user for a number between 1 and 10, generate a random number between 1 and 10, then see
    if those numbers match. If they do, congratulate the user! If not, tell 'em they guess wrong"""

    # Generate a random number between 1 and 10
    randomNumber = randint(1, 10)
    # Get an input from the user
    promptUserForNumber = input("Guess a number between 1 and 10: ")
    # Convert their input into an integer so you can check for equality between
    # the input and the random number generated
    userNumber = int(promptUserForNumber)

    # Check if the random number and user number equal each other
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

##################################################################################################

# below we want to iterate through a list of lists using a nested for loop,
# or in simpler terms a for loop within a for loop. this is very common
# in data structures and you will master this in no time! The first sublist in
# my_shows would be the entire list of ['How I Met Your Mother', 'Friends', 'Silicon Valley']
# Then, second for loop of "for show_name in sublist:" would iterate through each of those
# items in the list. Once the second for loop is completed, the program will return to the first
# for loop and move on to the second list of ['Family Guy', 'South Park', 'Rick and Morty'] and
# repeat the second for loop for that list's items.

my_shows = [
    ['How I Met Your Mother', 'Friends', 'Silicon Valley'],
    ['Family Guy', 'South Park', 'Rick and Morty'],
    ['Breaking Bad', 'Game of Thrones', 'The Wire']
]

for sublist in my_shows:
    for show_name in sublist:
        char_num = len(show_name)
        print("The title " + show_name + " is " + str(char_num) + " characters long.")

##################################################################################################

# below we want to iterate through a dictionary of key value pairs- where the values are
# dictionaries! We wil again use a nested for loop here. Here we have the first six
# episodes from the first three seasons each in the show, The Office.

the_office = {
    "Season 1":
    {
        "Episode 1" : "Pilot",
        "Episode 2" : "Diversity Day",
        "Episode 3" : "Health Care",
        "Episode 4" : "The Alliance",
        "Episode 5" : "Basketball",
        "Episode 6" : "Hot Girl",
    },
    "Season 2":
    {
        "Episode 1" : "The Dundies",
        "Episode 2" : "Sexual Harassment",
        "Episode 3" : "Office Olympics",
        "Episode 4" : "The Fire",
        "Episode 5" : "Halloween",
        "Episode 6" : "The Fight",
    },
    "Season 3":
    {
        "Episode 1" : "Gay Witch Hunt",
        "Episode 2" : "The Convention",
        "Episode 3" : "The Coup",
        "Episode 4" : "Grief Counseling",
        "Episode 5" : "Initiation",
        "Episode 6" : "Diwali",
    },
}

# for example, to find the title of episode 1 in season 3, you would use this:
# print(the_office["Season 3"]["Episode 1"])

# TODO: Question 1: What type of data set is the_office? Is it a list, dictionary, string, etc.?

# TODO: Question 2: Find the value of 'Season 3'. Print it. Now Print out 'Episode 6' in Season 3.

# TODO: Question 3: Loop through the the_office object and print out the value of each key.

# let's remember something when using a nested for loop here. The first iteration of our
# top level for loop would be "Season 1" since it is the first key in our dictionary. You
# might want to set a variable between the top level for loop and the nested loop. Remember,
# if the iteration of each loop is a key, that variable you'd set between loops should follow
# the format of variableName = dictionaryName[keyName]. Then, you can iterate through that new
# variable, since it should equal the value of the key which is a dictionary.
# TODO: Question 4: Create a nested for loop that would list an output for each episode
# TODO: that would state "Episode __ of Season __ is titled '____' "

##################################################################################################

# Lets try looping through a different nested data structure. Imagine having a set of classes
# in a list. However, each class would be an object with info like subject, level, teacher,
# students, and average quarterly grades. Following the data set, we will show a couple examples
# of how to use it.

math_classes = [
    {
        'subject': 'Math',
        'level': 'Geometry',
        'teacher': 'Professor Alisson',
        'students': ['Bill', 'Bob', 'Beatrice', 'Brandi'],
        'averages': {
            'MP1': 89.5,
            'MP2': 82,
            'MP3': 92,
            'MP4': 94,
        }
    },
    {
        'subject': 'Math',
        'level': 'Algebra',
        'teacher': 'Professor Dylan',
        'students': ['Callie', 'Chris', 'Cayla', 'Chantelle'],
        'averages': {
            'MP1': 95,
            'MP2': 86,
            'MP3': 97,
            'MP4': 79,
        }
    },
    {
        'subject': 'Math',
        'level': 'Calculus',
        'teacher': 'Professor Johnson',
        'students': ['Dani', 'Damien', 'Dinesh', 'Dira'],
        'averages': {
            'MP1': 99,
            'MP2': 86,
            'MP3': 77,
            'MP4': 94.8,
        }
    },
]

# for example, to find the value of MP4 in the Calculus level math class, I would run
# print(math_classes[3]['averages]['MP4])

# TODO: Question 1: What type of data set is classes? Is it a list, dictionary, string, etc.?

# TODO: Question 2:   How would I find the entire dictionary for the calculus course?
# TODO: Question 2: How would I find the 2nd student in the list of students from the Algebra class?

# TODO: Question 3: How would I find the MP4 grade from the calculus class?

# TODO: Question 4: How would I print each student's name from all of the classes?

# TODO: Question 5: How could I modify the above to print a statement for each student to say
# TODO: 'Teacher ____ teaches subject _____ to ______'

# TODO: Question 6: How could I find yearly grades average between marking periods for each class?
# TODO: for example, I would want all of the averages added up for each course, then divided by the
# TODO: number of marking periods to determine the average yearly grade for the course.
        