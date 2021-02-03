"""
Solve the below using helper functions
"""

# Context: Solving all of the problems below in one function would be kind of weird and not produce
# the prettiest code. You should break the function up into smaller, "helper" functions.

# Definitions for support: A prime number is a whole number greater than 1 whose only factors are 1 and
# itself. A factor is a whole number that can be divided evenly into another number.

# Tip: Test your helper functions out along the way! Make sure they work on their own before trying
# to solve the whole problem in one shot.

num_list = [12, 15, 22, 13, 17, 11]

# TODO: Define a helper function called "isPrime" and pass it an argument of "num".
# TODO: The function should determine whether or not the number is a prime number.
# TODO: It should return a string indicating "is prime" or "is not prime".

# TODO: Hint: Let's think. If a prime number is only evenly divisible by itself and 1...
# TODO: then if any number between 2 and itself minus one were to be a factor, the
# TODO: number would not be prime! So...you may want to iterate through numbers between 2 and
# TODO: the num argument minus one. With each of those numbers, you should check if there is a
# TODO: remainder using the modulo operator.

# TODO: Define a helper function called "isEven" and pass it an argument of "num".
# TODO: It should return a string indicating "is even" or "is odd".

# TODO: Finally, define a function called "main" that sets a parameter "listy". The argument passed
# TODO: will be num_list. The main() function should iterate through these numbers and call the above functions
# TODO: and produce an output for each, formatted as "Number ___("is even" or "is odd") and ("is prime" or
# TODO: "is not prime")."
