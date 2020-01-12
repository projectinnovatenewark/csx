"""
This is an introduction to string manipulation in Python
"""

# with the input function, you can get input from users
# lets set the user inputs equal to variables, then use them appropriately
first_name = input("What is your first name?: ")
last_name = input("What is your last name?: ")

# since the values you input are set to variables, we can concatenate the strings
print("My first name is " + first_name + " and my last name is " + last_name)

# you can also seperate variables in concatenation with commas. this is the preferred
# method of concatenation. we try not to build the string using simple addition, since
# that is quite slow in Python (strings are immutable objects, so each string addition
# involves creating a new string of the right length and copying the content of the two
# strings being added).
var_one = "scooby"
var_two = "doo"
print("Hello, my name is", var_one, var_two)

# go back to the end of the input variables we've set and add .title() to the end of the line
# the title() function capitalizes a variable
print(first_name.title()) # this title-izes the first name


##############################################################################################

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

# the python 3 way to do the above is strictly by using the format function as shown below
# you can also add a number (i.e. 04 below) to add padding to the front of a number
# which means that the first number will print with 6 digits (including the decimal point)
# and add any additional digits as zeros in front of the number
integer_number = 6
float_number = 5
print("Here is first variable passed into format {:06.2f} and here is the second {:.2f}".format(integer_number, float_number))

##############################################################################################

# lastly you can use lists (which will be explored more later) to format and directly
# input an item into a string
numbers = [3, 6, 9]
song_lyric = "{0} {1} {2}, transit line".format(numbers[0], numbers[1], numbers[2])

print(song_lyric)

# this would produce the same output as the line above. you can set the variable to be printed inside 
# the format function allows you to set the variable inputs in the function
song_lyric = "{first} {second} {third}, transit line".format(first="three", second="six", third="nine")

print(song_lyric)

##############################################################################################

# the join function combines items in a list. in this case, it will create a large string
list_to_join = ["combine", "these", "words", "into", "one", "string"]

# the first input specifies how to join the items in the list. It will join them with a comma
print(",".join(list_to_join))

# but that looks kind of silly! Lets join them with a space instead to see the better outcome.
print(" ".join(list_to_join))

# split seperates a string into items in a list. the split occurs in the character that you specify
# for example, in the split we put an empty space. This will split the string into items whenever
# there is a space, so each word will represent an item in the list.
string_to_listify = "lets separate these words into separate items in a list"
print(string_to_listify.split(" "))

##############################################################################################

# the replace function exchanges one input for another
# lets make this polite statement a little less formal
print("Hey, how are you?".replace("Hey", "Sup"))

##############################################################################################

# startswith returns a boolean value (true/false) on whether or not a string begins with a certain
# set of characters. Lets check if someone is saying hello in the following two statements
print("Hello, I am saying hi to someone".startswith("Hello"))
print("Whats good?".startswith("Hello"))

##############################################################################################

# endswith returns a boolean value (true/false) on whether or not a string ends with a certain
# set of characters. Lets check if these statements are questions
print("Am I a question?".endswith("?"))
print("I'm not a question.".endswith("?"))
