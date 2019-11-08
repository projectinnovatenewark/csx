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
print(first_name.title()) # this title-izes the first name

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

# this would produce the same output as the line above. you can set the variable to be printed inside 
# the format function allows you to set the variable inputs in the function
song_lyric = "{first} {second} {third}, transit line".format(first="three", second="six", third="nine")

print(song_lyric)

# the join function combines multiple strings into one from a list
list_to_join = ["combine", "these", "words", "into", "one", "string"]
print(",".join(list_to_join))

# split seperates a string into a list. the split occurs in the character that you specify
# i.e. a period as shown below splits the string every time a period is shown
string_to_listify = "combine, these, words, into, one, string"
print(string_to_listify.split(","))

# the replace function exchanges one input for another
# lets make this polite statement a little less formal
print("Hey, how are you?".replace("Hey", "Sup"))


# startswith returns a boolean value (true/false) on whether or not a string begins with a certain
# set of characters. Lets check if someone is saying hello in the following two statements
print("Hello, I am saying hi to someone".startswith("Hello"))
print("Whats good?".startswith("Hello"))

# endswith returns a boolean value (true/false) on whether or not a string ends with a certain
# set of characters. Lets check if these statements are questions
print("Am I a question?".endswith("?"))
print("I'm not a question.".endswith("?"))
