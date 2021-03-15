"""
In This lesson, we will go over using functions to perform actions on lists and dictionaries.
"""

unsorted_num_list = [10, 22, 8, 15, 7, 18, 3]

# Here is a long way to create a function and solve the problem above by sorting them.

# unsorted_num_list and putting the sorted items in a new list.
def sort_a_list(data_list):
    """
    This function removes the minimum of out input list, in this case it is 
    'unsorted_num_list' and appends it, (inserts at the 0 index position), 
    to the new list. This is used to sort the integers in the original list into a new list.
    """
    new_list = []

    while data_list:
        minimum = data_list[0]  # arbitrary number in list
        for x in data_list:
            print('x: ', x, 'minimum: ', minimum)
            if x < minimum:
                print('X is less than MIN. x: ', x, 'minimum: ', minimum)
                minimum = x
        new_list.append(minimum)
        data_list.remove(minimum)
        print('End while loop iteration. new_list: ', new_list, 'data_list: ', data_list)

    print(new_list)

sort_a_list(unsorted_num_list)

# This function does the same thing as the function above function.

# An important lesson about becoming a programmer is that you must understand underlying concepts.
# There's always tools to solve your problem quickly with imported functions, but what matters
# is that you understand how those functions work!
print(sorted(unsorted_num_list))

# TITLE: List Comprehension

# List comprehension is a means to create a new list based on the values of an existing list. The
# syntax for using list comprehension is "[expression for x in old_list]" where "expression"
# represents a value and "x" is each item in "old_list". In the example below we are using list
# comprehension to iterate through each number between 0 and 9, squaring the number, and then
# putting it in a list called "squares".
squares = [i**2 for i in range(10)] # IMPORTANT: the "range()" function creates a list of numbers.
print(f"Squares list: {squares}")


# Conditionals can be added to list comprehensions. The conditional is added to the end of the list
# comprehension after the "for loop". In the example below, an "if statement" is used to create a
# list of the square if odd numbers between 0 and 9.
squares_of_odd_numbers = [i**2 for i in range(10) if i % 2 != 0]
print(f"Squares of odd numbers list: {squares_of_odd_numbers}")

####################################################################################################

# In the next 3 sections, you can see that the condition actually comes before the "for" statement.
# This differs from list comprehensions, where the action comes before the "for" statement.

number_list = [3, 15, 31, 1, 11, 107]

# `all` is helpful when you want to assess every value of a set
# lets check if all the number are odd
if all(number % 2 != 0 for number in number_list):
    print("all the numbers are odd")

####################################################################################################

number_list = [3, 15, 31, 1, 11, 107]

# `not in` checks to see if an item is not in a list
if (1000000 not in number_list):
    print("there is not one million in the number list")

# `in` checks to see if an item is in a list
if (15 in number_list):
    print("fifteen is in the number list")

####################################################################################################

number_list = [3, 15, 31, 1, 11, 107]

# `any` is helpful when you want to see if a single value (or more!) satisfies your conditional
if any(number % 2 == 0 for number in number_list):
    print("there is at least one even number")

####################################################################################################

number_list = [3, 15, 31, 1, 11, 107]

# `enumerate` gives you the index position and actual value of the items in a list
for number in enumerate(number_list):
    print(number) # enumerate returns you a tuple in the form of (index, value). Remember- tuples are
                  # lists that cannot be changed!
    print(number[0]) # this will be the index number
    print(number[1]) # this will be the item

# TODO: Section 3 of TODO 11
####################################################################################################

# `switch` statements are common in other languages. What a switch statement does is take a
# case and apply it. Say you want to know what the name of the day is by it's place in the
# week. This function is the equivalent of a switch case

def week(i):
    """this function serves as a switch case equivalent in Python"""

    switcher = {
        1:'Sunday',
        2:'Monday',
        3:'Tuesday',
        4:'Wednesday',
        5:'Thursday',
        6:'Friday',
        7:'Saturday'
    }
    # this will return the printed statement of the number being passed as an argument
    # or it will return "invalid day of the week" if that number isn't in the switcher dictionary
    return print(switcher.get(i, "Invalid day of week"))

week(9)
