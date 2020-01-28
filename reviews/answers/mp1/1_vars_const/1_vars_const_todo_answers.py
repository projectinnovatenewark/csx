"""
working with vars, concats, canstants, strings and Booleans
"""
#Print Statement

# TODO: Print "Hello World"

print("Hello World")

# Math

# TODO: Use each math operation in a print statement

print(2 + 2) # addition
print(40 - 5) # subtraction
print(32 / 8) # division
print(4 * 2) # multiplication
print(4 ** 2) # exponent
print(10 % 3) # modulo operator finds the remainder 
# 3 goes into 10 3 times with the remainder of 1

# Data Types

# TODO: Set a variable to each data type we've learned and print them

number1 = 5 # integer
print(number1)

float2 = 6.3 # floating point number
print(float2)

string1 = "Hello" # string
print(string1)

boolean = False # boolean
boolean2 = True # boolean
print(boolean)
print(boolean2)

#  variables

# TODO: Define two (2) floats as variables and multiply them in a print statment.
var1 = 3.94
var2 = 40.1
print(var1 * var2)

#Concat


# TODO: Define a variable as your first name and print "Hello my name is (insert name here)"

name = "Gary"

print("Hello my name is", name)

# TODO: print the same concatenation using multiple variables
var1 = "Hello"
var2 = "my name is"
var3 = "Gary"
print(var1, var2, var3)


 # TODO: Print a mathematical boolean statement to test if it is True or Talse

print(10>9)

#######################################################################

# TODO: Use the file named "costant.py"
# TODO: Set a constant "PI" to 3.14
# TODO: In the current file: Import PI

import constant
print(constant.PI)

# TODO: Define the radius of a circle as "r"

r = 10

# TODO: Find the circumfrence of a cricle using our constant and variable (2(pi)(r^2)) and print it

circumference = 2 * constant.PI * (r ** 2)

print(circumference)

# TODO: print a readable statement giving the circumference

print("The circumference is", str(circumference), "inches.")

# circumference must be converted to a string to be concatanated.
# Students most likely will not know this.
# Use as a segway into next lesson. 

