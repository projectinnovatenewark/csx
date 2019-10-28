"""
Here we will cover lists and dicts
"""

# lists are a grouping of values
CLASS_LIST = ["Andy", "Bronny", "Carlos", "Denisa", "Enrique"]

##############################################################################################

# dictionaries are similar, except they have keys which have values
# similarly to how a dictionary has words with definitions, the keys represent
# the words and values represent the definitions
GRADES_DICT = {"Ang": 87, "Bronny": 95, "Carlos": 75, "Denisa": 55, "Enrique": 100}

##############################################################################################

# below is an example of indexing. the first item in any list has an index of ZERO
# and the next item is 1, followed by 2, etc.
print("The first student in the class class list is " + CLASS_LIST[0])

# in dictionaries, however, values can only be accessed by their key
print("Bronny's grade: " + str(GRADES_DICT["Bronny"]))

print("Denisa's score is " + str(GRADES_DICT["Denisa"]))

##############################################################################################

# tuples are lists that cannot have their values modified and they are denoted with parentheses
months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
