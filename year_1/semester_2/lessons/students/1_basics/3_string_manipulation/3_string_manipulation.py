"""
This is an introduction to string manipulation in Python
"""

# TITLE: Section 1 - The "input()" Function (5 minutes)

# With the input function, you can get input from users.
# Lets set the user inputs equal to variables, then use them appropriately.
first_name = input("What is your first name?: ")
last_name = input("What is your last name?: ")
age = input("What is your age?: ") # FIXME: Teacher, use type conversion after getting an error.

# As you can see below, inputs automatically set a user input to a string.
print(f"The variable age has a type of {type(age)}.")

# The line below will try to concatenate three variables. What type(s) can be concatenated?
statement = first_name + last_name + age
print(statement)

# Additionally, if you want a user to enter an input on a blank line you can use an empty input
# function.
print("Enter the name of your favorite movie on the next line:")
movie = input()
print(f"Your favorite movie is {movie}.")

# TODO: Section 1 of TODO 3 (2 minutes for students, 1 minute demo)
####################################################################################################

# TITLE: Section 2 - Modifying the Casing of Strings (3 minutes)
# Next we are going to introduce the .title() function. This will capitalize the beginning of every
# word in a string as well as make the rest of the characters lower case.
thor2 = "tHOr: the DARK wOrlD".title()
print(thor2)

# There are also casing functions for upper and lower cases, which are used the same as title().
# We will explore .upper() and .lower() below.
mixed_string = "whAT Does THIS dO?"

print(mixed_string.lower()) # This will change all characters to lower case.
print(mixed_string.upper()) # This will change all characters to upper case.

# New string tools! You can start a string with '\n' when printing it to print
# on a new line, which would add a line above it. "\" is a special character, also called
# the "escape" character. It is used in representing certain 'whitespace characters' or
# adding space between characters. : "\t" is a tab and "\n" is a newline,
print("\n" + mixed_string.lower())
print("Here is one line \nand here is another line")
print("\t" + mixed_string.title())

# TODO: Section 2 of TODO 3 (4 minutes for students, 1 minute demo)
##################################################################################################

# TITLE: Section 3 - Formatting Variables in Strings (5 minutes)

# TIP: This section can be of minor emphasis as it is not seen very often in our curriculum.
# There are many methods of formatting strings. One of which is the use of a percent sign "%" to
# format the amount of decimal places in a float.
integer_number = 3
print("Here is the number as a float: %.2f" %integer_number)

# The cleaner way to do the above is by using the format function. The .format() function lets us
# concatenate elements within a string through positional formating.
first_name = input("What is your first name?: ")
last_name = input("What is your last name?: ")
print("My name is {} {}.".format(first_name, last_name))

# You can also use the .format() function to modify the number of decimal places just as the % does.
# To do so, you use the format ":num_of_zeros.num_of_decimal_placesf"
integer_number = 6
float_number = 5.1234
print("Here is first variable passed into format {:06.2f} and here is the second {:.2f}".format(integer_number, float_number))

####################################################################################################

# TITLE: Section 4 - String-related Functions (9 minutes)

# The join function combines items in a list. In this case, it will create a large string. The first
# input specifies how to join the items in the list. In the example below, it will join each item
# with a comma.
list_to_join = ["combine", "these", "words", "into", "one", "string"]
print(f"Join the list_to_join {','.join(list_to_join)}")

# The join function will not change the original list. As you can see from this output, it stays
# the same.
print(f"As you can see, the original variable list_to_join has not changed {list_to_join}")

# If you wanted to capture the new value of combining the items in the list, you would have
# to set it equal to a new variable like this:
new_var = "".join(list_to_join)
print(f"This is the new var: {new_var}")

# But that looks kind of silly without spaces! Let's join them with a space instead to see a cleaner
# outcome. We can reassign the new_var variable to have this new value.
new_var = " ".join(list_to_join)
print(f"This is the new_var's updated value: {new_var}")

# The split function seperates a string into items in a list. The split occurs in every instance of
# the character that you specify. For example, in the split we put an empty space. This will split
# the string into list items wherever there is a space.
string_to_listify = "lets separate these words into separate items in a list"
print(f"Split the string_to_listify {string_to_listify.split(' ')}") # FIXME: Teacher, demo this
                                                                     # FIXME: with an "s", as well!

# Split shares the same behavior as the join function. It will NOT update the original
# variable. This will still be a string, even though we performed a split function on it.
print(f"As you can see, the original variable string_to_listify has not changed {string_to_listify}")

# Just as before, if we wanted to capture the value of that split, we will have to set it equal to a
# new variable.
listified_string = string_to_listify.split(" ")
print("this is listified_string's updated value: ", listified_string)

# The replace function exchanges one input for another. Lets make the following polite statement a
# little less formal:
print("Hello, how are you?".replace("Hello", "Sup"))

# The startswith function returns a boolean value (True/False) on whether or not a
# string begins with a certain set of characters. Lets check if someone is saying hello
# in the following two statements:
print("Hello, I am saying hi to someone".startswith("Hello"))
print("Whats up?".startswith("Hello"))

# The endswith function returns a boolean value (True/False) on whether or not a string ends
# with a certain set of characters. Lets check if these statements are questions:
print("Am I a question?".endswith("?"))
print("I'm not a question.".endswith("?"))

# TODO: Section 4 of TODO 3 (3 minutes for students, 1 minute demo)
