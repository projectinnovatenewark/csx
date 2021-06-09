"""
Advanced conditional statements with continue and break statements.
"""

# TITLE: Section 1 - Review

# As a reminder, conditional statements are used to perform different actions depending on whether
# a specific boolean constraint evaluates to true or false. A common conditional statement is an
# "if statement". The syntax for an "if statement" is: "if some_condition is True:" Below is an
# example of an "if statement":

booly = True
if booly:
  print("This runs if booly is true.")

# Another conditional statement we have learned previously is an "else statement". An "else
# statement" will run only if a given condition in an "if statement" does not return true. 

num = 10
if num > 11:
  print(f"The number {num} is greater than 11.")
else:
  print(f"The number {num} is less than 11.")

# IMPORTANT:
# An "else statement" must follow an "if statement". There cannot be a standalone "else statement"

# TODO: Hey Teacher: Demonstrate how this doesn't work, then comment it out and move on.
else:
  print("This doesn't work")

# TODO: Section 1 of TODO 12 (5 min for students, 2 min for demo)

####################################################################################################

# TITLE: Section 2 - The elif statement

# An "elif statement" can be read in plain english as "else if", meaning if the previous conditions
# were not true, then try this condition. The syntax for an "elif statement" is:
# "elif some_condition is True:". Below is an example of the syntax for an "elif statement":

num = 57
if num <= 50:
  print("The number is less than or equal to 50.")
elif num > 55: #This conditional statement will only run if the above if statement is false.
  print("the number is greater than 55.")

# The difference between an "else statement" and an "elif statement" is that an "else statement"
# does not test its own condition, whereas an "elif statement" does.

# Below is an example using each condtional statement we have learned so far.
num = 3 # TODO: Teacher, try changing this number up to satisfy the different conditions.

if num > 0:
  print(num, "is a positive number.")
elif num < 0: # The "elif statement" will only be triggered if the "if statement" is true.
  print(num, "is a negative number.")
else: # the "else statement" will only run if none of the conditions above are true.
  print(num, "is a zero value.")

# Below is a similar example to above, except multiple "if" statements are used.
num = 2 # TODO: Teacher, try changing this number up again to satisfy the different conditions.

if num > 0:
  print(num, "is a positive number.")
if num > 2: # Any number of "if statements" can be evaluated when executing the file.
  print(num, "is greater than 2.")
elif num < 0: # When "num" is equal to 2, the most recent "if statement" will return false. Each
                # "if statement" is the beginning of a new conditional chain, so even though the
                # first "if statement" is evaluated to be true, the "elif statement" will still
                # be evaluated.
  print(num, "is a negative number.")
else: # Since both the most recent "if statement" and above "elif statement" are false, the "else
      # statement" is executed.
  print(num, "is a zero value.")

# TODO: Section 2 of TODO 12 (7 min for students, 4 min for demo)

####################################################################################################

# TITLE: Section 3 - Continue Statements
# The "continue" statement rejects all the remaining statements in the current iteration of a loop
# and moves the control back to the top of the loop.

# Below are examples of how to use a continue statement within a "for loop" and a "while loop".
for letter in 'Python':
  if letter == 'h':
    continue # When the "for loop" observes the character 'h', the program will skip the print
             # statement and begin the next iteration.
  print(f"Current Letter: {letter}")

i = 10
while i > 0:
  i -= 1 # TIP: Remember the "-=" is used as a decrementor and will subtract 1 from "i" during
         # TIP: each iteration.
  if i == 5:
    print("\nThe continue statement will be triggered.\n")
    continue
  print(f"Current variable value: {i}")

# TODO: Section 3 of TODO 12 (4 min for students, 2 min for demo)

####################################################################################################

# TITLE: Section 4 - Break Statements

# In Python, you can use a "break statement" to forcefully end a "for loop" or "while loop". A 
# "break statement" is often used within the scope of a conditional statement so that when a
# condition is met, the loop will stop.

for letter in 'Python':
  if letter == 'o':
    break # When the variable "letter" is equal to "o", the loop will break.
  print(f"Current Letter: {letter}")

var = 10
while var > 2:
  var -= 1
  if var == 5:
    print("The break statement will be triggered.\n")
    break # When the variable "var" is equal to 5, the loop will break.
  print(f"Current variable value: {var}")

# TODO: Section 4 of TODO 12 (4 min for students, 2 min for demo)