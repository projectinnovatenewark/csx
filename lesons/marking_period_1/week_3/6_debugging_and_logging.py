"""
How to debug
"""

def isPrime(n):
    truth_val = True
    for n in (2,n):
        if (num % n == 0):
            truth_val = False
            print("Condition is satisfied")
            break
    return truth_val 

num = 15
def num_analyzer():
    while (num > 0):
        if num % 2 == 0:
            print (num, "is an even number")
        if num % 2 == 0:
            print (num, "is an odd number")
        if isPrime(num) = True
            print(num, "is a prime number")

        num -= 1

num_analyzer(num)

# TODO: the above code is broken, here are the steps to fix it.
# Step 1: Double check for syntax errors (colons, tabulation/scope, parentheses, general syntax)
# Step 2: Log functions to test if itis being called


# Program that describes if a number is Even, Odd, and/or Prime
# Solution to deBugging lesson

num = int(input("Enter a number: ")) #Input a number do five num a value

def numAnalyzer(num):
    while (num > 0):
        if(num % 2 == 0): # Checks if num is Even
            print(num, "is an even number")
        if(num % 2 != 0): # Checks if num is odd
            print(num, "is an odd number")
        if(isPrime(num)): # Checks if num is Prime [See inPrime function]
            print(num, "is a prime number")
        num -= 1 # Decriments num

def isPrime(n): # n is an arbitrary value. When you call the function later, you decide what value to pass.
    truthVal = True
    for range_number in range(2, n): # a is each value inbetween 2 and the arbitrary value.
        if(n % range_number == 0): # checks if the value passed is divded cleanly by the value in the range
            truthVal = False
            break
    return truthVal

numAnalyzer(num)

# FIXME: this code is broken and has explanations of what is wrong with it

def isPrime(n):
    truth_val = True
    for n in (2,n): #missing range function; avoid double-assigning variable in for loop and range function; re-name for loop variable
        if (num % n == 0): #argument in if statement should start with arbitrary number THEN for range variable 
            truth_val = False
            print("Condition is satisfied") #this is an exmple of logging to check if the function is at least being tested.
            break
    return truth_val 

num = 15
def num_analyzer(): #argument needed in function definition
    while (num > 0):
        if num % 2 == 0: #argument for if must be in parentheses
            print (num, "is an even number")
        if num % 2 == 0: #argument for if must be in parentheses; make sure the arguments you pass are correct. 
            print (num, "is an odd number")
        if isPrime(num) = True #arg for if must be in parentheses; True is not needed 
            print(num, "is a prime number")

        num -= 1

num_analyzer(num)

