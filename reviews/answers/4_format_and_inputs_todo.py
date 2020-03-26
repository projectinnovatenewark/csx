"""
Test your format and input knowledge
"""

# TODO: Use input that reads "Input a number: " and set it to the variable name num

num = input("Input a number: ")

# TODO: Then print that number with 3 decimal points. 
# It should look something like this: 50.000

print("{:.3f}".format(int(num)))

# TODO: Use input to ask for the users first name and last name and set them to the variables
# TODO: first_name and last_name respectively. 

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")

# TODO: Use format() to print the sentence "My first name is ____ and my last name is _____."

print("My first name is {} and my last name is {}.".format(first_name, last_name))

# TODO: Use a for loop to print the statement 
# TODO: "____'s favorite basketball player is ______." using the fav_players dictionary and format()

fav_players = {"John": "Lebron James", "Natasha": "Paul George", "Mark": "Russel Westbrook"}

for fan in fav_players:
    player = fav_players[fan]
    print("{}'s favorite basketball player is {}.".format(fan, player))