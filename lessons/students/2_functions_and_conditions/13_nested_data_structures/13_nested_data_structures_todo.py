"""
Practice using nested for loops to iterate through different data structures
"""

# TODO: Section 1:

# Hint! Remember that None is basically setting something as an undefined value. This is helpful when
# you intend on being specific about the scope of a variable and wanting to populate it later
# TODO: Create a series of for loops that prints out each day of the week with the 
# TODO: high and low of each day in this problem, the high and low of 
# TODO: each period of the day is set in the array in the key value pair

ADVANCED_FORECAST = {
    "Sunday": [42, 55, 52],
    "Monday": [40, 50, 51],
    "Tuesday": [55, 65, 59],
    "Wednesday": [50, 60, 48],
    "Thursday": [52, 59, 53],
    "Friday": [42, 50, 41],
    "Saturday": [43, 51, 47]
}


# TODO: ###########################################################################################

# TODO: Section 2:

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

def transactify(transactions):
    """this function should complete the above tasks"""
transactify(transactions_data) 
