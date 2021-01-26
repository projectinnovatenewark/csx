# """
# Indexing and range function for lists, dictionaries, strings and numbers.
# """

# # "for loops" iterate through something that is passed to it. What it does with that item is
# # specified in the loop. Each time the control is passed through the loop is called an "iteration".
# # You will see for loops in the following format: "for alias in iterable:" where "alias" is a
# # variable that assumes each iteration's value and "iterable" is an object in Python that can be
# # iterated through (i.e. list, dictionary, and strings).

# # Since range returns a list of numbers, it can also be iterated through. When using a for loop
# # within a range (i.e. "for x in range(10):"), x would equal each integer from 0 to 9.

# # If we are using a for loop with a list, the variable will iterate through each item in the list
# # starting with the first item and looping until the last item. When iterating through dictionaries,
# # the variable would represent each key of a key/value pair in the dictionary. Similar to lists, it
# # will loop through starting at the first key until reaching the last one.

# ####################################################################################################

# # TITLE: Section 1 - FOR loops
# # "for x in range(y)" is a loop that would iterate through every number from zero up until the
# # given number of "y". When there is only one number passed to the range() function, the "lower bound" 
# # of that range would default to zero. The "upper bound", which in the case below is 9, would NOT be
# # included. In the loop, each iteration will assign itself the variable "num". For the first iteration
# # of this for loop, zero (0) would be assigned to num. In the second iteration, num would be
# # assigned one (1) and so on.
# print("range 9 loop: ")
# for num in range(9):
#     print(num) # This print statement will run once for every iteration of "num".

# # Let's put in an initial argument now to change our lower bound from zero (0) to three (3). Now
# # when we print each "num", we should see "3, 4, 5, ..., 10".
# print("\nrange 3, 11 loop: ")
# for num in range(3, 11):
#     print(num)

# # TODO: Section 1 of the TODO (4 minutes for students, 2 minutes for demo)

# ####################################################################################################

# # TITLE: Section 2 - String Slicing and Loops

# # It is actually possible to loop through each character of a string. The for loop will keep the
# # same format as the above.
# beatles = "You say goodbye, and I say hello!"
# for char in beatles:
#     print(char)

# # It is also possible to slice strings by their characters as we have done with lists in previous
# # lessons. This is done by setting each character to an index position, similar to a list. Below in
# # "beatles[3:11]", the 3 and 11 represent the third and eleventh index in the string. This can
# # also be looped through when set to a variable!
# parsed_beatles = beatles[3:11]
# for char in parsed_beatles:
#     print(char)

# print("letters from the beatle song: " + beatles[3:11])

# ####################################################################################################

# # TITLE: Section 2.1 - Lists and Loops

# # Index lists with for loops.
# grades = [72, 87, 99, 45, 70]

# # When indexing lists, remember that the first position starts with zero and
# # you can reference the last item with a negative one.
# # Recall: if you want to concatenate a number into a string, convert it to a string by wrapping
# # it with the str() function.

# # IMPORTANT:
# # if you want to use f shorthand accross multiple lines, you need to use concatenation. You'll
# # notice that although our print statement is across lines 76-77, its output will be on one line.
# print(f"The first element in the list is {grades[0]}",
#       f"and the last element in the array is {grades[-1]}")

# # Let's see how a for loop works with lists. This loop will "iterate" over each number. Each
# # item in the list will be iterated over in this loop.
# for grade in grades:
#     print(grade)

# print("End of first for loop. \n")

# # Now, lets make it readable! Add one to the index number so it starts at one instead of zero
# # to find the index of an element in a list, use the index function as shown below. The index
# # function will return an item's index value within the list, in the format of:
# # "idx = list_name.index(item_name)"
# for num in grades:
#     print(f"Student number {grades.index(num) + 1}'s grade is a(n) {num}.")

# print("End of second for loop.\n")

# TODO: Section 2 of TODO 9 (6 minutes for students, 3 minutes for demo)
####################################################################################################

# TITLE: Section 3 - Looping through a dictionary

# Let's make reading grades easier by storing each grade as a value to the 
# student's name as its key in the dictionary. When you use a for loop,
# it will return each key in the dictionary. You can access each value by using
# bracket notation: "dictionary[key]".

grades = {"Chris": 65, "Deshaun": 77, "Mariah": 88, "Paula": 94}

# Here is how you access values in a dictionary and store it into a variable with the format:
# value = dict[key]
chris = grades["Chris"]
print(f"Chris got a {chris}")

# When you use a for loop with a dictionary, the variable gets set to every key, NOT the value :)
# It is important to understand that functions and loops use a colon and work within a 'scope', 
# or whatever falls within the tabulation set by the line thereafter. 
# We use four spaces in one tab to denote that certain code falls within a function
for student in grades:
    print(f"{student} got a {grades[student]} on their comp sci exam.")

# HINT: We can use bracket notation in the for loop to make it easier to reference the key's value
print("\n2nd for loop:\n")
for student in grades:
    grade = grades[student]
    print(f"{student} got a {grade} on their comp sci exam.")

# TODO: Section 3 of TODO 9 (6 minutes for students, 3 minutes for demo)
