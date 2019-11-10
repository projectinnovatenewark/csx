"""
This is an introduction to basic math in Python
"""

# here are some basic mathematical functions shown in Python
# we will change these values later in this file to show that variables can change
addition = 2 + 2
subtraction = 10 - 5
multiplication = 3 * 4

# note- in python 2, division of whole numbers always returned a whole number
# but in python 3, they return float values
division = 12 / 4
exponents = 2 ** 2

# the number 9 goes into 120 13 times, with a remainder of 3. This is also called a "modulo operator"
# modulo returns the remainder
remainder = 120 % 9
print("Math Section One")
print(addition, subtraction, multiplication, division, exponents, remainder)

# when setting multiple variables, you can also set them like this
addition, subtraction, multiplication = 4 + 4, 20 - 6, 2 * 2

##############################################################################################

# notice in the variables above, we used the same names. Variables can change and be reassigned.
# Let's reprint the variables from above and see if they change to our new mathematical operations
print("Math Section Two")
print(addition, subtraction, multiplication)

# Here is a new concept we haven't covered yet- constants! Constants are like variables,
# but they are typed in all caps and don't change! Variables can be manipulated and change,
# whereas constants must remain the same
# for example, the corporate tax rate is 20%. Hence, that would be an example of a constant
# you will also see for company profit we use the int() function, which converts items to the type of integer
company_profit = int(input("How much money did your company make this year?: "))
CORPORATE_TAX_RATE = .20
taxes_paid = company_profit * CORPORATE_TAX_RATE

# wait, you can't concatenate floats and strings!! lets use the str() function with the
# "taxes_paid" variable to make the output work
print("I paid " + str(taxes_paid) + " dollars in taxes for my business")

# if you do calculations between a integer and float, the output is a float
summation = 3 + 3.0

# formatting is important for numbers if you want to specify an output. By using the percent
# sign below and .2f, you specify that the variable "summation", which follows the string, will have two
# decimal points.
print("The sum of x and y is %.2f" %summation)

number_list = [1, 2, 3, 4, 5, 6]
# min finds the minimum of a set of numbers
print(min(number_list))

# max finds the max of a set of numbers
print(max(number_list))

# abs finds the absolute value
print(abs(150))

# the absolute value of a negative number is the positive of that number
print(abs(-43))

# the absolute value of a float is the positive of that number including the decimal values
print(abs(-43.5))

# sum adds numbers together if you're either
#   a) too lazy to put plus signs between everything
#   b) have a super long list that makes your head spin
#   c) both of the above
print(sum(number_list))