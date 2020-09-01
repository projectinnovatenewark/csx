"""
Indexing and range function for lists, dictionaries, strings and numbers.
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

# TITLE: Section 1 - FOR loops
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

# TITLE: Section 2 - String Slicing and Loops

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

# TITLE: Section 2.1 - Lists and Loops

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

####################################################################################################

# TITLE: Section 2.2 - Using a dictionary in a loop

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

# TODO: Section 2 of TODO 9 (6 min for students, 3 min for demo)

####################################################################################################

# TITLE: Section 3 - While loops

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

# TODO: Section 3 of TODO 9 (3 min for students, 1 min for demo)

####################################################################################################

# TITLE: Section 4 - Continue Statements and Intro to Conditionals

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

# TITLE: Section 4.1 - Break Statements

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

# TODO: Section 4 of TODO 9 (3 min for students, 2 min for demo)
