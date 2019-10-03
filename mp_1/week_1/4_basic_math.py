"""
This is an introduction to basic math in Python
"""

# here are some basic mathematical functions shown in Python

addition = 2 + 2

subtraction = 10 - 5

multiplication = 3 * 4

# note- in python 2, division of whole numbers always returned a whole number
# but in python 3, they return float values
division = 12 / 4

exponents = 2 ** 2

# the number 9 goes into 120 13 times, with a remainder of 3. This is also called a "modulo operator"
remainder = 120 % 9

print(addition, subtraction, multiplication, division, exponents, remainder)

# when setting multiple variables, you can also set them like this
addition, subtraction, multiplication = 4 + 4, 20 - 6, 2 * 2

# notice in the variables above, we used the same names. Variables can change and be reassigned. 
# Let's reprint the variables from above and see if they change to our new mathematical operations

print(addition, subtraction, multiplication)

# Here is a new concept we haven't covered yet- constants! Constants are like variables,
# but they are typed in all caps and don't change! Variables can be manipulated and change,
# whereas constants must remain the same

# for example, the corporate tax rate is 20%. Hence, that would be an example of a constant

company_profit = int(input("How much money did your company make this year?: "))
CORPORATE_TAX_RATE = .20
