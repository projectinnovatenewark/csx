"""
Solve the problems below using helper functions.
"""

# TODO:
# Create a program that takes a list of numbers, determines if each number is prime, and determines
# if each number is even or odd.

# The function "isPrime()" is already defined for you and will return True if the integer passed
# as an argument is a prime number or False if the integer is not a prime number.

# IMPORTANT:
# A prime number is a whole number greater than 1 whose only factors are 1 and itself. A factor is
# a whole number that can be divided evenly into another number.

# TODO:
# Define a helper function called "isEven()" and pass it an argument of "num". It should return a
# string indicating "{num} is even" or "{num} is odd".

# TODO:
# Define a function called "main()" that uses a parameter "listy". The argument passed will be
# "num_list" which is defined below. The "main()" function should iterate through these numbers and
# call both "isPrime()" and "isEven()" for each iteration. Store the function call of "isPrime()" in
# a variable called "is_prime" and the function call of "isEven()" in a variable called "is_even".

# TIP: The following 4 lines are examples of potential outputs from the "main()" function. This is
# TIP: the format that should be followed for solving this problem.
# "The number num is odd and prime."
# "The number num is odd and not prime."
# "THe number num is even and prime."
# "THe number num is even and not prime."

# TIP: Test your helper functions out along the way. Make sure each helper function works
# TIP: individually before trying to solve the whole problem in one shot.

num_list = [12, 15, 22, 13, 17, 11]

# TODO: Hey Teacher, make sure the students understand how "isPrime()" works.
def isPrime(num):
  is_prime = True

  for n in range(2,num):
    if (num % n == 0):
      is_prime = False
      break
  return is_prime
