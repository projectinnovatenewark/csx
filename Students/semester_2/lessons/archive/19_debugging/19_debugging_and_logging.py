"""
Fix this broken code and teach students what debugging looks like
"""

# FIXME: this code is broken and has explanations of what is wrong with it. also, change the
# FIXME: variable of num = 15 so that a variable of num takes in a user input. num_analyzer 
# FIXME: should test every number from the user input all the way down to on.

def isPrime(n):
    """isPrime should take a number as an argument and return true if it is prime or false if it is not"""
    truth_val = True
    # FIXME: this problem was supposed to range through numbers between 2 and n
    for n in (2,n): #missing range function; avoid double-assigning variable in for loop and range function; re-name for loop variable
        if num % n == 0: #argument in if statement should start with arbitrary number THEN for range variable 
            truth_val = False
            print("Condition is satisfied") #this is an exmple of logging to check if the function is at least being tested.
        break # when would this break statement occur?
    return truth_val

isPrime(13)

####################################################################################################

def num_analyzer(): #argument needed in function definition
    """numAnalyzer should accept an argument and return if it is even or false AND if it is prime
    it shold test from every number """
    # FIXME: this problem is supposed to decrement by one to test
    # FIXME: all numbers between argument passed and zero
    while (num > 0):
        if num % 2 == 0: #argument for if must be in parentheses
            print (num, "is an even number")
        if num % 2 == 0: #argument for if must be in parentheses; make sure the arguments you pass are correct. 
            print (num, "is an odd number")
        if isPrime(num) = True #arg for if must be in parentheses; True is not needed
            print(num, "is a prime number")

        num = 1

num_analyzer(15)