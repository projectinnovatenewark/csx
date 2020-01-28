"""
working with vars, concats, canstants, strings and Booleans
"""
# Print Statements

# The way to see Python's outputs in the terminal is to use a print statement.
# It's customary for everyone's first program in a new language is to print "Hello World!"

print("Hello World")

#################################################################################################

#  Data Types

number1 = 10 # integer (whole numbers)
float2 = 4.3975 # floating point number (has a decimal)
string1 = "Let's learn some Python" # string (anything wrapped in quotes)
boolean = False # boolean
boolean2 = True # boolean
no_value = None # This has no value

# booleans are anything you can assign a true or false value

#################################################################################################

# Variables

# variables can be defined by any data type and structure. You'll see this as we progress 
# through the semester.

name = "Kobe"
num1 = 24
num2 = 8.0
boolean = True

equation1 = 10 + 4

# Variables can bhave their values reassigned as you wish. It can be the same data type or a completely different one!

#################################################################################################

# Math

print(2 + 2) # addition
print(40 - 5) # subtraction
print(32 / 8) # division
print(4 * 2) # multiplication
print(4 ** 2) # exponent
print(10 % 3) # modulo operator finds the remainder
# 3 goes into 10 3 times with the remainder of 1
# If a number is evenly divisible by another number, the remainder will be 0
# For example:
print(10 % 2) # 2 goes into 10 evenly 5 times, so the remainder is 0

var_1 = 10 * 4
print(var_1)

var_1 = "This is a new variable"
print(var_1)

#################################################################################################

#  Constants

GRAVITY = 9.8
#  constants are defined only in all caps
#  gravity = variable    GRAVITY = constant

GRAVITY = 11.2
print(GRAVITY)
# When you try to redefine a constant, you'll see an error in your terminal
# Constants are rarely used, but in most cases they are imported from other files.

#################################################################################################

#  Concatenate
#  concatenate is just combing strings


print("Hello my name is " + "Gary")

# Tip: Using plus signs is inconvienant and slows down your code. 
# See how the next example uses commas to seperate strings and automatically adds a space.

name = "Gary"

print("Hello my name is", name) #(name is the varable here)

# You can contatenate multiple variables as well as long as they are strings.

var1 = "Hello"
var2 = "my name is"
var3 = "Gary"
print(var1, var2, var3)

#################################################################################################

# Import

# Importing variables, constants, and anything else can come in hendy.
# To do this is simple. Use the import command followed by the name of the file.

# Import is normally done at the top of a file.
import import_learning

# then when going to use the desired variable use the filename.variable method

print(5 + import_learning.usefulnumber)

# This is done by using "import 'name_of_imported_file'"
# then the constant imported can be used as 'name_of_imported_file.CONSTANT'
