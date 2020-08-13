"""
This is an introduction to string manipulation in Python
"""

# TITLE Section 1 of Todo 3

# With the input function, you can get input from users.
# Lets set the user inputs equal to variables, then use them appropriately.
first_name = input("What is your first name?: ")
last_name = input("What is your last name?: ")

# Since the values you input are set to variables, we can concatenate the strings.
print("My first name is", first_name, "and my last name is", last_name)

# You can also seperate variables  with commas. This is the preferred
# method when using the print function. We try not to build the string using simple addition, since
# that is quite slow in Python. Strings are immutable objects, so each string addition
# involves creating a new string of the right length and copying the content of the two
# strings being added.
var_one = "scooby"
var_two = "doo"
print("Hello, my name is", var_one, var_two)

#TODO: Section 1 of TODO 3
####################################################################################################

# TITLE Section 2 of TODO 3
# Next we are going to introduce the title() function. This will capitalize the beginning of every
# word in a string as well as make the rest of the characters lower case. 

thor2 = "tHOr: the DARK wOrlD".title()
print(thor2)

# There are also casing functions for upper and lower cases, which are used the same as title().
# They are .upper() and .lower(). We will explore these below.

mixed_string = "whAT Does THIS dO?"

print(mixed_string.lower())
print(mixed_string.upper())

# New string tools! You can start a string with '\n' when printing it to print
# on a new line, which would add a line above it. "\" is a special character, also called
# the "escape" character. It is used in representing certain 'whitespace characters' or
# adding space between characters. : "\t" is a tab and "\n" is a newline,

print("\n" + mixed_string.lower())

print("\t" + mixed_string.title())

#TODO: Section 2 of TODO 3
####################################################################################################

# TITLE Section 3 of TODO 3
# There are many methods of string formatting including the format() function and using
# percent signs (%) to include numbers. Here are brief examples of each:
integer_number = 3
print("Here is the number as a float: %.2f" %integer_number)

# The Python3 way to do the above is strictly by using the format function as shown below.
# You can also add a number (i.e. 04 below) to add padding to the front of a number
# which means that the first number will print with 6 digits (including the decimal point)
# and add any additional digits as zeros in front of the number.
integer_number = 6
float_number = 5
print("Here is first variable passed into format {:06.2f} and here is the second {:.2f}".format(integer_number, float_number))

# Lastly you can use lists (which will be explored more later) to format and directly
# input an item into a string. For example, numbers[0] would represent the first number in the list.
numbers = [3, 6, 9]
song_lyric = "{0} {1} {2}, transit line".format(numbers[0], numbers[1], numbers[2])

print(song_lyric)

# This would produce the same output as the line above. You can set the variable to be printed inside
# the format function allows you to set the variable inputs in the function.
numbers = [3, 6, 9]
song_lyric = "{first} {second} {third}, transit line".format(first="three", second="six", third="nine")

print(song_lyric)

# As we explored above, this is a list. students[0] would be "Marcus", students[1] would
# be "Gary", and so on.
students = ["Marcus", "Maria", "Sam"]
attendance_output = "The present students are {}, {}, and {}".format(students[0], students[1], students[2])
print(attendance_output)

#TODO: Section 3 of TODO 3
####################################################################################################

# TITLE: Section 4 of TODO 3
# The join function combines items in a list. In this case, it will create a large string.
# The first input specifies how to join the items in the list.
# In the example below, it will join each item with a comma.
list_to_join = ["combine", "these", "words", "into", "one", "string"]
print(",".join(list_to_join))

# The join function will not change the original list. As you can see from this output, it stays the same.
print('as you can see, the list has not changed', list_to_join)

# If you wanted to capture the new value of combining the items in the list, you would have
# to set it equal to a new variable like this:
new_var = "".join(list_to_join)
print("this is the new var: ", new_var)

# But that looks kind of silly without spaces! Lets join them with a space instead to see
# the better outcome. We can reassign the new_var variable to have this new value.
new_var = " ".join(list_to_join)
print("this is the new var's updated value: ", new_var)

# Split seperates a string into items in a list. The split occurs in the character that you specify.
# For example, in the split we put an empty space. This will split the string into items whenever
# there is a space, so each word will represent an item in the list.
string_to_listify = "lets separate these words into separate items in a list"
print(string_to_listify.split(" "))

# IMPORTANT:
# The behavior for the join function also applies to split. It will NOT update the original
# variable. This will still be a string, even though we performed a split function on it.
print(string_to_listify)

# If we wanted to capture the value of that split, we would have to set it equal to a new variable.
listified_string = string_to_listify.split(" ")
print(listified_string)

# The replace function exchanges one input for another.
# Lets make the following polite statement a little less formal:
print("Hello, how are you?".replace("Hello", "Sup"))

# The startswith funtion returns a boolean value (true/false) on whether or not a
# string begins with a certain set of characters. Lets check if someone is saying hello 
# in the following two statements:
print("Hello, I am saying hi to someone".startswith("Hello"))
print("Whats good?".startswith("Hello"))

# The endswith function returns a boolean value (true/false) on whether or not a string ends with a certain
# set of characters. Lets check if these statements are questions:
print("Am I a question?".endswith("?"))
print("I'm not a question.".endswith("?"))

#TODO: Section 4 of TODO 3
