"""
Here we will cover lists and dicts
"""

# lists are a grouping of values
CLASS_LIST = ["Andy", "Bronny", "Carlos", "Denisa", "Enrique"]

##############################################################################################

# dictionaries are similar, except they have keys which in turn have values
# similarly to how a dictionary has words with definitions, the keys represent
# the words and values represent the definitions.
GRADES_DICT = {"Andy": 87, "Bronny": 95, "Carlos": 75, "Denisa": 55, "Enrique": 100}

##############################################################################################

# below is an example of indexing. the first item in any list has an index of ZERO
# and the next item is 1, followed by 2, etc.
print("The first student in the class class list is " + CLASS_LIST[0])

# in dictionaries, however, values can only be accessed by their key. The format to finding
# a key's value is `dictionary[key]`

print("Bronny's grade: " + str(GRADES_DICT["Bronny"]))

print("Denisa's grade: " + str(GRADES_DICT["Denisa"]))

# hm. so, the first student in class can be found using CLASS_LIST[0] . We can set that equal
# to a variable like this.

first_student = CLASS_LIST[0]

# now, since this student has a grade in the grades list, let's use this variable to find the
# value of their grade in the list!

first_student_grade = GRADES_DICT[first_student]

# lets print this out together in a readable way. Tip- when you combine strings with commas,
# a space is placed between the strings. However, when you use a `+` , there are no spaces added
print(first_student + "'s grade was", first_student_grade)

##############################################################################################

# tuples are lists that cannot have their values modified and they are denoted with parentheses
months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
