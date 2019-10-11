"""
Indexing and range function for lists, dictionaries, strings and numbers
"""

# range for numbers is a function that includes zero but not the number in the range function
for num in range(9):
    print(num)

# if you put in an initial argument, that number is included in the range. If you just put one
# number, it starts with zero.
for num in range(3,11):
    print(num)

# if you want to access a part of a string, you can get a portion of the string with indexing
beatles = "You say goodbye, and I say hello!"
print(beatles[3:11])

# index lists wth for loops
grades = [72, 87, 99, 45, 70]

# when indexing lists, remember that the first position starts with zero
# recall: if you want to concatenate a number into a string, convert it to a string by wrapping
# it with the str() function
print("The first element in the list is " + str(grades[0]))

# lets print each grade with the number of the position of the list
# but, lets make it readable! add one to the index number so it starts at one instead of zero
# to find the index of an element in a list, use the index function as shown below
for num in grades:
    print("Student number " + str(grades.index(num) + 1) + "'s grade is " + str(num))

# lets make the reading of grades easier by attaching them to the name of the student that got the grade
# when you use a for loop, it will return each key in the dictionary. You can access the value by indexing
# the dictionary using dictionary[key] to find that key's value
grades = {"Chris": 65, "Deshaun": 77, "Mariah": 88, "Paula": 94}

for student in grades:
    print(student + " got a " + str(grades[student]) + " score on their comp sci exam")

# lets find out how many students had scores!
print("Number of students: " + str(len(grades)))
