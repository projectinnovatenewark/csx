"""
This is an introduction to string manipulation in Python
"""

# TITLE Section 1 (5 minutes)

# With the input function, you can get input from users.
# Lets set the user inputs equal to variables, then use them appropriately.
first_name = input("What is your first name?: ")
last_name = input("What is your last name?: ")

# Inputs automatically set a user input to a string- so what if we wanted to ask someone
# for their age and have it set equal to an integer? We can wrap the entire input statement
# in an int() function, and then the user's number input would be converted into a variable.
# As you recall from last lesson, we can also convert values to strings with the str() function.
age = int(input("What is your age?"))
print("I am", str(age), "years old.")

# Since the values you input are set to variables, we can print them next to plan old strings.
# Additionally, since we want a period at the end of the sentence, we will use a "+" sign so that
# there isnt an extra space after the last_name variable (recall- spaces occur when you use commas).
print("My first name is", first_name, "and my last name is", last_name + ".")

# Additionally, if you want a user to enter an input without having any words on the line of that
# input, you can use an empty input function.
print("Enter the name of your favorite movie on the next line:")
movie = input()
print("Your favorite movie is", movie)

# TODO: Section 1 of TODO 3 (2 minutes for students, 1 minute demo)
####################################################################################################

# TITLE Section 2 (3 minutes)
# Next we are going to introduce the .title() function. This will capitalize the beginning of every
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

# TODO: Section 2 of TODO 3 (4 minutes for students, 1 minute demo)
####################################################################################################

# TITLE Section 3 (10 minutes)
# There are many methods of string formatting including the .format() function and using
# percent signs "%" to include numbers. Here are brief examples of each:
integer_number = 3
print("Here is the number as a float: %.2f" %integer_number)

# The cleaner to do the above is strictly by using the format function as shown below.
# You can also modify a number (i.e. 06 below) to add padding to the front of a number
# which means that the first number will print with 6 digits (including the decimal point)
# and add any additional digits as zeros in front of the number.
integer_number = 6
float_number = 5.1234
print("Here is first variable passed into format {:06.2f} and here is the second {:.2f}".format(integer_number, float_number))

# IMPORTANT:
# Here we will introduce the primary method with which we will be inserting variables directly
# into strings, called "f shorthand". Let's set some variables and insert them in a string that has
# a lowercase "f" right before the first quotation mark in the string.

num1, num2, num3 = 3, 6, 9
song_lyric = f"{num1}, {num2:.1f}, {num3:.2f} transit line." # You can also include formatting like
                                                             # our previous examples with ":.2f"

print(song_lyric)

# When we explore lists and dictionaries in the future, you will see that items from lists and
# key/value pairs from dictionaries can also be directly inserted into the f shorthand curly braces.
# The first item in "students" is "Marcus", and we access the first item with the
# convention "students[0]". The first item in a list is always zero, the second item is one, etc.
students = ["Marcus", "Maria", "Sam"]
first_student = students[0] # This variable would equal the string "Marcus".
print("The first student in the list is", first_student, "and the second student is", students[1] + ".")

attendance_output = f"The present students are {students[0]}, {students[1]}, and {students[2]}."
print(attendance_output)

# TODO: Section 3 of TODO 3 (5 minutes for students, 2 minute demo)
####################################################################################################

# TITLE: Section 4 (7 minutes)
# The join function combines items in a list. In this case, it will create a large string.
# The first input specifies how to join the items in the list.
# In the example below, it will join each item with a comma.
list_to_join = ["combine", "these", "words", "into", "one", "string"]
print(",".join(list_to_join))

# The join function will not change the original list. As you can see from this output, it stays
# the same.
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

# The startswith function returns a boolean value (true/false) on whether or not a
# string begins with a certain set of characters. Lets check if someone is saying hello
# in the following two statements:
print("Hello, I am saying hi to someone".startswith("Hello"))
print("Whats good?".startswith("Hello"))

# The endswith function returns a boolean value (true/false) on whether or not a string ends
# with a certain set of characters. Lets check if these statements are questions:
print("Am I a question?".endswith("?"))
print("I'm not a question.".endswith("?"))

# TODO: Section 4 of TODO 3 (3 minutes for students, 1 minute demo)
