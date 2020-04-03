"""
Using functions and understanding scope
"""

# functions are blocks of code that execute when called upon. a function definition is the naming
# of these set of instructions. `def functionName([arguments-if-needed]):` is the format.
# functions can take an argument and do things with it inside the function. if you want to
# create a function that adds 10 to any given number and prints the new number, you would
# write something like this:

def addTen(x): # the parameter, in this case 'x', is sometimes called an alias for the actual
               # argument that is passed
    newNum = x + 10
    print(newNum)

# then to call this function and pass it an argument of a number, do this
addTen(5)

# remember, if we wanted to set a number equal to a variable and pass that variable, it would be
# doing the same thing
num = 23
addTen(num)

##################################################################################################

#  we can also set two parameters for functions!
def doMultiplier(number, multiplier):
    solution = number * multiplier
    print(number, "times", multiplier, "would equal", solution)

# Order matters here- make sure to pass the arguments in the correct order!
# In this case, 25 would be assigned to "number" and 4 would be assigned to "multiplier".
doMultiplier(25, 4)

##################################################################################################

# here are a couple of dictionaries
EXAMPLE_DICTIONARY = {"Abigail": 78, "Brian": 86, "Carlito": 95, "Debbie": 100, "Erion": 88}
EXAMPLE_DICTIONARY_TWO = {"Andy": 90, "Brovan": 75, "Celeste": 88, "Danilo": 60, "Epsilo": 85}

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
dictionary_reader(EXAMPLE_DICTIONARY)
dictionary_reader(EXAMPLE_DICTIONARY_TWO)

##################################################################################################

# Lets show how a return value from a dictionary can be set equal to a variable
def grade_average_calculator(dictionary):
    """this function will add the total of grades and divide
    it by the number of students to calculate the average"""

    gradeTotal = 0
    numberOfStudents = 0

    for student in dictionary:
        # this variable would access the value of each key value pair for
        # every iteration
        grade = dictionary[student]

        # lets add every grade to the grade total to find an average
        gradeTotal += grade

        # lets add 1 to the numberOfStudents variable for each iteration
        # to find the total number of students
        numberOfStudents += 1

    average = gradeTotal / numberOfStudents

    return average

# this variable would be equal to the return value from the function being called
class_one_average = grade_average_calculator(EXAMPLE_DICTIONARY)
print('the function run to calculate the first class average returned a value of', class_one_average)

class_two_average = grade_average_calculator(EXAMPLE_DICTIONARY_TWO)
print('the function run to calculate the second class average returned a value of', class_two_average)

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