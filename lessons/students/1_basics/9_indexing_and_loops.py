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
# TITLE: Section 1: FOR loops
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

# TITLE: Section 1.1: Loops with range 
# If you put in an initial argument, that number is included in the range and would be the
# "lower bound". The second number would be the "upper bound", and therefore not included
# in the loop.
print("range 3, 11 loop: ")
for num in range(3, 11):
    print(num)

# TODO: Section 1 of the TODO

####################################################################################################

# TITLE: Section 2: String Indexing
# If you want to access a part of a string, you can get a portion of the string with indexing.
beatles = "You say goodbye, and I say hello!"

parsed_beatles = beatles[3:11]

for char in parsed_beatles:
    print(char)

print("letters from the beatle song: " + beatles[3:11])

####################################################################################################

# TITLE: Section 2.1: Lists and Loops

# Index lists with for loops.
grades = [72, 87, 99, 45, 70]

# When indexing lists, remember that the first position starts with zero and
# you can reference the last item with a negative one.
# Recall: if you want to concatenate a number into a string, convert it to a string by wrapping
# it with the str() function.

# IMPORTANT:
# if you want to use the f shorthand accross multiple lines, you need to use concatenation.
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

# Lets find out how many scores were in our list.
# We do this by using the len() function with the "grades" list
# to print us the length, or the number of items in the list.
print("Number of students: " + str(len(grades)))

# TODO: Section 2 of the TODO

####################################################################################################

# TITLE: Section 3: Using a dictionary in a loop

# Let's make reading grades easier by storing each grade as a value to the 
# student's name as its key in the dictionary. When you use a for loop,
# it will return each key in the dictionary. You can access each value by using
# bracket notation: "dictionary[key]".

grades = {"Chris": 65, "Deshaun": 77, "Mariah": 88, "Paula": 94}

# Here is how you access values in a dictionary- you pass it the key!
# The format for this is value = dict[key]
print(f"Chris got a {grades["Chris"]}")

# When you use a for loop with a dictionary, the variable gets set to every key, NOT the value :)
# It is important to understand that functions and loops use a colon and work within a 'scope', 
# or whatever falls within the tabulation set by the line thereafter. 
# We use four spaces in one tab to denote that certain code falls within a function
for student in grades:
    print(f"{student} got a {grades[student]} on their comp sci exam")

# Lets find out how many students had scores!
# We do this by using the len() function with the "grades" dictionary
# to print us the length, or the number of key/value pairs in the dictionary
print("Number of students: " + str(len(grades)))

####################################################################################################
# TITLE: Section 3.1: While loops


# The way that a for loop/while loop decides to continue running is if it evaluates a condition
# as true. We will go over what is considered "True" for different types of iterable
# data (i.e. lists, dicts, range) using loops.

# This will continue to run until all the items have been removed with the .pop method
# and your list is empty. An empty list equates to a False condition, and the loop will end.
grocery_list = ['Bread', 'Butter', 'Frozen Pizza', 'Mozz Sticks', 'Ice Cream']
while grocery_list:
    purchased_item = grocery_list.pop()
    print(f'You purchased {purchased_item} and removed it from your list.')
    print('Your remaining items are', grocery_list)

# TODO: Section 3 of the TODO

####################################################################################################
# TITLE: Section 4: While Loop incraments 

# If you have a number that you are decrementing, the while loop will run until that number
# is zero. A zero value equates to a False condition, and the loop will then end.
i = 10
while i:
    print(i)
    i -= 1

# TODO: Section 4 of the TODO

####################################################################################################
# TITLE: Section 5: Tying it all together 

# "continue" statement:
# The continue statement rejects all the remaining statements in the current iteration of the loop
# and moves the control back to the top of the loop.

# In this example, we provide a sneak peak at a conditional. The condition we are using is an "if"
# condition. That just means "if the following condition is true, then do something within the scope
# of this statement". While we also haven't really addressed scope, 
# just know that everything following the if statement that is tabbed inward represents 
# the scope of that if statement.
# Example:
if (str(5) == '5'):
    print('this is in the scope of the if statement')
    print('this would also be in the scope of the if statement')

print('this would NO LONGER be in the scope of the if statement')

# The continue statement can be used in both while and for loops.
for letter in 'Python': # this will iterate through every letter in the word Python.
   if (letter == 'h'):
      continue
   print(f"Current Letter :{letter}")

var = 10
while var > 0:
    var -= 1 # this will subtract one from the "var" variable and set it equal to that new value
    if(var == 5):
        print("This iteration, since the if statement condition was true, we will trigger the",
        " continue statement. That will skip the current iteration and not execute the print ",
        "statement within the while loop. \n")
        continue
    print(f"Current variable value :{var}")

# this would execute after the while loop is done running.
print("Good bye!") # since this tabulation is set to the same spacing as the while loop,
                   # this print statement won't run until the while loop is complete.

# "break" statement:

for letter in 'Python':
    if letter == 'h': # this will, again, iterate through every letter in the word Python.
        break
    print(F"Current Letter :{letter}")

var = 10
# You can see that custom conditions can be placed in a while loop, too. 
# We can check for the following conditions:
# "x == y" (x is equal to y); "x != y" (x is NOT equal to y); 
# "x > y" (x is greater than y); "x >= y" (x is greater than or equal to y);
# "x < y"(x is less than y); "x <= y" (x is less than or equal to y); 
# "x in y" (x exists in y- often y represents a list here);
# "x not in y" (x does not exist in y); 
# and we can combine conditions such as "x < y and x != z" (x is less than y AND x does not equal z)

while var > 2: # this loop will only run if "var" is greater than 2.
    var -= 1 # this will subtract one from the "var" variable and set it equal to that new value
    if (var == 5):
        print("This iteration, since the if statement condition was true, will trigger the break statement. That end the current iteration and then end the for loop. \n")
        break
    print(f"Current variable value : {var}")
print("Your while loop has ended. Good bye!") # since this tabulation is set to the same spacing as the while loop, this will run once the loop is complete

# TODO: Section 5 of the TODO
