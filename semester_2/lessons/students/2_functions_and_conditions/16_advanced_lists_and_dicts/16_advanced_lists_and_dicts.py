"""
In this lesson, we will go over using functions to perform actions on lists and dictionaries as well
as more advanced methods on lists and dictionaries.
"""

# TITLE: Section 1 - List and Dictionary Constructors

# In Python, you can convert iterable objects into lists by using a list constructor. The syntax
# for using a list contructor is "list(iterable_object)". The new list can then be stored in a
# variable and act just as if the object was originally defined as a list with brackets. Below is an
# example of using the list contructor.

stringy = 'racecar'
print(f"stringy: '{stringy}', type: {type(stringy)}")

listy = list(stringy) # This converts 'stringy' to a list.
print(f"listy: {listy}, type: {type(listy)}")

# You can create a dictionary using keyword arguments in Python with a dictionary constructor. A
# "keyword arguement" is a way to define key/value pairs as an argument when executing a function or
# method call. The syntax for using "dict()" with keyword arguments is:

# "dict(key1=value1, key2=value2)".

# Additionally, the dictionary constructor can take as many arguments as the
# user wants. Below is an example:

dicty = dict(Apple='iPhone', Samsung='Galaxy', Google='Pixel')
print(f"Dicty printed:\n{dicty}")

####################################################################################################

# TITLE:  Section 2.1 - List Comprehension

# List comprehensions are a means to create a new list based on the values of an existing iterable.
# The syntax for using list comprehensions is "[expression for x in iterable_object]" where
# "expression" represents a value and "x" is each item in "iterable_object". In the example below we
# are using list comprehensions to iterate through each number between 0 and 9, squaring the number,
# and then storing it in a list called "squares".
squares = [i**2 for i in range(10)] # IMPORTANT: The "range()" function creates a list of numbers.
print(f"Squares list: {squares}")

# Conditions can be added to list comprehensions. The condition is added to the end of a list
# comprehension after the "for loop". In the example below, an "if statement" is used to create a
# list of the squared odd numbers between 0 and 9.
squares_of_odd_numbers = [i**2 for i in range(10) if i % 2 != 0]
print(f"Squares of odd numbers list:\n{squares_of_odd_numbers}")

####################################################################################################

# TITLE:  Section 2.2 - Dictionary Comprehension

# Python also allows for dictionary comprehensions. Just as in list comprehensions, dictionary
# comprehensions are a means to create a new dictionary based on the values of two existing iterables.
# The syntax for a dictionary comprehension is "{key: value for vars in iterable}" where "key" is
# the new key in a given key/value pair, "value" is the new value in a given key/value pair, "vars"
# is an iteration in the iterable, and "iterable" is the iterable object. In the below example, we
# are creating a dictionary that has keys of 0-9 and values of the key*2.

new_dictionary = {num: num*2 for num in range(10)}
print(f'new_dictionary:\n{new_dictionary}')

# Again, just as in list comprehension, a condition can be added to the end of a dictionary
# comprehension. In the example below, we will take the same comprehension from above, but only add
# a key/value pair if the key is an even number.
new_dictionary = {num: num*2 for num in range(10) if num % 2 == 0}
print(f'new_dictionary:\n{new_dictionary}')

# TODO: Section 2 of TODO 16 (5 min for students, 2 min for demo)

####################################################################################################

# TITLE: Section 3.1 - Advanced Loops For Lists

num_list = [3, 15, 31, 1, 11, 107]

# In previous lessons, we have used counters to keep track of which element is being iterated over
# in a string or list. Below is an example of this concept through the use of a "for loop".

i = 0 # This will act as a counter to keep track of the index position of each element in "num_list"
for num in num_list:
  print(f"{num} is at index {i}")
  i += 1

# The "enumerate()" function is a built-in Python function that makes the above syntax cleaner and
# easier to read. The "enumerate()" function adds a counter to an iterable and returns it as a value
# called an enumarate object. The counter created by "enumerate()" replaces the need to set your own
# iterator outside of the for loop.

# The syntax for looping through an enumerate object is
# "for index, var in enumerate(iterable_object)" where "index" is a number starting at 0 that is
# incremented by one for each iteration and "var" is the variable representing each element in the
# iterable. Below is an example of using a "for loop" to loop through an enumerated object of
# "number_list".
for idx, num in enumerate(num_list):
    print(f"{num} is at index {idx}")

####################################################################################################

# TITLE: Section 3.2 - Advanced Loops For Dictionaries

leagues = {'MLB': 'baseball', 'MLG': 'e-sports', 'WNBA': 'basketball'}

# In previous lessons we learned that we can use variables to access key/value pairs while
# looping through a dictionary. Below is an example of this concept.
for league in leagues:
  sport = leagues[league] # Using bracket notation to access the key's value.
  print(f"The {league} plays {sport}.")

# Python also has a more readable way to access key/value pairs while iterating over a dictionary.
# The ".items()" method is used to access the key/value pair in a given iteration. The syntax for
# the ".items()" method is "for key, value in iterable.items():". Below is an example of using the
# ".items()" method.
for league, sport in leagues.items():
  print(f"The {league} plays {sport}.")

# TODO: Section 3 of TODO 16 (5 min for students, 2 min for demo)

####################################################################################################

# TITLE: Section 4 - Using Membership Operators with Lists and Dictionaries

# A membership operator is used to test if an object is present in an iterable object. For example,
# the "in" operator is used to check "if" a given element is "in" an iterable object. The syntax for
# this is, "if object in iterable_object:". Below are examples of using the "in" operator
# with a list and dictionary.

listy = ["Take", "me", "out", "to", "the", "ballgame"]

var = "ballgame"
if var in listy: # This checks if the value of "ballgame" is in the list "listy".
  print(f"The string {var} is in listy.")

if "CSX" in listy: # This checks if the value of "CSX" is in the list "listy".
  print(f"'CSX' is in listy.")
else: # If "var2" isn't in listy, the condition will be False and the "else" statement will execute
  print(f"'CSX' is not in listy.")

languages = {"italian": "Italy", "spanish": "Spain", "french": "France"}

if "italian" in languages: # This checks if "italian" is in the dictionary "languages".
  print(f"The string 'italian' is a key in languages.")

if "mandarin" in languages: # This checks if "mandarin" is in the dictionary "languages".
  print(f"The string 'mandarin' is a key in languages.")
else: # If "mandarin" isn't in languages, the condition will return False and the "else" statement will execute
  print(f"The string 'mandarin' is not a key in languages.")

# In Python, we can also check if an object does not exist in an iterable object with the operator,
# "not in". The syntax for using the "not in" operator is, "if object not in iterable_object:".
# Below are examples of using the "not in" operator with a list and dictionary.

if "peanuts" not in listy:
  print("The string 'peanuts' is not in listy")

if "german" not in languages:
  print("The string 'german' is not a key in listy")


# TODO: Section 4 of TODO 16 (7 min for students, 4 min for demo)
