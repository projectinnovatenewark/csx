"""
rename to 'common coding practices'
Lambdas
Base classes
Switcher
"""

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