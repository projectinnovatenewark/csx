"""
Review on variables, and variable types.
"""

# TITLE: Section 1 - Variables & Types

# A variable is a reserved memory location used to store a given value. All data types can be stored
# as variables. When defining a variable, the name is on the left side of the "=" and the data
# being stored is on the right.

# A number without a decimal point is an integer.
number1 = 5

# You can set multiple variables in one line of code using commas.
var1, var2, var3 = 1, 2, 3
print(var1, var2, var3)

# A number with a decimal point is a float.
float1 = 6.3

# Anything wrapped in quotation marks is a string, which represents text.
string1 = "Hello"
string2 = "World!"

# Concatenation is the process of combining strings.
big_string = string1 + string2
print(big_string)

# Booleans are true or false values.
boolean = False
boolean2 = True

# If you want to set a variable to an empty value, use the None type.
variable_for_later = None

# TODO: Section 1 of TODO 2R

####################################################################################################

# TITLE: Section 2 - Type Function and Type Conversion

# Python uses the type() function to check the type of a variable.

num1, string1 = 2, "Any string"

print(f"num1: {type(num1)}")
print(f"string1: {type(string1)}")

# To convert values into other types use the following built in functions:
int() # is used to convert a given value to an integer.
float() # is used to convert a given value to a float.
str() # is used to convert a given value to a string.
bool() # is used to convert a given value to a boolean.

num1 = 45
print(f"num1: {type(num1)}")

num_to_string = str(num1)
print(f"num_to_string: {type(num_to_string)}")
