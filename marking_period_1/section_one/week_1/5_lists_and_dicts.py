"""
Here we will cover lists and dicts
"""

# lists are a grouping of values
class_list = ["Andy", "Bronny", "Carlos", "Denisa", "Enrique"]

# dictionaries are similar, except they have keys which have values
# similarly to how a dictionary has words with definitions, the keys represent
# the words and values represent the definitions
grades_dict = {"Ang": 87, "Bronny": 95, "Carlos": 75, "Denisa": 55, "Enrique": 100}

# below is an example of indexing. the first item in any list has an index of ZERO
# and the next item is 1, followed by 2, etc.
print("The first student in the class class list is " + class_list[0])

# in dictionaries, however, values can only be accessed by their key
print("Bronny's grade: " + str(grades_dict["Bronny"]))