"""
Using functions and understanding scope
"""

# TITLE: Section 1 - Printing Function Outputs (8 minutes)
# A function is a block of code that executes a task. Functions are defined using the following
# format: "def functionName(parameterName):" The parameter name can be anything you want (just like
# variables), so whatever you pass as an argument to the function when you "call" it will be
# renamed to the parameter you set when defining the function. To "call" a function simply means
# to run it.
def addTen(n): # "addTen" is the name of the function and "n" is the parameter name.
  newNum = n + 10 # Lines of code indented after the function is defined are
                  # considered to be in the scope of the function. This is also known as the
                  # function body. The function body gets executed every time the function
                  # is called.
  print("addTen is called\n") 
  return newNum # A return statement indicates the end of a function, meaning there should be no
                # more code in the function after a return statement.

# Now that we are at the leftmost indentation of the file, we have exited the scope of the function
# above. For this reason, the following line is considered outside the scope of the function.
print("This is not a part of the function")
    
    # # FIXME: The below line will throw an Indent Error
    # print("This is not in the scope of 'addTen()'") # FIXME: This will not be in the scope of
    #                                                 # FIXME: addTen() because the function ended
    #                                                 # FIXME: in line 14. Comment it out to continue.

# The function "addTen()" should take an argument of 3, add ten to it, and return the final value.
print("First call to addTen function: ")
addTen(3) # The argument will be assigned to the parameter "n" within the function call.

# Huh, why didnt this function call create an output? Well, we didn't print it! We could either
# 1) change the "return" value to be a print statement in the function
# ...OR...
# 2) we can print the function call itself.

# To create an output, you can set the return value equal to a variable and print it as seen below:
num = addTen(4)
print(f"Second call to addTen function: {num} \n")

# Otherwise, you can print a function call like the following:
print(f"Third call to addTen function: {addTen(5)} \n")

# Parameters aren't mandatory when defining functions, because functions can perform operations that
# don't require an argument. 

num = 12345
def giveOutput():
  print(num)

# In the case above we just print the variable "num", which is considered to be a global variable.
# A global variable is a variable that is accessible to the whole file, including a given function's
# body.

print("Calling our giveOutput function: ")
giveOutput() # This would call "giveOutput()" which would print out num variable.

# TODO: Section 1 of TODO 11 (4 min for students, 1 min for demo)
####################################################################################################

# TITLE: Section 2 - Calling Functions with Other Functions (8 minutes)
# Functions are useful because you can have them "return" a value. These return values can then be
# used elsewhere in your file. Below is an example of how the "control" of a program will navigate
# the code. 

# TODO:
# Hey Teacher, Use the "Control #" flags to bring the students through each control as they are
# executed.

def addTwo(j):
  newNum = j + 2
  return newNum # Control 3: "j", which is equal to the argument of 9 that was passed, has 2
                # added to it and 11 is returned.

added_two = addTwo(3)
print(f"We called 'addTwo' and set it's return value equal to a variable. That variable equals {added_two}")

def addFive(k):
  return k + 5 # Control 6: "k", which is equal to the arugment of 11 that was passed, has 5
               # added to it and that value of 16 is returned.

def addingChain(i):
  curr_num = addTwo(i) # Control 2: The "addTwo()" function is called and passed "i", which is
                       # equal to 9.
  # Control 4: The value of 11 that was returned from the addTwo function call is set to a
  # variable called curr_num.

  new_num = addFive(curr_num) # Control 5: addFive function is called and passed curr_num, which
                              # is equal to 11.
  # Control 7: The value of 16 is returned from the addFive function call and is set to a
  # variable called new_num.

  return new_num # Control 8: The new_num variable, which equals 16, is returned and the
                  # "addingChain()" function call has ended.

print(addingChain(9)) # Control 1: the "addingChain()" function gets called and passed 9 as an
                      # argument.
# Control 9: After the function call is complete, the print statement prints the value of
# "addingChain(9)".

# TODO: Section 2 of TODO 11 (4 min for students, 1 min for demo)
####################################################################################################

# TITLE: Section 3 - Using Return Values with Conditionals (7 minutes)

# Using functions with return values is important when you want to store a value for additional use
# instead just logging it in that moment. Here is an example of this idea in practice:

def daysActivities(type_of_day):
  """Analyze a user's input and return a message for them. Just as a file gets a doc string,
  functions get one too!"""
  # The conditionals below check to see if the "type_of_day" argument is equal to something. In
  # our case we are using a conditional statement to determine if "type_of_day" is "fun". If the
  # conditional is true, then whatever is within the scope of the conditional is executed. If the
  # conditional is not true, the "else" block's code is executed.

  if type_of_day.lower() == "fun":
    day_string = "You should enjoy some of your favorite activities."
  else:
    day_string = "You should try to have some more fun!"

  return day_string # This will return the variable "day_string" and end the function. When a return
                    # statement is run, the function will effectively stop running.

def inquireDay():
  """This function will ask the user what type of day they want to have"""

  # First we will take the user input value and then pass it as an argument to our
  # "daysActivities()" function.
  user_day = input("What type of day do you want to have? You can choose 'fun' or a response of your own. Enter your choice: ")

  user_message = daysActivities(user_day)
  print(user_message) # The variable "user_message" will be equal to the return value of the
                      # function call.

inquireDay() # This is a standard function call without any parameters.

# TODO:
# Hey, Teacher, You should have your students walk you through the control of the above
# function call. Make sure the class understands the flow of the program.

# TODO: Section 3 of TODO 11 (4 min for students, 1 min for demo)
####################################################################################################

# TITLE: Section 4 - Looping in Functions (7 minutes)
# Here are a couple of dictionaries that we will work with for this section.
example_dict_1 = {"Abigail": 78, "Brian": 86, "Carl": 95, "Debbie": 100, "Erin": 88}
example_dict_2 = {"Andy": 73, "Benny": 64, "Celeste": 90, "Danilo": 84, "Eric": 78}

# One important concept related to functions is that they can be reused. Therefore, we can execute
# the same function to perform operations on BOTH of the above dictionaries.
def dictionary_reader(dictionary):
  """This function will format and print a dictionary."""
  print("Let's output a dictionary \n")

  for student in dictionary:
    print(f"{student} got a score of {dictionary[student]} on their exam!")
  
  print("\n This function has finished running.")

dictionary_reader(example_dict_1) # Here we pass the function an argument for our first dictionary

print("\n")

dictionary_reader(example_dict_2) # Here we see the same function performing operations with our
                                  # second dictionary.

# TODO: Section 4 of TODO 11 (4 min for students, 2 min for demo)
###################################################################################################

# TITLE: Section 5 - Working with Scope (7 minutes)
# Below are examples of using variables & the timing of a function call to portray scope.
# Here we call "s" after the function is called, which will return a NameError.
def func():
  print(s)
func()
s = "I love Paris in the summer!"

# Here, since the variable is declared before the function is called, it will print the "s2" value
def func2():
  print(s2)
s2 = "I love San Diego in the summer!"
func2()

# Here, the variable "s3" is referenced within the function's scope. Since "s3" is not passed as an
# argument to the function call of "func3()", the global variable "s3" defined outside the scope
# of the function has no impact on the output. Therefore "func3()" will print the statement,
# "I love London."
def func3():
  s3 = "I love London!"
  print(s3)

s3 = "I love Malaysia!"
func3()

# Here, the global variable "s3" is printed.
print(s3)
