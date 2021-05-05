import random

# TITLE: Data Types

# TODO: Define a dictionary with some key value pairs of your choice. Print a value by using
# TODO: its key in a readable string.

# TODO: Define a list with some items of your choice. Print an item by using
# TODO: it's index position in a readable string.

####################################################################################################

# TITLE: Conditions

# TODO: Write a condition to check if this variable is a string. If it is true, print "string here"
type_test = "i am a string"

# TODO: Write a condition to check if this is an even number AND the number is two, if it is print
# TODO: "this is even AND two". If the number is even and not two, print "this is just even".
# TODO: If neither of those conditions is true, print "this is an odd number".

# TIP: Test your code by first keeping this variable set to 2.
# TIP: Then change the variable to 4 and 7 in that order.
num_check = 2

####################################################################################################

# TITLE: Basic Loops

# TODO: Solve the FizzBuzz problem.
# Below is 10 random numbers between 0 and 100. Iterate over each number. If the number is
# divisible by 3, print "fizz". If the number is divisible by 5, print "buzz". If the number
# is divisible by both 3 and 5, print ONLY "fizzbuzz".

nums = [random.randrange(0, 100) for n in range(10)]

# TODO: Add the numbers 1 through 100 to a single integer. Print out that integer.

####################################################################################################

# TITLE: Nested Data
# These data structures can be used together to create complex data sets.
# Below is an example of a dictionary holding multiple dictionaries and lists.

# This is what spread data set would look like with correct tabulation.
# If something is nested, it should be tabbed once from the original position.
bobs_burgers = {
  "season 1": {
    "episode 1": {
      "cast": [
        "H. Jon Benjamin",
        "Kristen Schall",
        "Dan Mintz"
      ],
      "title": "Food Truckin",
      "run time": "30"
    },
    "episode 2": {
      "cast": [
        "H. Jon Benjamin",
        "Kristen Schall",
        "Dan Mintz"
      ],
      "title": "Out of Burgers",
      "run time": "29.30"
    }
  },
  "season 2": {
    "episode 1": {
      "cast":[
        "H. Jon Benjamin",
        "Kristen Schall",
        "Dan Mintz"
      ],
      "title": "Sheesh! Cab, Bob?",
      "run time": "28.42"
    },
    "episode 2": {
      "cast": [
        "H. Jon Benjamin",
        "Kristen Schall",
        "Dan Mintz"
      ],
      "title": "Buns City",
      "run time": "29.15"
    }
  }
}

# TODO: Calculate the average runtime of the episodes in our nested data

# TODO: Output a single string of every episode in the format of:
# "[Episode One Name] + [Episode Two Name] ... [Last Episode Name]"

####################################################################################################

# TITLE: Functions

# TODO: Define a function called "wordy" that takes a string & returns 'yell', 'whisper' or 'words'
# If the word is all caps it should return "yell", if it is all lowercase it should return "whisper",
# and if it is neither all caps nor all lowercase it should return "words".

yelling = 'AHHHHH'
whispering = 'shhhh'
words = 'Whats up?'

print(wordy(yelling)) # should print "yell"
print(wordy(whispering)) # should print "whisper"
print(wordy(words)) # should print "words"

####################################################################################################

# TITLE: Classes

# TODO: Define a class of PIN. This class should have attributes and methods as the following:
class PIN:
  """
  Class Attribute:
  'organization_type' should be set to 'nonprofit'.
  Instance Attributes:
  'purpose' should be a short string describing the purpose of PIN.
  'board_members' should contain names of people on the board of directors.
  'years_old' should be an integer containing how many years PIN has been active for.

  Methods:
  'describe' should output all of the attributes in a readable way of your choice.
  'age_pin' should increment the years_old attribute by one.
  'add_member' should prompt the user to input a first/last name and add that name to the board.
  """

# TITLE: Inheritance

# TODO: Define a class of PINProgram. This class should inherit the PIN class and add some
# TODO: additional functionality.

# A PINProgram should have attributes of 'name', 'program_coordinator', and 'schools'.

# A PINProgram should have methods of 'change_coordinator', 'add_school', and 'remove_school'.
# 'add_school' should inquire the user for the school's name.
# 'remove_school' should list the schools the program currently has along with a
# number (ie 1: Northstar, 2: East Side...) and the user should input the number of the school
# they would like to remove.