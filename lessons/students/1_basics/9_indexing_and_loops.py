"""
Indexing and range function for lists, dictionaries, strings and numbers
"""

# for loops iterate through something that is passed to it. What it does with that item is specified
# in the loop. Each time the control is passed through the loop is called an "iteration".

# for ranges, the variable you set will be equal to the number in the range,
# starting with the lower bound of that range.

# for lists, the variable will iterate through each item in the list, starting with the first item.

# for dictionaries, the variable will represent each iterate through each key,
# starting with the first key.

####################################################################################################

# TITLE: Section 1- FOR loops
# "for x in range(y)" is a loop that would iterate through every number from zero up until the
# given number of "y". When there is only one number passed to the range() function, the "lower bound" 
# of that range would default to zero. The "upper bound", which in the case below is 9, would NOT be
# included. In the loop, each iteration will assign itself the variable `num`. For the first iteration
# of this for loop, zero would be assigned to num. In the second iteration, num would be
# assigned one (and so on).
print("range 9 loop: ")
for num in range(9):
    print(num)

####################################################################################################

# TITLE: Section 1.1- Loops with range 
# If you put in an initial argument, that number is included in the range and would be the
# "lower bound". The second number would be the "upper bound", and therefore not included
# in the loop.
print("range 3, 11 loop: ")
for num in range(3, 11):
    print(num)

# TODO: Section 1 of TODO 9

####################################################################################################

# TITLE: Section 2- String Indexing
# If you want to access a part of a string, you can get a portion of the string with indexing.
beatles = "You say goodbye, and I say hello!"

parsed_beatles = beatles[3:11]

for char in parsed_beatles:
    print(char)

print("letters from the beatle song: " + beatles[3:11])

####################################################################################################

# TITLE: Section 2.1- Lists and Loops

# Index lists with for loops.
grades = [72, 87, 99, 45, 70]

# When indexing lists, remember that the first position starts with zero and
# you can reference the last item with a negative one.
# Recall: if you want to concatenate a number into a string, convert it to a string by wrapping
# it with the str() function.

# IMPORTANT:
# if you want to use f shorthand accross multiple lines, you need to use concatenation.
print(f"The first element in the list is {grades[0]}",
      f"and the last element in the array is {grades[-1]}")

# Lets show how a for loop works with lists. This loop will "iterate" over each number. Each
# item in the list will iterated over in this loop.
for num in grades:
    print(num) # this will happen once for every "iteration"

print("End of first for loop. \n")

# Now, lets make it readable! Add one to the index number so it starts at one instead of zero
# to find the index of an element in a list, use the index function as shown below. The index
# function will return an item's index value within the list, in the
# format of `idx = list_name.index(item_name)`
for num in grades:
    print("Student number " + str(grades.index(num) + 1) + "'s grade is " + str(num))

print("End of second for loop. \n")

####################################################################################################

# TITLE: Section 2.2- Using a dictionary in a loop

# Let's make reading grades easier by storing each grade as a value to the 
# student's name as its key in the dictionary. When you use a for loop,
# it will return each key in the dictionary. You can access each value by using
# bracket notation: "dictionary[key]".

grades = {"Chris": 65, "Deshaun": 77, "Mariah": 88, "Paula": 94}

# Here is how you access values in a dictionary and store it into a variable witht the format:
# value = dict[key]
chris = grades["Chris"]
print(f"Chris got a {chris}")

# When you use a for loop with a dictionary, the variable gets set to every key, NOT the value :)
# It is important to understand that functions and loops use a colon and work within a 'scope', 
# or whatever falls within the tabulation set by the line thereafter. 
# We use four spaces in one tab to denote that certain code falls within a function
for student in grades:
    print(f"{student} got a {grades[student]} on their comp sci exam")

# HINT:
# We can use bracket notation inside the for loop to make it easier to reference the given values.
print("\n2nd for loop:\n")
for student in grades:
    grade = grades[student]
    print(f"{student} got a {grade} on their comp sci exam")

# TODO: Section 2 of TODO 9

####################################################################################################

# TITLE: Section 3- While loops

# The way that a while loop decides to continue running is if it evaluates a condition as true.
# The following while loop will continue to run until all the items have been removed with the
# .pop() method and your list is empty. This is because while there are items in the list, the
# condition remains true. An empty list equates to a False condition, and the loop will end.
grocery_list = ['Bread', 'Butter', 'Frozen Pizza', 'Mozz Sticks', 'Ice Cream']
while grocery_list:
    purchased_item = grocery_list.pop()
    print(f'You purchased {purchased_item} and removed it from your list.')
    print('Your remaining items are', grocery_list)

# If you want to execute an action a certain number of times, you can use an iterator with a while
# loop to decrement until that number is 0. A zero value will equate to a False condition, thus
# ending the while loop.
i = 10
while i:
    print(f"i ={i}")
    i -= 1

# TODO: Section 3 of TODO 9

####################################################################################################

# TITLE: Section 4- Continue Statements and Intro to Conditionals

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

# TITLE: Section 4.1- Break Statements

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

# TODO: Section 4 of TODO 9
