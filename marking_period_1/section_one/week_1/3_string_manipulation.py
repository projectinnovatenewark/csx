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

# there are many methods of string formatting including the format() function and using
# percent signs to include numbers. here are brief examples of each
integer_number = 3
print("Here is the number as a float: %.2f" %integer_number)

# you can also seperate variables in concatenation with commas
var_one = "scooby"
var_two = "doo"
print("Hello, my name is", var_one, var_two)

# lastly you can use lists (which will be explored more later) to format and directly
# input an item into a string
numbers = [3, 6, 9]
song_lyric = "{0} {1} {2}, transit line".format(numbers[0], numbers[1], numbers[2])
print(song_lyric)
