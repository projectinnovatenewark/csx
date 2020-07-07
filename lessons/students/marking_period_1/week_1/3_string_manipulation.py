"""
This is an introduction to string manipulation in Python
"""

# with the input function, you can get input from users
# lets set the user inputs equal to variables, then use them appropriately
first_name = input("What is your first name?: ")
last_name = input("What is your last name?: ")

# since the values you input are set to variables, we can concatenate the strings
print("My first name is", first_name, "and my last name is", last_name)

# you can also seperate variables in concatenation with commas. this is the preferred
# method of concatenation. we try not to build the string using simple addition, since
# that is quite slow in Python (strings are immutable objects, so each string addition
# involves creating a new string of the right length and copying the content of the two
# strings being added).
var_one = "scooby"
var_two = "doo"
print("Hello, my name is", var_one, var_two)

# go back to the end of the input variables we've set and add .title() to the end of the line
# the title() function capitalizes the first letter of every word in a string.
print(first_name.title()) # this title-izes the first name

# TODO: Section 1 of TODO 3
####################################################################################################

# there are also casing functions for upper and lower cases, which are used the same as title
# they are .upper() and .lower(). we will explore these below

# new string tools! you can start a string with '\n' when printing it to print
# on a new line, which would add a line above it. "\" is a special character, also called
# the "escape" character. It is used in representing certain 'whitespace characters' or
# adding space between characters. : "\t" is a tab and "\n" is a newline,
mixed_string = "frAnCiNe"

print(mixed_string.lower())

print("\n" + mixed_string.upper())

print("\t" + mixed_string.title())

# there are many methods of string formatting including the format() function and using
# percent signs (%) to include numbers. here are brief examples of each
integer_number = 3
print("Here is the number as a float: %.2f" %integer_number)

####################################################################################################

# the python 3 way to do the above is strictly by using the format function as shown below
# you can also add a number (i.e. 04 below) to add padding to the front of a number
# which means that the first number will print with 6 digits (including the decimal point)
# and add any additional digits as zeros in front of the number
integer_number = 6
float_number = 5
print("Here is first variable passed into format {:06.2f} and here is the second {:.2f}".format(integer_number, float_number))

####################################################################################################

# lastly you can use lists (which will be explored more later) to format and directly
# input an item into a string. numbers[0] would represent the first number in the list
numbers = [3, 6, 9]
song_lyric = "{0} {1} {2}, transit line".format(numbers[0], numbers[1], numbers[2])

print(song_lyric)

####################################################################################################

# this would produce the same output as the line above. you can set the variable to be printed inside
# the format function allows you to set the variable inputs in the function
numbers = [3, 6, 9]
song_lyric = "{first} {second} {third}, transit line".format(first="three", second="six", third="nine")

print(song_lyric)

#####################################################################################################

# as we explored above, this is a list. students[0] would be "Marcus", students[1] would
# be "Gary", and so on
students = ["Marcus", "Gary", "Francine"]
attendance_output = "The present students are {}, {}, and {}".format(students[0], students[1], students[2])
print(attendance_output)

# TODO: Section 2 of TODO 3
####################################################################################################

# the join function combines items in a list. in this case, it will create a large string
list_to_join = ["combine", "these", "words", "into", "one", "string"]

# the first input specifies how to join the items in the list. It will join them with a comma
print(",".join(list_to_join))

# these methods will not change the original list. as you can see from this output, it stays the same
print('as you can see, the list has not changed', list_to_join)

# if you wanted to capture the new value of combining the items in the list, you would have
# to set it equal to a new variable like this:
new_var = "".join(list_to_join)
print("this is the new var: ", new_var)

# but that looks kind of silly without spaces! Lets join them with a space instead to see
# the better outcome. We can reassign the new_var variable to have this new value.


new_var = " ".join(list_to_join)
print("this is the new var's updated value: ", new_var)

####################################################################################################

# Split seperates a string into items in a list. The split occurs in the character that you specify.
# For example, in the split we put an empty space. This will split the string into items whenever
# there is a space, so each word will represent an item in the list.
string_to_listify = "lets separate these words into separate items in a list"
print(string_to_listify.split(" "))

# Note: The behavior for the join function also applies to split. It will NOT update the original
# variable. This will still be a string, even though we performed a split function on it.
print(string_to_listify)

# If we wanted to capture the value of that split, we would have to set it equal to a new variable
listified_string = string_to_listify.split(" ")
print(listified_string)

####################################################################################################

# the replace function exchanges one input for another
# lets make this polite statement a little less formal
print("Hey, how are you?".replace("Hey", "Sup"))

####################################################################################################

# startswith returns a boolean value (true/false) on whether or not a string begins with a certain
# set of characters. Lets check if someone is saying hello in the following two statements
print("Hello, I am saying hi to someone".startswith("Hello"))
print("Whats good?".startswith("Hello"))

####################################################################################################

# endswith returns a boolean value (true/false) on whether or not a string ends with a certain
# set of characters. Lets check if these statements are questions
print("Am I a question?".endswith("?"))
print("I'm not a question.".endswith("?"))
