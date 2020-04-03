"""
Example recursion functions. reference: https://realpython.com/python-thinking-recursively/
"""

# the first example we will review is recursively executing a factorial.
# Factorial multiplies every number by the number before it until it hits 1
# i.e. 5! is equal to 5 x 4 x 3 x 2

# recursion is a functioning that calls itself, thus breaking a large
# problem down into smaller and smaller sub-problems until it is solved

# FIXME: what the heck is this example from???
# def factorial_recursive(n):
#     # Base case: 1! = 1
#     if n == 1:
#         return 1

#     # Recursive case: n! = n * (n-1)!
#     else:
#         return n * factorial_recursive(n-1)

# The Fibonacci sequence is a set of numbers that starts with a one or a zero,
# followed by a one, and proceeds based on the rule that each number
# (called a Fibonacci number) is equal to the sum of the preceding two numbers.
# the first few numbers in the fibonacci sequence are 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

def fibonacci(num):
    """use recursion to find the n'th term in the fibonacci sequence"""
    if (num < 2):
        return num
    else:
        return fibonacci(num-1)+fibonacci(num-2)

print(fibonacci(7))
