"""
Using functions and understanding scope
"""

# here are a couple of dictionaries
EXAMPLE_DICTIONARY = {"Abigail": 78, "Brian": 86, "Carlito": 95, "Debbie": 100, "Erion": 88}
EXAMPLE_DICTIONARY_TWO = {"Andy": 78, "Brovan": 86, "Celeste": 95, "Danilo": 100, "Epsilo": 88}

# this is a function. Functions are defined using def functionName(argumentName):
# the argument name can be anything you want---whatever you pass to the function
# when you call it will be renamed to the argument you set it to when defining the function
def dictionary_reader(dictionary):
    """this function will format and print a dictionary"""
    print("Let's output a dictionary")

    for student in dictionary:
        print(student + " got a score of " + str(dictionary[student]) + " on their exam!")

    print("Completed dictionary output")

# now that we are at the leftmost part of the page, we have exited the scope of the function above
dictionary_reader(EXAMPLE_DICTIONARY_TWO)

##################################################################################################

# below are examples by using variables & the timing of a function call to portray scope
# here we call s after the function is called, which will return a NameError
def func():
    print(s)
func()
s = "I love Paris in the summer!"

##################################################################################################

# here, since the variable is declared before the function is called, it will return the s2 value
def func2():
    print(s2)
s2 = "I love Paris in the summer!"
func2()

##################################################################################################

# here, the variable in the function is referenced within the function's scope, therefore it will
# print the "I love London" statement
def func3(): 
    s3 = "I love London!"
    print(s3) 

##################################################################################################

s3 = "I love Paris!"
func3()
print(s3)