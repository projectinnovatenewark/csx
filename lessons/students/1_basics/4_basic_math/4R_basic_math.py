"""
This is an introduction to basic math and imports in Python
"""

# TITLE: Section 1 - Basic Mathematical Operations in Python, & Modulo (8 minutes)
# Below are some basic mathematical operations.
addition = 2 + 2 # This is addition
subtraction = 10 - 5 # This is sutraction
multiplication = 3 * 4 # This is multiplication
division = 12 / 4 # This is division
exponents = 2 ** 2 # This is finding exponential value (2^2 or 2 squared)

# The "%" is called the modulo operator. The modulo operator is used to return the remainder
# of one number in the next. In the below example, 9 goes into 120 13 times with a remainder of 3.
remainder = 120 % 9
print("Math Section One")
print(f"addition: {addition}, subtraction: {subtraction}, multiplication: {multiplication}, division: {division}, exponents: {exponents}, remainder: {remainder}.")

####################################################################################################

# TITLE: Section 1.1 - PEMDAS and Order of Operations (5 minutes)

# Math in Python follows PEMDAS. Let's test out some examples:

eq1 = 4 * (12 - 10) / 2
eq2 = (4 * 12) - 10 / 2
eq3 = 4 * (12 - 10 / 2)

print(f"We expect eq1 to equal 4. Python gives us {eq1}")
print(f"We expect eq1 to equal 43. Python gives us {eq2}")
print(f"We expect eq1 to equal 28. Python gives us {eq3}")

####################################################################################################

# TITLE: Section 1.2 - Constants, Incrementing/Decrementing, & Converting Numeric User Inputs (9 minutes)
# Constants are like variables, but they are typed in all caps and shouldn't change. If you do
# calculations between a integer and float, the output is a float.
summation = 3 + 3.0 # summation will now equal 6.0
print(f"1. summation is {summation}")

# Let's say you want to add to the variable summation. You want to increment it by one, for
# whatever reason. There's two ways to do this, and one is a bit longer code-wise.
# Lets do it that way first.
summation = summation + 1 # summation will now be 7.0
print(f"2. summation is {summation}")

# Using += will add whatever value comes after to the variable, then reassign the variable
# to that new value. Since summation was 7.0 and we use += 2, the value of summation after
# this line will be 9.0.
summation += 2 # summation will now equal 9.0
print(f"3. summation is {summation}")

# On a similar note, you can decrement with -=. Let's see how that looks.
summation -= 3 # summation will now equal 6.0
print(f"4. summation is {summation}")

# TODO: Section 1 of TODO 4 (8 minutes for students, 3 minute demo)

####################################################################################################

# TITLE: Section 2 - Math with Lists and Absolute Values (10 minutes)
# Below is a list of random numbers we are going to use to practice some built-in Python
# functionality.
number_list = [13, 27, 4, 12, 39, 100]

# To find the minimum value in a list, we can use the built in function: min().
list_min = min(number_list)
print(f"The min of number_list is {list_min}")

# To find the maximum value in a list, we can use the built in function: max().
list_max = max(number_list)
print(f"The max of number_list is {list_max}")

# To find the summation of all the numbers in a list, we can use sum().
list_sum = sum(number_list)
print(f"The sum  of number_list is {list_sum}")

# To find the absolute value of a number, we can use abs().
neg_int = -10
pos_int = 10

abs_neg = abs(-10)
abs_pos = abs(10)
print(f"The absolute value of {neg_int} is {abs_neg}.")
print(f"The absolute value of {pos_int} is {abs_pos}.")

# The same concept applies to floats as well!
neg_float = -49.232
pos_float = 3.5
print(f"The absolute value of {neg_float} is {abs(neg_float)}.")
print(f"The absolute value of {pos_float} is {abs(pos_float)}.")

# TODO: Section 2 of TODO 4 (8 minutes for students, 3 minute demo)

####################################################################################################	

# TITLE: Section 3 - Short Import Intro and the Math Package (8 minutes)
# We also have the math package/module from python. Python has built in tools that we	
# can import and use to help us in mathematical operations. Normally imports go at the	
# TOP of a file, but we will put it here to consolidate the lesson.	

import math	

# Now that we have the math package imported, we can use methods attached to the module. We will be
# using the pi method, which returns the numerical value of π. We will be using this to calculate
# the area of a circle.

pi = math.pi
print(f"π is equal to {pi}.")

radius = int(input("What is the radius of your circle (Only input integers): "))
area = pi * radius ** 2

print(f"The area of a circle with a radius of {radius} is equal to {area} units.")
