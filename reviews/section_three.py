import random

# TITLE: Loops

# TODO:  Solve the FizzBuzz problem.
# Below is 10 random numbers between 0 and 100. Iterate over each number. If the number is
# divisible by 3, print "fizz". If the number is divisible by 5, print "buzz". If the number
# is divisible by both 3 and 5, print ONLY "fizzbuzz".

nums = [random.randrange(0, 100) for n in range(10)]

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
# TODO: "[Episode One Name] + [Episode Two Name] ... [Last Episode Name]"

# TITLE: Classes

# TODO: Define a class of PIN. This class should have attributes and methods as the following:
class PIN:
  """
  Attributes:
  'purpose' should be a short string describing the purpose of PIN.
  'board_members' should contain names of people on the board of directors.
  'years_old' should be an integer containing how many years PIN has been active for.

  Methods:
  'describe' should output all of the attributes in a readable way of your choice.
  'age_pin' should increment the years_old attribute by one.
  'add_member' should prompt the user to input a first/last name and add that name to the board.
  """

# TODO: Define a class of PINProgram. This class should inherit the PIN class and add some
# TODO: additional functionality.

# A PINProgram should have attributes of 'name', 'program_coordinator', and 'schools'.

# A PINProgram should have methods of 'change_coordinator', 'add_school', and 'remove_school'.
# 'add_school' should inquire the user for the school's name.
# 'remove_school' should list the schools the program currently has along with a
# number (ie 1: Northstar, 2: East Side...) and the user should input the number of the school
# they would like to remove.