"""
example recursion functions
"""

def fibonacci(num):
    """use recursion to complete a fibonacci sequence"""
    if num < 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif num == 1:
        return 0
    # Second Fibonacci number is 1
    elif num == 2:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)

print(fibonacci(9))
