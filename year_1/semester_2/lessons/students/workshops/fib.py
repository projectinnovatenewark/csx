"""Recursion and the Fibonacci Sequence"""

# TITLE: Basic Recursion with Factorials

# "In computer science, recursion is a method of solving a problem where the solution depends
# on solutions to smaller instances of the same problem. Most computer programming languages
# support recursion by allowing a function to call itself from within its own code" - Wiki.

# In the below code, we will find the factorial of "x". This function will recursively
# call itself until it reaches the base case. Once it finds the solution in the base
# case, it will return that value and resolve the other function calls' return
# values as a result.

# TIP: Reminder that a factorial is a number multiplied by itself and every number
# TIP: between itself and zero (i.e. factorial of 4 is 24 such that 4 x 3 x 2 x 1).

def factorial(x):
  """Find the factorial of an integer"""
  print(f"factorial({x}) was called.")

  # Base Case - this is when the function will stop calling itself recursively
  if x == 1:
    return 1
  else:
    # Recursive function call
    return (x * factorial(x-1))

num = 3
print(f"{num}'s factorial: {factorial(num)}")

# This function call of factorial(3) will recursively call factorial(2), which will
# call factorial(1). Now, think about the following question.

# TODO: Will factorial(1) call factorial(0)? Why or why not?


# The call stack is the functions that call one another when executing.
# factorial(3) will not finish executing until factorial(2) is finished
# executing, and that pattern will continue until you hit your base case
# and a function call finishes executing.

# TODO: Joint exercise - walk through a call stack for factorial(3) and include return values.


###################################################################################################

# TITLE: Recursion Trees and the Fibonacci Sequence

# Fibonacci' Formula- add up the previous two positions in the fibonacci sequence to find
# the next number.
# n'th position- 1 2 3 4 5 6
# fibonacci val- 1 1 2 3 5 8

def fib(n):
  """Find the n'th term in the Fibonacci Sequence"""
  # Base Case
  if n < 2:
    return n
  else:
    # Recursive function calls
    return fib(n-1) + fib(n-2)

print(fib(5))

# Since there are two recursive function calls in this function, we must calculate
# a return value for the first recursive function call of fib(n-1) before we can
# proceed to the next recursive function call of fib(n-2). This is true because
# Python reads top-down/left-right just like written language and will execute
# function calls in that order.

# TODO: Joint exercise: Walkthrough a recursive tree for a function call fib(3).
# TODO: Type out a small tree together.

#                               f5
#                          /           \
#                      f4                f3
#                   /     \             /   \
#                f3       f2          f2     f1
#              /   \     /  \        /  \
#            f2     f1  f1   f0    f1    f0
#          /    \
#        f1      f0

# TODO: Now that you've seen the complete tree, try explaining in your own
# TODO: words how the fib executes fib(5).
