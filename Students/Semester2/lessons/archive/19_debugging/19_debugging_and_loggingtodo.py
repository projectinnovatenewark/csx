"""
Match up with a partner. One person should solve the 1st problem, the other should solve the 2nd.
You will then break your working code in minor ways and exchange the broken solutions. The other
person will have to fix your broken code. You can break your code in minor ways like removing colons
or completely switch up the function. Its up to you!
"""

# TODO: Problem 1:
# Write a function called multiplier. it should accept two arguments. The first arg, "l", should be
# a list of numbers. The second arg, "m", should be a number. In the function, set a new variable
# equal to an empty list, titled "new_list". Then, iterate through the list of numbers parameter, multiply
# each number by the multiplier parameter, and append that number to the new list.

# Once you complete the above loop, print out the original list followed by the new list inside the function.
# Call this function for both the first and second sets of multipliers and lists, which is done for you below
# the function definition.

multiplier_one = 3
num_data_one = [15, 12, 22, 8, 4]

multiplier_two = 4
num_data_two = [5, 88, 64, 35]

# Here's a quickstarter for your solution

def multiplier(l, m):
    new_list = []

multiplier(num_data_one, multiplier_one)
multiplier(num_data_two, multiplier_two)


# TODO: Problem 2:
# Write a "curver" function that sets a parameter of "grades". The argument passed should be the
# dictionary below, titled uncurved grades. Create new, empty lists for attendance, homework,
# midterm_one, and midterm_two.

# You should iterate through every score in the attendance, curve it up by 10%, and append that
# value to the new attendance list you created. Use that same logic of iterating through
# the lists and appending the curved values to the empty lists you create in the beginning
# of the function. Apply the above logic to the following curves:

# The homework should curve by 2%.
# The midterm one should be curved by 15%.
# The midterm two should be curved by 20%.

# Print the curved lists in the following format:
    # "The curved attendance grades are: " followed by your curved list.

uncurved_grades = {
    "attendance": [80, 90, 86, 94, 100, 64, 73],
    "homework": [100, 76, 92, 77, 80, 74, 70],
    "midterms": {
        "midterm_one" : [73, 64, 76, 90, 45, 67, 80],
        "midterm_two": [80, 90, 86, 94, 100, 64, 73]
    }
}

# Here's a quickstarter for your solution

def curver(grades):
    new_attendance = []
    new_homework = []
    new_midterm_one = []
    new_midterm_two = []

curver(uncurved_grades)
