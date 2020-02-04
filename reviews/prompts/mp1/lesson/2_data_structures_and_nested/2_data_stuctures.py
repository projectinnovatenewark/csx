"""
Data Structures/Nested Data Types/NEsted Data Structures Review
"""
# Here are some things to remember about Lists before we get started:
    # First - A list is multiple strings grouped together seperated by commas
    # Second - You use square brackets to establish the list
    # Third - The "Index" of an item in a list is its position in the list.
          # - The first item always has an index of 0 and is increased by one with each item.

names = [
    "John",
    "Marshall",
    "Amy",
    "Chris",
    "Nicole",
    "Brittany",
    "Lisa"
]

print(names)

###############################################################################

# There are plenty of actions we can perform on lists
# .append adds items to the end of a list

print(names)
names.append("Alshon")
print(names)

###############################################################################

# .remove is used to remove items from a list

names.remove("Chris")
print(names)
# Notice that this method does not return a value

###############################################################################

# .insert adds an item to a list to a specific index
print(names)
names.insert(1,"Joyce")
print(names)

# .pop will remove the last item from a list AND return it's value

print(names)
print(names.pop()) # Here you can see that Alshon was removed from the list names
print(names)

# You can use index to pop a specific item by position

print(names)
print(names.pop(2))
print(names)

###############################################################################

# .extend can add a list to the end of another list

superlatives = ["Best Dressed", "Class Clown", "Most Likely to be famous"]
print(superlatives)
extra_superlatives = ["Most likely to brighten your day", "Coolest car"]
print(extra_superlatives)
superlatives.extend(extra_superlatives)
print(superlatives) # You can see extra_superlatives was added to the superlatives list

###############################################################################

# slicing is a quick way to split up lists into segments by using index

fruits = ["apple", "pear", "orange", "banana", "pineapple", "watermelon"]
print(fruits)
first_half = fruits[:3]
second_half = fruits[3:]
print(first_half)
# You can see here that the list first_half grabs the first 3 items (Index 0 through 2)

print(second_half)
# You can see here that the list second_half grabs the last 3 items (Index 3 through 5)

print(fruits[-1]) # This index returns the last item in the list
print(fruits[:-1]) # This index returns all items EXCEPT the last

# This last one is a stepper. It will return values from 0 through 5, but skipping
# every other value (hence the 2)
print(fruits[0:5:2])

################################################################################

# DICTIONARIES

# Dictionaries are different than lists in that dictionaries are made up of Keys and Values
# Each key is assigned a value that can be used to return said value
# Dictionaries use {}

materials = {
    1 : "cotton",
    2 : "polyester",
    3 : "linen"
}

print(materials)

# This is how you use the key to return its value
print(materials[2])

###############################################################################

# to append a dictionary, use the following format - dictionary[key] = "value"

materials[4] = "microfiber"
print(materials)

###############################################################################

# use .update to update a key's value

materials.update({4: "bamboo cotton"})
print(materials)
# Notice the syntax used - it is similar to the way dictionaries are created from scratch

###############################################################################

# You can use .pop here too! You have to reference a key to be able to do so though.
# materials.pop() will return an error message

materials.pop(4)
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
fourth_value = example_dict.get("Four", 321)
print(fourth_value)

###############################################################################

# Nested Data Structures
# These data structures can be used together to create complex data sets!
# Below is an example of a dictionary holding multiple dictionaries and lists!


bobs_burgers = {
    "season 1": {
        "episode 1":"cast":["H. Jon Benjamin", "Kristen Schall", "Dan Mintz"],
                    "title": "Food Truckin",
                    "run time": "30 minutes"
    }
    "season 2": {
        "episode 2":"cast":["H. Jon Benjamin", "Kristen Schall", "Dan Mintz"],
                    "title": "Sheesh! Cab, Bob?",
                    "run time": "30 minutes"
    }
