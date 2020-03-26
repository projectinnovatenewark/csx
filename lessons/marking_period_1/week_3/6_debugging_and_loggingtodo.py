"""
Match up with a partner. One person should solve the 1st problem, the other should solve the 2nd.
You will then break your working code and trade the broken solutions. The other person will have to
fix your broken code.
"""

# TODO: Problem 1:
# Write a function called multiplier. it should accept two arguments. The first arg, "l", should be
# a list of numbers. The second arg, "m", should be a number. In the function, iterate through
# the list of numbers and multiply them by the multiplier. First, print out the list that was
# passed as an argument. Once the loop is complete and the numbers have been multiplied, print out
# the new list. Call this function for both the first and second sets of multipliers and lists.

multiplier_one = 3
num_data_one = [15, 12, 22, 8, 4]

multiplier_two = 4
num_data_two = [5, 88, 64, 35]

# TODO: Problem 2:
# Write a function that takes in an argument of "grades". The argument should be the
# dictioary below, titled uncurved grades. You should iterate through every score in the
# attendance and curve it up by 10%. The homework should curve by 2%. The midterm one should
# be curved by 15%. The midterm two should be curved by 20%. Return a new variable called
# curved_grades with the newly curved values.

uncurved_grades = {
    "attendance": [80, 90, 86, 94, 100, 64, 73],
    "homework": [100, 76, 92, 77, 80, 74, 70],
    "midterms": {
        "midterm_one" : [73, 64, 76, 90, 45, 67, 80],
        "midterm_two": [80, 90, 86, 94, 100, 64, 73]
    }
}
