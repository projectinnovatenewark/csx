"""
if, else, elif, while, and try/except/else with error handling
"""

num = 3

if num > 0:
    print(num, "is a positive number.")
elif num < 0:
    print(num, "is a negative number.")
else:
    print(num, "is a zero value.")

# notice how we used the same variable of "num" but reassigned its value- we can
# do that because it is a variable and NOT a constant

num = 533

if num % 2 == 0:
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")

# lets take 12 and subt
countdown = 12
countdown_sum = 0
