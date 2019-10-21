"""
This is an introduction to string manipulation in Python
"""

# with the input function, you can get input from users
# lets set the user inputs equal to variables, then use them appropriately
first_name = input("What is your first name?: ")
last_name = input("What is your last name?: ")

# since the values you input are set to variables, we can concatenate the strings
print("My first name is " + first_name + " and my last name is " + last_name)

# go back to the end of the input variables we've set and add .title() to the end of the line
# the title() function capitalizes a variable
# there are also casing functions for upper and lower cases, which are used the same as title
# they are .upper() and .lower()
