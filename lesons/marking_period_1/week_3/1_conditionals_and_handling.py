"""
if, else, elif, while loops
"""

num = 3

if num > 0:
    print(num, "is a positive number.")
elif num < 0:
    print(num, "is a negative number.")
else:
    print(num, "is a zero value.")

##################################################################################################

# notice how we used the same variable of "num" from the above function but reassigned its value..
# we can do that because it is a variable and NOT a constant

num = 533

if num % 2 == 0:
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")

##################################################################################################

# lets take 12 and add each number between it and zero to a variable (i.e. 12 + 11 + 10.....0)
countdown = 12
countdown_sum = 0

while countdown > 0:
    countdown_sum += countdown # += or -= will add/subtract a number to a variable and then
                               # reassign the NEW value to that variable

    countdown -= 1 # in this case of -= it will subtract one from countdown and then countdown will
                   # equal countdown - 1. so, in the first iteration of the while loop, countdown
                   # will go from 12 to 11
    print("countdown equals", countdown)
    print("countdown sum equals", countdown_sum)

# this code below the while loop will NOT run until the while loop 'breaks', which would happen when
# the condition of countdown > 0 is no longer true
print("countdown now equals: ", countdown)

print("the final countdown equals: ", countdown_sum)

##################################################################################################

number_list = [3, 15, 31, 1, 11, 107]

# all is helpful when you want to assess every value of a set
# lets check if all the numbers are odd
if all(numbers % 2 != 0 for numbers in number_list):
    print("all the numbers are odd")

# ##################################################################################################

# not in checks to see if an item is not in a list
if (1000000 not in number_list):
    print("there is not one million in the number list")

##################################################################################################

# any is helpful when you want to see if a single value (or more!) satisfies your conditional
if any(numbers % 2 == 0 for numbers in number_list):
    print("there is at least one even number")

##################################################################################################

# enumerate gives you the index value and actual value of values in a list
for numbers in enumerate(number_list):
    print(numbers)

# ##################################################################################################

# switch statements are common in other languages. What a switch statement does is take a
# case and apply it. Say you want to know what the name of the day is by it's place in the
# week. This function is the equivalent of a switch case

def week(i):
    """this function serves as a switch case equivalent in Python"""

    switcher = {
        0:'Sunday',
        1:'Monday',
        2:'Tuesday',
        3:'Wednesday',
        4:'Thursday',
        5:'Friday',
        6:'Saturday'
    }
    # this will return the printed statement of the number being passed as an argument
    # or it will return "invalid day of the week" if that number isn't in the switcher dictionary
    return print(switcher.get(i, "Invalid day of week"))

week(3)
