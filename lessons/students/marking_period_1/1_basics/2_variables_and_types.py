"""
This is a docstring. They are used to detail files at a high level.
"""

# These lines that start with a pound sign are comments. They do nothing to the program
# except provide instructions, personal notes, or anything that you want really!

# Variables can be thought of as "containers" for a value. These values have types.
# Types include things like integers, strings, floats, booleans, lists, and dictionaries.
# The name of the variable is on the left of the `=` sign and on the right is the content
# of the variable

# a number without a decimal point is of the type integer
number1 = 5 # integer

####################################################################################################

# a number with a decimal point is a float
float2 = 6.3 # floating point number
float1 = 7. # also a floating point number

####################################################################################################

# anything wrapped in quotes is a string
string1 = "Hello" # string over here
string2 = "my name is 29#$%@#$^%" # literally, anything wrapped in quotes is a string
string3 = "369"

####################################################################################################

# naming variables is important!!! this has a capital "S" in string, so its different
# than the previous variable of string1
String1 = "Wonderful!"

####################################################################################################

# MULTIPLE VARIABLES IN ONE VARIABLE?! YEP!
big_string = string1 + string2
print(big_string)

# TODO: Section 1 of TODO 2
####################################################################################################

# Setting multiple variables in one line of code? Also yep. Make sure you use your commas wisely!
var1, var2, var3 = 1, 2, 3
print(var1, var2, var3)

# TODO: Section 2 of TODO 2
####################################################################################################

# Booleans are true or false values. The first letter gets capitalized in the word
boolean = False
boolean2 = True

####################################################################################################

# if you want to set a variable to an empty value, use the None type
variable_for_later = None

# TODO: Section 3 of TODO 2
####################################################################################################

# print is an example of a function. a function is a block of code that runs when it is called upon.
# the items you place in the parentheses are called arguments
# lets call the print function and pass arguments to print them
print("printing things, woohoo!!")
print(2387938457)
print(number1)
print(string1)

string1 = "hello"
string3 = 45

# FIXME: the code right here is broken, let's run it for fun to show that numbers cannot be
# concatenated directly with strings
# print(string1, " i am python number " + string3, ", hear me roar!!")

# You can also "concatenate" strings together below and print multiple strings
print(string1, " i am python number", string3, ",hear me roar!!")

# notice how the spacing is off in the output of big_string?
# thats because variables dont account for spaces! put an extra space in the string to make it neat
print(big_string)
####################################################################################################

# Type conversion. 

# Python defines type conversion functions to directly convert one data type to another.

# For example, you can convert integers to strings by wrapping the variable in the string function, 
# as seen below:

player_name = "Lebron James"
player_weight = 250

print(player_name + " weighs " + str(player_weight) + " pounds ")

# Similarly, you can convert an integer into a float:

num = 18
floated_num = float(num)
print(floated_num)

# And you can check type of something in Python by wrapping `type()` and printing it
print(type(floated_num))

# See below on how to convert the different data types

# String: str()
# Float: float()
# Integer: integer()
# Boolean: bool()


# TODO: Section 4 of TODO 2
