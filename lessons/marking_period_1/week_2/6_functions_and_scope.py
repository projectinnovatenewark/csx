"""
Using functions and understanding scope
"""

# This is a function. Functions are defined using the format `def functionName(parameterName):`
# the parameter name can be anything you want---whatever you pass to the function
# when you call it will be renamed to the argument you pass to the function when defining the function.
def addTen(n):
    newNum = n + 10 # this is within the scope of the function
    return newNum # this is also within the scope of the function

print("This is not a part of the function") # since this line is not indented within the function, it is outside
                                            # the scope of the function and the function definition has therefore ended

# Now that we are at the leftmost part of the page, we have exited the scope of the function above.
# This function should now take the argument passed, which is 3, and add ten to it. It will then return
# that value. What you see below is called "calling a function", which basically runs the function above.
print("First call to addTen function: ")
addTen(3)

# Huh, why didnt this function call create an output?! Well, we didn't print it!! We could either
# 1) change the "return" value to be a print statement...or
# 2) we can print the function call itself!

# To do it the first way, you would just replace "return newNum" with "print(newNum)" within the
# function definition

# To do it the second way, do this. This would essentially print the return value of the function
print("Second call to addTen function: ")
print(addTen(5))

# Functions also don't NEED parameters. They can perform some operation that doesn't require an argument.
# In this case, we will just print a "global" variable that would be accessible by the whole file- including
# within the scope of this function!
randomNumVar = 12345
def outputOurNumber():
    print(randomNumVar)

# This would call the above function which would print out the randomNumVar variable.
print("Calling our outputOurNumber function: ")
outputOurNumber()

####################################################################################################

# Calling functions within other functions and using their return values.
# Having return values from functions is important when you want to use that value,
# and not just log it in that moment. Here is an example of one such case:

def daysActivities(typeOfDay):
    """Analyze a user's input and return a message for them"""
    dayString = ""
    # These if statements check to see if the typeOfDay argument is equal to something- in our case
    # we are checking in three different statements if typeOfDay is either "fun", "productive",
    # or "lazy". If one of those if's is true, then we do whatever is within the scope of that if
    # block. If none of the if statements are true, we execute what is in the "else" block.

    if (typeOfDay == "fun"):
        dayString = "You should enjoy some of your favorite activities"
    if (typeOfDay == "productive"):
        dayString = "Let's get some work done, player!"
    if (typeOfDay == "lazy"):
        dayString = "You work too hard, and this day is all about YOU. Do NOTHING and enjoy it, you deserve it :)"
    else:
        dayString = "I can only compute one of the three provided types of days. Try again, chief!"

    # This will return the variable dayString and end the function. When a return statement is run,
    # the function will effectively stop running.
    return dayString

def inquireDay():
    """This function will ask the user what type of day they want to have"""

    # We will take the user input value and pass it as an argument to our "daysActivities" function.
    userDay = input("What type of day do you want to have? You can choose from fun, productive, or lazy. Enter your choice!: ")

    # This variable below would be equal to the return value of the function call
    userMessage = daysActivities(userDay)
    print(userMessage)

# This is a regular old function call
inquireDay()

####################################################################################################

# here are a couple of dictionaries
EXAMPLE_DICTIONARY_ONE = {"Abigail": 78, "Brian": 86, "Carlito": 95, "Debbie": 100, "Erion": 88}
EXAMPLE_DICTIONARY_TWO = {"Andy": 73, "Brovan": 90, "Celeste": 65, "Danilo": 84, "Epsilo": 78}

# One important concept of functions is that they can be reused. Therefore, we can execute the
# same function to perform operations on BOTH of the above dictionaries.
def dictionary_reader(dictionary):
    """This function will format and print a dictionary. Just as a file gets a doc string, functions get one too!"""
    print("Let's output a dictionary")

    for student in dictionary:
        print(student + " got a score of " + str(dictionary[student]) + " on their exam!")

    print("This function has finished running.")

# Here we pass the function an argument for our first dictionary
dictionary_reader(EXAMPLE_DICTIONARY_ONE)

# Here we see the same function performing operations with our second argument
dictionary_reader(EXAMPLE_DICTIONARY_TWO)

####################################################################################################

# below are examples by using variables & the timing of a function call to portray scope
# here we call "s" after the function is called, which will return a NameError
def func():
    print(s)
func()
s = "I love Paris in the summer!"

####################################################################################################

# here, since the variable is declared before the function is called, it will print the "s2" value
def func2():
    print(s2)
s2 = "I love San Diego in the summer!"
func2()

####################################################################################################

# here, the variable in the function is referenced within the function's scope, therefore it will
# print the "I love London" statement
def func3():
    s3 = "I love London!"
    print(s3)

s3 = "I love Malaysia!"
func3()

print(s3)
