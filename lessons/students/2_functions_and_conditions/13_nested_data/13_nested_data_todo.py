"""
Practice using nested for loops to iterate through different data
"""

# TODO: Section 1:

# Below is a nested data structure containing a list of lists called "toppings". Use a nested
# for loop to print each topping.

toppings = [
  ["lettuce", "tomato", "onion"],
  ["bacon", "cheese", "avocado"]
]

####################################################################################################

# TODO: Section 2:

movie_series = {
  "Harry Potter": {
    "Movie 1": "The Sorcerer's Stone",
    "Movie 2": "The Chamber of Secrets",
    "Movie 3": "The Prisoner of Azkaban"
  },
  "Lord of the Rings": {
    "Movie 1": "The Fellowship of the Ring",
    "Movie 2": "The Two Towers",
    "Movie 3": "The Return of the King"
  },
  "The Hunger Games": {
    "Movie 1": "The Hunger Games",
    "Movie 2": "Catching Fire",
    "Movie 3": "Mockingjay"
  }
}

# The nested dictionary "movie_series" contains the first 3 movies in a few popular movie
# franchises. Iterate through "movie_series" and print the statement: "The second movie in the
# [franchise] franchise is [movie]." (i.e The second movie in the The Hunger Games franchise is
# Catching Fire.)

# HINT: Use a nested "for loop" to iterate through "movie_series".

####################################################################################################

# TODO: Section 3:


transactions_data = [
  {
    "amount": 2307.21,
    "place": "Apple Store",
    "acct": "Chase Checking",
  },
  {
    "amount": 75.20,
    "place": "Qdoba",
    "acct": "Wells Savings",
  },
  {
    "amount": 25,
    "place": "Food Depot",
    "acct": "Chase Checking",
  },
  {
    "amount": 10000,
    "place": "Home Depot",
    "acct": "BofA Savings",
  },
  {
    "amount": "1500",
    "place": "Chipotle",
    "acct": "Chase Checking",
  },
  {
    "amount": 1700.56565656,
    "place": "Lowe's",
    "acct": "Chase Checking",
  },
  {
    "amount": 150,
    "place": "AMC Theaters",
    "acct": "Deutsche Bank",
  },
]

# TODO: do all of the below todo's inside a function called "transactify" and pass it an argument
# TODO: which will be the transactions_data list

# TODO: create and print a list of all transactions above $100
# TODO: create and print a list of places we made transactions
# TODO: create and print a list of the bank accounts we use
# TODO: print out each transaction in a string indicating:
# TODO: "You spent $ X at X with your X account"


# Inside the function "transactify", write a program that will print the statement: "You spent
# $[amount] at [location] with your [account]." if the dollar amount was over $100.

# IMPORTANT: Use variables to make your code more readable, as noted in the lesson.

def transactify(transactions):
    """This function should complete the above tasks"""

transactify(transactions_data) 
