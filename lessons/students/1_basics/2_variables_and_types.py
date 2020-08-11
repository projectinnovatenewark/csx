"""
This is a docstring. They are used to detail files at a high level.
"""

# These lines that start with a pound sign are comments. They do nothing to the program
# except provide instructions, personal notes, or anything that you want really!

# Variables can be thought of as "pointers" to a value. These values have types.
# Types include things like integers, strings, floats, booleans, lists, and dictionaries.
# The name of the variable is on the left of the `=` sign and on the right is the content
# of the variable.

# A number without a decimal point is of the type integer.
number1 = 5

# A number with a decimal point is a float.
float2 = 6.3 # Floating point number
float1 = 7. # This is also a floating point number.

# Anything wrapped in quotation marks is a string.
string1 = "Hello" # String over here!
string2 = "my name is 29#$%@#$^%" # Literally, anything wrapped in quotes is a string.
string3 = "369" # Yes this is a string too.

# Naming variables is important! This has a capital "S" in string, so it's different
# than the previous variable of 'string1'.
String1 = "Wonderful!"

# MULTIPLE VARIABLES IN ONE VARIABLE?! YEP!
big_string = string1 + string2
print(big_string)

# When you see, TODO: Section x of TODO y, you should stop where you are and head over to
# the corresponding assignment for this section of the lesson.
# TODO: Section 1 of TODO 2

####################################################################################################

# Setting multiple variables in one line of code? Also yep. This is possible only when you use
# commas to separate them out. Be sure to keep track of this, as it can get confusing
# if you set too many variables on the same line.
var1, var2, var3 = 1, 2, 3
print(var1, var2, var3)

# Booleans are true or false values. Python knows it is a boolean when you capitalize the first
# letter in your value just like below!
boolean = False
boolean2 = True

# if you want to set a variable to an empty value, use the None type. Don't confuse this with the
# value '0'.
variable_for_later = None

# TODO: Section 2 of TODO 2

####################################################################################################

# Print is an example of a function. A function is a block of code that runs when
# it is called upon. The items you place in the parentheses are called arguments. Lets
# call the print function and pass arguments to print them.
string1 = "hello"
num3 = 45

print("printing things, woohoo!!")
print(2387938457)
print(num3)
print(string1)

# FIXME: The code right here is broken, let's run it for fun to show that strings cannot be
# concatenated directly non-strings. Be sure to comment it out before moving on in the lesson.
print(string1 + " I am python number " + num3, ", hear me roar!!")

# You can print any type by separating them with commas, as Python will automatically pass
# them into the print statement as separate "arguments", then convert them all into strings
# separated by one blank space.
print(string1, " I am python number", num3, ",hear me roar!!")


# TODO: Section 3 of TODO 2

####################################################################################################

# Sometimes when you are dealing with variables, you are ggoing to want to check the type of
# the variable to make sure you are correctly using it. Python has a built in funciton for this!
# To check the type of a variable, simply use type(some_variable_here). Here's a bunch of
# different variables what we can test this with:

num1, string1, bool1, flt1 = 2, "Any string", True, 12.903

# Now we use type(variable) to check.. Don't forget we need to use print() also to see an output.

print("num1:", type(num1))
print("string1:", type(string1))
print("bool1:", type(bool1))
print("flt1:", type(flt1))

# Python also makes it pretty easy to convert types into other trypes. For example,
# you can convert integers to strings by wrapping the variable in the string
# function to make concatenation possible as seen below:

player_name = "Lebron James"
player_weight = 250

print(player_name + " weighs " + str(player_weight) + " pounds.")

# Similarly, you can convert a variable that has an integer as its value into a float:

num = 18
floated_num = float(num)
print(floated_num)

# See below on how to convert the different data types

# String: str()
# Float: float()
# Integer: integer()
# Boolean: bool()

# TODO: Section 4 of TODO 2
