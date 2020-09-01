"""
Indexing and range function for lists, dictionaries, strings and numbers
"""

# "for loops" iterate through something that is passed to it. What it does with that item is
# specified in the loop. Each time the control is passed through the loop is called an "iteration".
# You will see for loops in the foolowing format: "for variable in object:" where "variable" is an
# arbitrary name and "object" is the object you are iterating through.

# When using a for loop within a range (i.e. "for x in range(10):"), x would equal each integer
# from 0 to 9.

# If we are using a for loop with a list, the variable will iterate through each item in the list
# starting with the first item and looping until the last item.

# When iterating through dictionaries, the variable would represent each key of a key/value pair
# in the dictionary. Similar to lists, it will loop through starting at the first key until reaching
# the last one.

####################################################################################################

# TITLE: Section 1: FOR loops
# "for x in range(y)" is a loop that would iterate through every number from zero up until the
# given number of "y". When there is only one number passed to the range() function, the "lower bound" 
# of that range would default to zero. The "upper bound", which in the case below is 9, would NOT be
# included. In the loop, each iteration will assign itself the variable `num`. For the first iteration
# of this for loop, zero (0) would be assigned to num. In the second iteration, num would be
# assigned one (1) and so on.
print("range 9 loop: ")
for num in range(9):
    print(num) # This print statement will run once for every iteration of "num".

# Let's put in an initial argument now to change our lower bound from zero (0) to three (3). Now
# when we print each "num", we should see "3, 4, 5, ..., 10".
print("range 3, 11 loop: ")
for num in range(3, 11):
    print(num)

# TODO: Section 1 of the TODO

####################################################################################################

# TITLE: Section 2: String Slicing and Loops

# It is actually possible to loop through each character of a string. The for loop will keep the
# same format as the above.
beatles = "You say goodbye, and I say hello!"
for char in beatles:
    print(char)

# It is also possible to slice strings by their characters as we have ddone with lists in previous
# lessons. This is done by setting each character to an index position, similar to a list. Below in
# "beatles[3:11]", the 3 and 11 represent the third and eleventh index in the string. This can
# also be looped through when set to a variable!
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
# if you want to use f shorthand accross multiple lines, you need to use concatenation. You'll
# notice that although our print statement is across lines 76-77, its output will be on one line.
print(f"The first element in the list is {grades[0]}",
      f"and the last element in the array is {grades[-1]}")

# Lets see how a for loop works with lists. This loop will "iterate" over each number. Each
# item in the list will be iterated over in this loop.
for grade in grades:
    print(grade)

print("End of first for loop. \n")

# Now, lets make it readable! Add one to the index number so it starts at one instead of zero
# to find the index of an element in a list, use the index function as shown below. The index
# function will return an item's index value within the list, in the
# format of `idx = list_name.index(item_name)`
for num in grades:
    print(f"Student number {grades.index(num) + 1}'s grade is a(n) {num}.'")

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
