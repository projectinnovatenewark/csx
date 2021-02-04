"""
  Pre-Reqs:
  vars_and_types,
  basic_math,
  imports,
  functions_and_scope,
  Sem 1 - Workshop_2: Pseudocode,
  classes
"""

# FIXME: Add import here
from random import randrange

# TODO: E-1 (1 minute)

# First, import the "randrange()" function from the "random" module. The randrange function will
# return a value between a lower bound and upper bound non-inclusive. For example, the function call
# "randrange(1,11)" will return a random number between 1 and 10.

# TODO: E-2

# Define a function called "evaluateRand()" that will take a parameter of "rand_num". The variable
# rand will be evaluated through a series of conditionals within the scope of this function. We want
# to test the following conditions:
  
  # 1. If rand_num is even print, "[rand_num] is an even number." If the previous statement returns
  # false print, "[rand_num] is an odd number."
  # HINT:
  # A number is even if it can be evenly divided by 2, meaning it has a remainder of 0. What 
  # mathematical operator is used to find the remainder of a given quotient.

  # 2. If rand_num is greater than 50 print the statement, "[rand_num] is greater than 50." If
  # the previous statement returns false and rand_num is greater than or equal to 30 print the
  # statement, "[rand_num] is greater than or equal to 30." If all statements above are false print,
  # "[rand_num] is less than 30."

# Outside of the function's scope, store the "randrange()" function call with a lower bound of 1 and
# includes up to 100 in a variable called "rand". 

# Call the "evaluateRand()" function and pass "rand" as an argument.

def evaluateRand(rand_num):
  if (rand_num % 2 == 0):
    print(f"{rand_num} is an even number.")
  else:
    print("odd baby")
  
  if (rand_num > 50):
    print("impressive rectangle")
  elif (rand_num >= 30):
    print("ok sized rectangle")
  else:
    print("get this rectangle out of here")

rand = randrange(1,101)

evaluateRand(rand)