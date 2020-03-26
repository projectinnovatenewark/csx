"""
Indexing and range function for lists, dictionaries, strings and numbers
"""

# for loops iterate through an item that is passed to it. how it iterates depends on the item you pass it.
# for ranges, the variable you set will be equal to the number in the range, starting with the smallest number
# for lists, the variable will iterate through each item in the list, starting with the first item
# for dictionaries, the variable will represent each iterate through each key, starting with the first key

# range values for numbers is a function that includes zero but not the number in the range function
# the below for loop will only print numbers zero through 8, not including 9
# `num` is the variable we assign to every number in the range. In the first `iteration` of this for
# loop, zero would be assigned to num. In the second iteration, num would be assigned one (and so on)
for num in range(9):
    print(num)

##############################################################################################

# if you put in an initial argument, that number is included in the range. If you just put one
# number, it starts with zero.
for num in range(3, 11):
    print(num)

##############################################################################################

# if you want to access a part of a string, you can get a portion of the string with indexing
beatles = "You say goodbye, and I say hello!"
print("letters from the beatle song: " + beatles[3:11])

##############################################################################################

# index lists with for loops
grades = [72, 87, 99, 45, 70]

# when indexing lists, remember that the first position starts with zero and
# you can reference the last item with a negative one
# recall: if you want to concatenate a number into a string, convert it to a string by wrapping
# it with the str() function
print("The first element in the list is " + str(grades[0]) +
      "and the last element in the array is " + str(grades[-1]))

# lets print each grade with the number of the position of the list
# but, lets make it readable! add one to the index number so it starts at one instead of zero
# to find the index of an element in a list, use the index function as shown below.
for num in grades:
    print("Student number " + str(grades.index(num) + 1) + "'s grade is " + str(num))

##############################################################################################

# lets make reading grades easier by attaching them to the name of the student that got the grade
# when you use a for loop, it will return each key in the dictionary. You can access the value
# by indexing the dictionary using dictionary[key] to find that key's value
grades = {"Chris": 65, "Deshaun": 77, "Mariah": 88, "Paula": 94}

# Here is how you access values in a dictioary- you pass it the key!
print("Chris got a " + str(grades["Chris"]))

# When you use a for loop with a dictionary, the variable gets set to every key item, NOT the value :)
# here we are also introduced to tabulation (aka spacing with tabs). It is important to understand
# that functions and loops use a colon and work within a 'scope', or whatever falls within the 
# tabulation set by the line thereafter. We use four spaces in one tab to denote that certain code
# falls within a function
for student in grades:
    print(student + " got a " + str(grades[student]) + " score on their comp sci exam")

# lets find out how many students had scores!
# we do this by using the len() function with grades to print us the length of the grades dictionary
print("Number of students: " + str(len(grades)))
