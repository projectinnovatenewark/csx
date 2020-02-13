"""
Data Structures/Nested Data Types/Nested Data Structures Review
"""
# Here are some things to remember about Lists before we get started:
    # 1) A list is a set of items seperated by commas.
    # 2) You use square brackets to establish the list
    # 3) The "Index" of an item in a list is its position in the list.
    # 3a) The first item always has an index of 0 and is increased by one with each item.

names = [
    "John",
    "Marshall",
    "Amy",
    "Chris",
    "Nicole",
    "Brittany",
    "Lisa"
]

# Lists can also be displayed as below. We will refer to the above as spreading.
# names = ["John", "Marshall"]

print(names)

##############################################################################

# There are plenty of actions we can perform on lists
# .append adds items to the end of a list

print(names)
names.append("Alshon")
print(names)

###############################################################################

# .remove is used to remove items from a list

names.remove("Nicole")
print(names)
# Notice that this method does not return a value

###############################################################################

# YOu can replace an item in a list by calling the index and assigning a new value

names[4] = "Johnny"

# .insert adds an item to a list to a specific index

print(names)
names.insert(1, "Joyce") # This will now be the second item in the list.
print(names)

# .pop will remove the last item from a list AND return it's value

print(names)
print(names.pop()) # Here you can see that Alshon was removed from the list names
print(names)

# You can use index to pop a specific item by position

print(names)
second_name = names.pop(2) # Since .pop returns a value, you can also set it to a variable.
print(second_name)
print(names)

###############################################################################

# .extend can add a list to the end of another list

superlatives = ["Best Dressed", "Class Clown", "Most Likely to be famous"]
print(superlatives)
extra_superlatives = ["Most likely to brighten your day", "Coolest car"]
print(extra_superlatives)
superlatives.extend(extra_superlatives)
print(superlatives) # You can see extra_superlatives was added to the superlatives list
print(extra_superlatives) # You can see that extra_superlatives still retains its list.

###############################################################################


# The first item in a list has an index of 0

fruits = ["apple", "pear", "orange", "banana", "pineapple", "watermelon"]
print(fruits)
print(fruits[2])
second_item = fruits[1]
print(second_item)

# slicing is a quick way to split up lists into segments by using index positions

first_half = fruits[:3]
second_half = fruits[3:]
print(first_half)
# You can see here that the list first_half grabs the first 3 items (Index 0 through 2)

print(second_half)
# You can see here that the list second_half grabs the last 3 items (Index 3 through 5)

# This will include each item except the first and last
# This can be printed directly instead of using a variable as well

print(fruits[1:5])

# An index of -1 will always be the last item in a list

print(fruits[-1]) 
print(fruits[:-1]) # This index returns all items EXCEPT the last

# This last one is a stepper. It will return values from 0 through 5, but skipping
# every other value (hence the 2)
print(fruits[0:5:2])

# ################################################################################

# DICTIONARIES

# Dictionaries are different than lists in that dictionaries are made up of Keys and Values
# Each key is assigned a value that can be used to return said value
# Dictionaries use {}

materials = {
    "shirt": "cotton",
    "pants": "polyester",
    "sheets": "linen"
}

print(materials)

# This is how you use the key to return its value
# print(materials["pants"])

###############################################################################

# to append a dictionary, use the following format - dictionary["new_key"] = "new_value"

new_key = "towel"
new_material = "microfiber"
materials[new_key] = new_material
# This would be the same as materials["towel"] = "microfiber"
# But when you are using a variable equal to a string, you do not need to wrap it in quotes
# since its value is already a string.
print(materials)

##############################################################################

# use .update to update a key's value

materials.update({"shirt": "bamboo cotton"})
print(materials)
# Notice the syntax used - it is similar to the way dictionaries are created from scratch

###############################################################################

# You can use .pop here too! You have to reference a key to be able to do so though.
# materials.pop() will return an error message

materials.pop("shirt")
print(materials)

###############################################################################


# the get method will find a value for a key in a dictionary
# you can also specify a return value if the key does not exist in the dictionary
example_dict = {"One": 10, "Two": 20, "Three": 30}
second_value = example_dict.get("Two")
print(second_value)

###############################################################################

# a second argument with the get function is what is returned if the first argument isnt in the dict
# this will return 321 since there is no key "Four"

fourth_value = example_dict.get("Four", 1000)
print(fourth_value)

###############################################################################

# Nested Data Structures
# These data structures can be used together to create complex data sets!
# Below is an example of a dictionary holding multiple dictionaries and lists!

# This is what a spread data set would look like with correct tabulation.
# If something is nested, it should be tabbed once from the original position
bobs_burgers = {
    "season 1": {
        "episode 1": {
            "cast": [
                "H. Jon Benjamin",
                "Kristen Schall",
                "Dan Mintz"
            ],
            "title": "Food Truckin",
            "run time": 30
        },
        "episode 2": {
            "cast": [
                "H. Jon Benjamin",
                "Kristen Schall",
                "Dan Mintz"
            ],
            "title": "Out of Burgers",
            "run time": 30
        }
    },
    "season 2": {
        "episode 1": {
            "cast":[
                "H. Jon Benjamin",
                "Kristen Schall",
                "Dan Mintz"
            ],
            "title": "Sheesh! Cab, Bob?",
            "run time": 30
        },
        "episode 2": {
            "cast": [
                "H. Jon Benjamin",
                "Kristen Schall",
                "Dan Mintz"
            ],
            "title": "Buns City",
            "run time": 30
        }
    }
}
# Matrices

# Python doesn't have a formal way of creating a matrix, but we can think of one as a list of lists.
# What do we mean by this?
# Take the following for example
# [[1, 4, 5, 12], 
# [-5, 8, 9, 0],
# [-6, 7, 11, 19]]

# You can see by the bracket notation that the list starts, then the first 'value'
#  in the list is another list and so on!
# This can be used and treated like any other list

list1 = [
    [1, 4, 5, 12], 
    [-5, 8, 9, 0],
    [-6, 7, 11, 19]
]
print(list1)
print("The last item in the list is:", list1[-1])

# You can even call on an item inside the main list

print("The second item in the second list is:", list1[1][1])

print(list1[0]*4)

# This is an important concept going forward and will be called on later in the semester.