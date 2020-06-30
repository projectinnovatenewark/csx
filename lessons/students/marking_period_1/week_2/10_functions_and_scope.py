"""
Using functions and understanding scope
"""

# A function is a block of code that executes some task. Functions are defined using the format
# `def functionName(parameterName):` The parameter name can be anything you want---whatever you pass as
# an argument to the function when you "call" it will be renamed to the parameter you set when defining the function.
# To "call" a function simply means to run it.
def addTen(n): # "addTen" is the name of the function and "n" is the parameter name
    newNum = n + 10 # this is within the scope of the function
    return newNum # this is also within the scope of the function

print("This is not a part of the function") # since this line is not indented within the function, it is outside
                                            # the scope of the function and the function definition has therefore ended

# Now that we are at the leftmost part of the page, we have exited the scope of the function above.
# This function should now take the argument passed, which is 3, and add ten to it. It will then return
# that value. What you see below is called "calling a function", which basically runs the function with the given input.
print("First call to addTen function: ")
addTen(3) # "3" is the argument we pass, which will be assigned to the variable "n" within the function call.

# Huh, why didnt this function call create an output?! Well, we didn't print it!! We could either
# 1) change the "return" value to be a print statement in the function
# ...OR...
# 2) we can print the function call itself!

# To do it the first way, you would just replace "return newNum" with "print(newNum)" within the
# function definition

# To do it the second way, do this. This would essentially print the return value of the function
print("Second call to addTen function: ")
print(addTen(5))

# Functions also don't NEED parameters. They can perform some operation that doesn't require an argument.
# In this case, we will just print a "global" variable that would be accessible to the whole file- including
# within the scope of this function!
randomNumVar = 12345
def outputOurNumber():
    print(randomNumVar)

# This would call the above function which would print out the randomNumVar variable.
print("Calling our outputOurNumber function: ")
outputOurNumber()

####################################################################################################

# Calling functions within other functions and using their return values.
# Here we will show you how the "control" of a program will navigate the code.

def addTwo(j):
    newNum = j + 2
    return newNum # Control 3: "j", which is equal to the argument of 9 that was passed, has 2
                  # added to it and 11 is returned.

def addFive(k):
    return k + 5 # Control 6: "k", which is equal to the arugment of 11 that was passed, has 5
                 # added to it and that valur of 16 is returned.

def addingChain(i):
    curr_num = addTwo(i) # Control 2: addTwo function is called and passed "i", which is equal to 9
    # Control 4: The value of 11 that was returned from the addTwo function call is set to a
    # variable called curr_num

    new_num = addFive(curr_num) # Control 5: addFive function is called and passed curr_num, which is equal to 11
    # Control 7: The value of 16 that was returned from the addFive function call is set to a
    # variable called new_num

    return new_num # Control 8: The new_num variable, which equals 16, is returned and the
                   # addingChain function call has ended

print(addingChain(9)) # Control 1: the addingChain function gets called and passed 9 as an argument
# Control 9: After the function call is complete, the print statement prints the return value.

####################################################################################################

# Calling functions within other functions and using conditions.

# Having return values from functions is important when you want to use that value,
# and not just log it in that moment. Here is an example of one such case:

def daysActivities(typeOfDay):
    """Analyze a user's input and return a message for them"""
    # These if statements check to see if the typeOfDay argument is equal to something- in our case
    # we are checking in three different statements if typeOfDay is either "fun", "productive",
    # or "lazy". If one of those if's is true, then we do whatever is within the scope of that if
    # block. If none of the if statements are true, we execute what is in the "else" block.

    if (typeOfDay == "fun"):
        dayString = "You should enjoy some of your favorite activities"
    elif (typeOfDay == "productive"):
        dayString = "Let's get some work done, player!"
    elif (typeOfDay == "lazy"):
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

# TODO: Hey, Teach! You should have your students walk you through the control of the above function
# TODO: call. Make sure the class understands the flow of the program 🚀

####################################################################################################

# here are a couple of dictionaries
EXAMPLE_DICTIONARY_ONE = {"Abigail": 78, "Brian": 86, "Carlito": 95, "Debbie": 100, "Erion": 88}
EXAMPLE_DICTIONARY_TWO = {"Andy": 73, "Brovan": 90, "Celeste": 65, "Danilo": 84, "Epsilo": 78}

# One important concept of functions is that they can be reused. Therefore, we can execute the
# same function to perform operations on BOTH of the above dictionaries.
def dictionary_reader(dictionary):
    """This function will format and print a dictionary. Just as a file gets a doc string, functions get one too!"""
    print("Let's output a dictionary")
    print("\n")

    for student in dictionary: # TODO: Hi Teacher! Let's show how we can set a variable of grade to
                               # TODO: access every student's grade, then use that in our print statement.
        print(student + " got a score of " + str(dictionary[student]) + " on their exam!")

    print("\n")
    print("This function has finished running.")

# Here we pass the function an argument for our first dictionary
dictionary_reader(EXAMPLE_DICTIONARY_ONE)

print("\n")

# Here we see the same function performing operations with our second dictionary
dictionary_reader(EXAMPLE_DICTIONARY_TWO)

###################################################################################################

# Below are examples of using variables & the timing of a function call to portray scope.
# Here we call "s" after the function is called, which will return a NameError
def func():
    print(s)
func()
s = "I love Paris in the summer!"

####################################################################################################

# Here, since the variable is declared before the function is called, it will print the "s2" value
def func2():
    print(s2)
s2 = "I love San Diego in the summer!"
func2()

####################################################################################################

# Here, the variable in the function is referenced within the function's scope, therefore it will
# print the "I love London" statement
def func3():
    s3 = "I love London!"
    print(s3)

s3 = "I love Malaysia!"
func3()

print(s3)
