
"""
NEXT ADVANCED LESSON
SOLID principles
"""

# review optional arguments and advanced functions including
# nested for loops, conditionals, and possibly use packages

# link on optional args: https://stackoverflow.com/questions/9539921/how-do-i-create-a-python-function-with-optional-arguments

# include lambdas, map, filter, reduce, higher order functions

# Lambdas/Anonymous functions
def raiseToTheFourth(n):
    return n*n*n*n

# This is an anonymous function that will take an argument of "x" and perform the operations after the colon.
# It can accept multiple arguments but only return one expression.
fourth = lambda x: x*x*x

print(fourth(7))
print(raiseToTheFourth(5))

##################################################################################################

# A higher order function is a function that contains either functions as an argument or returns a
# function as an output
def shout(text):
    return text.upper() # here we are returning a function being called on a string,
                        # making this a higher order function

def whisper(text):
    return text.lower()

def proper(text):
    return text.title()

def greet(func):
    # here you can see the argument being passed is used as a function call- we can assume
    # that this function is meant to be passed a function as an argument. It also shows how
    # function calls can be stored in variables- something we've seen prior to this lesson.
    greeting = func("should i YELL or whisper?")
    print(greeting)

# in the three following function calls, we are passing previously defined functions as arguments
greet(shout)
greet(whisper)
greet(proper)

##################################################################################################

# Your higher order functions can also return function calls. Here is an example including
# a "partial" function call. While the adder function is defined within the scope of create_adder,
# our next example will display using a function from the global scope.
def create_adder(x):
    print('x', x)
    def adder(y):
        print('x, y: ', x, 'and', y)
        return x + y
    # the create_adder function returns a different function call
    return adder

# This variable is being set equal to a partial function call. However, even though we passed "x" to
# "create_adder", we need to pass add_8 another argument so that the inner "adder" funtion that's
# returned is passed a "y" argument.
add_8 = create_adder(8)

# Since the above variable returns a function- we will need to pass an argument to that return
# function to call it.
add_second_num = add_8(6)

print(add_second_num)

##################################################################################################

#
