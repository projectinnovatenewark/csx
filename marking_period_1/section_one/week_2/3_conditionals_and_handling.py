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

# notice how we used the same variable of "num" but reassigned its value- we can
# do that because it is a variable and NOT a constant

num = 533

if num % 2 == 0:
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")

# lets take 12 and add each number between it and zero to a variable (i.e. 12 + 11 + 10.....0)
countdown = 12
countdown_sum = 0

while countdown > 0:
    countdown_sum += countdown
    countdown -= 1
    print("countdown equals", countdown)
    print("countdown sum equals", countdown_sum)

print("countdown now equals", countdown)

print(countdown_sum)
