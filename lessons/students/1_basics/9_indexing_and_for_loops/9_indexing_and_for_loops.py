"""
Indexing and range function for lists, dictionaries, strings and numbers.
"""

# In Python, "for loops" are used to iterate through objects. The syntax of a "for loop" is:
# "for iteration in iterable:". In plain english this reads as, "for each element in
# an object, do something." The "iteration" is a variable that assumes the value of each instance in
# the iterable object, also known as each "iteration". The "iterable_object" can be any object in
# Python that you can loop through and has a collection of items. This includes lists, dictionaries,
# strings, and more.

# It is important to understand that "for loops" use a colon to define it's body. Another thing to
# note is that for loops are "controlled" loops, meaning that they will only loop over an iterable
# object until there is no iterations remaining. In the next lesson we will review another type of
# loop that is different in how it iterates, called a "while" loop.

####################################################################################################

# TITLE: Section 1 - Lists and For Loops

# When using a "for loop" with a list, the variable will iterate through each item in the list
# starting with the first item and continue looping until the last item. 

grades = [72, 87, 99, 45, 70]

# Let's see how a "for loop" works with lists. The following loop will "iterate" over each number.
# Each "grade" in the list "grades" will be printed in this loop starting at index 0 until reaching
# the end of the list.
for grade in grades:
  print(grade)

print("End of first for loop. \n")

# To find the index of an element in a list, you can use the index function as shown below. The
# ".index()" method takes one argument, the item you would like the index position of, and returns
# the first instances index position for that item.
print(f"Student #{grades.index(72)} recieved a grade of {grades[0]}\n") # Remember when indexing lists
                                                                        # the first position starts
                                                                        # with zero.

# The print statement above refers to "Student #0", which wouldn't make much sense as an output to
# an end user. However, we can use a "for loop" to make print statements more readable when using
# the index function. To do so, you can add one to the index number of a given item to represent its
# position in the list in plain english.

print("Starting Loop 2")
for grade in grades:
    print(f"Student #{grades.index(grade) + 1} recieved a grade of {grade}.")

print("End of second for loop.\n")

# TODO: Section 1 of TODO 9 (5 minutes for students, 3 minutes for demo)

###################################################################################################

# TITLE: Section 2 - String Slicing and For Loops

# Like lists, strings can also be indexed. The first character in a string is at index position 0.
# Given the string below, we can grab the first character just as we do in lists with bracket
# notation.

beatles = "You say goodbye, and I say hello!"
print(f"Character at index position 0: {beatles[0]}")

# We can use indexing to "slice" strings as well. The syntax to slice a string would look like:
# "string[lower:upper]", where "lower" is the lower bound (inclusive) and "upper" is the upper bound
# (not inclusive). Below in "beatles[3:11]", the 3 and 11 represent the third and eleventh index in
# the string. This can also be looped through when set to a variable.
parsed_beatles = beatles[3:11]
print(f"Parsed beatles: {parsed_beatles}")

# It is also possible to loop through each character of a string. In the code below, each character
# in the string "beatles" will be printed one at a time starting at index 0 until reaching the end
# of the list.
for char in beatles:
    print(char)

# TODO: Section 2 of the TODO (4 minutes for students, 2 minutes for demo)

####################################################################################################

# TITLE: Section 3 - For Loops
# The range function returns a list of numbers and can be iterated through as well. For example,
# "for num in range(9):" would result in x representing each integer from 0 to 8. When there is only
# one number passed to the range() function, the "lower bound" will default to zero. The
# "upper bound", which in the case below is 9, would NOT be included. In the loop below, each
# iteration will assign itself the variable "num". For the first iteration of this "for loop", 0
# would be assigned to num. In the second iteration, num would be assigned 1 and so on.
print("range 9 loop: ")
for num in range(9):
    num += 1
    print(num)

# If we want to add a lower bound we can use the following syntax: "range(lower, upper)" where
# "lower" is inclusive and "upper" is non-inclusive. Let's put in an initial argument to change
# our lower bound from 0 to 3 and the upper bound to 11. Now the range will include numbers 3 to 10.
print("\nrange(3, 11) loop: ")
for num in range(3, 11):
    print(num)

# A common pattern you may encounter is that of an iterator outside of the loop that is modified
# inside the loop. This can be done for a number of reasons, which you will see later in our
# curriculum.
i = 0 # i will be incremented by one for every iteration in our loop
for n in range (100):
  j = 0 # j will be set to zero at the beginning of every loop, therefore it will always print 1.
  i += 1
  j += 1
  print(f"i: {i}, j: {j}")

# TODO: Section 3 of the TODO (4 minutes for students, 2 minutes for demo)

####################################################################################################

# TITLE: Section 4 - Dictionaries and For Loops

# When iterating through dictionaries, the variable will represent each key of a key/value pair in
# the dictionary. The "for loop" will iterate through the dictionary's keys starting at the first
# key until reaching the last one.

# Let's make reading grades easier by storing each grade as a value with a student's name as its key
# in the dictionary. When you use a "for loop", it will return each key in the dictionary. You can
# access each value by using bracket notation (i.e. dictionary[key]).

grades = {"Chris": 65, "Deshaun": 77, "Mariah": 88, "Paula": 94}

# When you use a "for loop" with a dictionary, the variable gets set to every key, but not the value.
for student in grades:
    print(f"{student} got a {grades[student]} on their comp sci exam.")

# We can use bracket notation in the "for loop" to make it easier to reference the key's value, as
# seen below.
print("\n2nd for loop:\n")
for student in grades:
    grade = grades[student]
    print(f"{student} got a {grade} on their comp sci exam.")

# TODO: Section 4 of TODO 9 (6 minutes for students, 3 minutes for demo)
