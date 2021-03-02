"""
Common errors you will/may have already encounter(ed).
"""

# Below are a few examples of errors you will undoubtedly see in your time as a programmer.
# These errors will show up in your terminal letting you know where the problem is and which
# type of error it is. 

# TITLE: Section 1: No Dividing by Zero! (3 min)
# Our first error is a ZeroDivisionError. This is pretty self explanatory. As we know from math
# classes, you can't divide a number by 0. That rule doesn't go away in Python. Pay attention
# to the message in the terminal, as it tells you where Python thinks there is an error. 

# ZeroDivisionError: division by zero
number = 10 * (1/0) # FIXME: Comment out this line once this error has been demo'd.
print(number)

####################################################################################################

# TITLE: Section 2: NameErrors are Easy (3 min)
# You'll see below when we run our code again that we get a 'NameError'. This occurs when you try to 
# use a variable in your program that has not been defined yet. The below code uses the variable
# 'spam' when 'spam' hasn't been defined. Again pay attention to your terminal. It lets you know
# where the problem is and gives hints as to what's wrong.

# NameError: name 'spam' is not defined
equation = 4 + spam * 3 # FIXME: Comment out this line once this error has been demo'd.
print(equation)

####################################################################################################

# TITLE: Section 3: Know Your Types (3 min)
# Lastly let's take a look at a 'TypeError'. In this case, there is an error occuring because Python
# thinks the variable "twotwo" is looking to concatenate the string "2" and the integer "2". As we
# know from earlier lessons, we can't concatenate strings and integers, so Python throws us
# this error.

# TypeError: Can't convert 'int' object to str implicitly
twotwo = '2' + 2 # FIXME: Comment out this line once this error has been demo'd.
print(twotwo)

# TODO: Complete TODO 8 (5 minutes for students, 2 minute demo)
