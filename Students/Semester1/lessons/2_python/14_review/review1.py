# Variables
variable_name = "variable's value" # define a variable
print(variable_name) # output the variable
print(type(variable_name)) # print the type of the variable

########################################################

# Math 

summ = 10+5 # addition
divv = 50/5 # division

# modulo - six goes into fifteen evenly twice, with a remainder of 3 (modd is equal to 3)
modd = 15%6

pemdas_result = 10/(2+3)+5 # PEMDAS applies in Python, try to guess the output
print("Pemdas result: ", pemdas_result)

########################################################

# Imports

import random # random package comes built in to python

# the following print statement uses a "multi-line" string,
# which is commonly used when you have a long string
# that wouldn't be readable on one line.
print(
f"""
Random number generated using the randrange function
from the random package: >>>{random.randrange(0,5)}<<<
"""
)

########################################################

# Conditions

# basic if statement
if 10 > 5: # greater than check
  print("ten is greater than 5")

# if/else
if 'a' == 'b': # equivalency check
  print("These two things equal each other")
else:
  print("These values do not equal each other")

# explaining if/elif/else in their respective condition bodies
if 'a' == 'b':
  print("'If' is TRUE.")
elif 'a' == 'a':
  print("'If' is FALSE and 'Elif' is TRUE.")
else:
  print("All the conditions above me were FALSE")

########################################################

# Array operations
arr = ['spades','clubs'] # define array
arr.append('hearts') # add element to end of array
print(arr[0]) # reference element in array (via index position)
arr[0] = 'diamonds' # reassign first element in array to be 'diamonds'
print("Array: ", arr) # print the resulting array

########################################################

# Dictonary operations
dct = {'a':1, 'b': 2} # define dictionary
dct['c'] = 3 # define key/value pair
print(dct['b']) # reference values by their key
dct['a'] = 0 # reassign key/value pair
dct.pop('b') #remove key/value pair
print("Dictionary: :", dct) # print the resulting dictionary

########################################################

# Inputs and F Shorthand
name = input("What is your name?") # Inputs come in as strings by default
age = int(input("What is your age?")) # Convert age input to an integer
new_age = age+1 # It's your birthday!! Add one to your age (we can do this because we converted it to an integer)

birthday_card = f"Happy birthday {name} you are now {new_age} years old."
print(birthday_card)

########################################################

# Function basics
def funcName(p1,p2):
  print("You have called this function")
  return p1+p2

print("About to call the function...")
res = funcName(1,2) # Call the function and store the return value in the variable "res"
print("Print the result of the function: ", res)
