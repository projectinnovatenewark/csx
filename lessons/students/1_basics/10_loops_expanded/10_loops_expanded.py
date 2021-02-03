"""
Expanding on our knowledge of loops
"""

# TITLE: Section 1 - While loops

# The way that a while loop decides to continue running is if it evaluates a condition as true.
# The following while loop will continue to run until all the items have been removed with the
# .pop() method and your list is empty. This is because while there are items in the list, the
# condition remains true. An empty list equates to a False condition, and the loop will end.
grocery_list = ["Bread", "Butter", "Frozen Pizza", "Mozz Sticks", "Ice Cream"]
while grocery_list:
    purchased_item = grocery_list.pop()
    print(f"You purchased {purchased_item} and removed it from your list.")
    print(f"Your remaining items are: {grocery_list}")

# If you want to execute an action a certain number of times, you can use an iterator with a while
# loop to decrement until that number is 0. A zero value will equate to a False condition, thus
# ending the while loop.
i = 10
while i:
    print(f"i ={i}")
    i -= 1

# TODO: Section 1 of TODO 9 (3 minutes for students, 1 minutes for demo)

####################################################################################################

# TITLE: Section 2 - Continue Statements and Intro to Conditionals

# The "continue" statement rejects all the remaining statements in the current iteration of the loop
# and moves the control back to the top of the loop.

# In this example, we provide a sneak peak at a conditional. The condition we are using is an "if"
# condition. That just means "if the following condition is true, then do something within the scope
# of this statement". While we also haven't really addressed scope, just know that everything
# following the if statement that is tabbed inward represents the scope of that if statement.
# Below is an example to get you comfortable with how conditionals work.
if (str(5) == '5'): # "if the integer '5' converted to a string is equal to the string '5"
    print('this is in the scope of the if statement')
    print('this would also be in the scope of the if statement')

print('this would NO LONGER be in the scope of the if statement')

# Here we will show examples of using a continue statement, as well as a conditional, within a for
# loop and a while loop.
for letter in 'Python': # This will iterate through every letter in the word Python.
   if (letter == 'h'):
      continue
   print(f"Current Letter :{letter}")

i = 10
while i > 0: # Here we are using a condtional (while i is greater than 0), to set custom
               # True/False conditions for our while loop.
    i -= 1 # This will subtract one from the "i" variable and set it equal to that new value.
    if(i == 5):
        print("This iteration, since the if statement condition was true, we will trigger the",
        "continue statement. That will skip the current iteration and not execute the print",
        "statement within the while loop. \n")
        continue
    print(f"Current variable value :{var}")

# This will execute after the while loop is done running.
print("Goodbye!") # This print statement won't run until the while loop is complete
                  # since this tabulation is set to the same spacing as the while loop.

####################################################################################################

# TITLE: Section 2.1 - Break Statements

# "break" statements are used with conditionals to stop a loop from running before its natural end.
# Normally in a for loop or while loop, the natural end is when the base condition is False whether
# it be iterating through the last item in a list or an iterator hitting 0 in a while loop. Adding a
# break statement when a sub-condition is True though will end the for loop or while loop no matter
# what iteration the program is on. Below is an example of this within a for loop.
for letter in 'Python':
    if (letter == 'h'): # Again, this will iterate through every letter in the word Python.
        break # When the variable "letter" is eequal to "h", the loop will break.
    print(F"Current Letter :{letter}")

var = 10
while var > 2: # This loop will only run if "var" is greater than 2.
    var -= 1 # This will decrement the "var" variable by one (1).
    if (var == 5):
        print("This iteration, since the if statement condition was true, will trigger the break",
              "statement. This will end the current iteration and subsequently the while loop.\n")
        break
    print(f"Current variable value: {var}")
print("Your while loop has ended. Goodbye!") # Since this tabulation is set to the same
                                             # spacing as the while loop, this will run once
                                             # the loop is complete.

# TODO: Section 2 of TODO 9 (4 min for students, 2 min for demo)
