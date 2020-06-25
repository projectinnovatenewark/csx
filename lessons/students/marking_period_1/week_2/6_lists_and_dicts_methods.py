"""
Actions you can perform on lists and dictionaries
"""

# LIST METHODS

# The append method adds an item to the end of a list.
medals = ["gold", "silver"]
medals.append("bronze")
print(medals)

####################################################################################################

# The insert method adds an item to a specific index.
priority_list = ["go to sports practice", "hangout with friends", "talk to mom", "eat vegetables"]
priority_list.insert(2, "study computer science")
print(priority_list)

####################################################################################################

# The remove method removes a specific item from a list.
fruits = ["apples", "oranges", "asparagus", "bananas"]
fruits.remove("asparagus")
print(fruits)

####################################################################################################

# The pop method removes the last item from a list and returns it's value. Therefore, you could
# set the pop() method equal to a variable.
# You could also pick an index item to remove (i.e. removing the first item and
# returning it's value would be .pop(0))
shopping_list = ["t-shirt", "laptop", "belt", "dress", "mousepad"]
last_item = shopping_list.pop()
print("last item:", last_item, "and shopping list:", shopping_list)

####################################################################################################

# The extend method adds a list to the end of another list.
# language list
languages1 = ['French', 'English', 'German']

# Another list of language.
languages2 = ['Spanish', 'Portuguese']

languages1.extend(languages2)

# Extended List
print('Language List: ', languages1)

# Or if you want to replace an item in a list you can simply set it's index position to a new value.
languages1[0] = "Malaysian"
print(languages1)

#TODO: Section 1 of TODO 6
####################################################################################################

# Slicing is a way to segment items in a list.
table_items = ["cloth", "mug", "newspaper", "magazine", "remote", "coozie"]

# This slice would include index items zero, one, and two.
# When there is no first number, the "lower bound" would be zero, thus including the first item.
first_half = table_items[:3]

# This slice would include index items three, four, and five.
# When there is no secondary number, the "upper bound" would be the last index item in the list.
second_half = table_items[3:]
print("The first half:", first_half, "The second half:", second_half)

# You can include negative numbers when indexing which start at the end of the list.
# This item would be the last item in the list.
last_item = table_items[-1]

# This list would include all items except the last one.
all_but_last_item = table_items[:-1]

# This list would include the first index item and exclude the fifth index item.
all_but_first_and_last = table_items[1:5]

# This would print all items in the list from index zero to five.
# The third number is a stepper, which would skip every other number.
list_stepper = table_items[0:5:2]
print("List stepper:", list_stepper)

#TODO: Section 2 of TODO 6
####################################################################################################

# List comprehensions are ways to define potentially lengthy lists in one line.
# While you may not recognize the syntax here, just know that you are creating a list of
# squares for all numbers between zero and ten, then printing them. "for x in something" means
# that "x" is a variable assigned to the items we are iterating through.
squares = [i**2 for i in range(10)]
print("Squares list", squares)

# What if we wanted to only find the squares of odd numbers? Lets add a condition to the list
# comprehension. The order of a list comprehension is action - for loop - conditional (optional)
squares_of_odd_numbers = [i**2 for i in range(1, 10) if i % 2 != 0]
print("Squares of odd numbers list", squares_of_odd_numbers)

# Lets throw an extra condition in there. What if we want ONLY even numbers NOT including 4?
# We can simply use 'and'. Also, since zero does not have a remainder when divided by two, we will
# check to see if "i % 2" is equal to zero, and if it is then "i" would be zero.

squares_of_even_numbers_without_4 = [i**2 for i in range(1, 10) if i % 2 == 0 and i != 4]
print("Squares of even numbers without 4 list", squares_of_even_numbers_without_4)

#TODO: Section 3 of TODO 6
####################################################################################################

# DICTIONARIES

# The adding of a key/value pair to a dictionary is shown below.
programming_languages = {"One" : "Python", "Two" : "Java"}
print(programming_languages)

# This would add a key of "Three" with a value of "CSharp" to the dict "programming_languages"
programming_languages["Three"] = "CSharp"
print("post c sharp", programming_languages)

# The update method will update the value of a key.
programming_languages.update({"Two": "Golang"})
print("post golang", programming_languages)

# The generic way to update the value of a key.
programming_languages["Two"] = "Julia"
print("post julia", programming_languages)

# The pop method can remove a key-value pair if you pass the key as an argument. Just as in lists,
# the pop method returns a value, so you can set it equal to a variable.
lang_one = programming_languages.pop("One")
print("post pop 1", programming_languages)

# Now lets pop the key/value pair of ``"Two": "Julia"` and set it equal to a variable. That variable
# will be equal to the key.
lang_two = programming_languages.pop("Two")
print("post pop 2: programming_languages is equal to- ", programming_languages, "and the lang_two variable that we set equal to a pop() is- ", lang_two)

#TODO: Section 4 of TODO 6
####################################################################################################

# the get method will find a value for a key in a dictionary
# you can also specify a return value if the key does not exist in the dictionary
example_dict = {"One": 10, "Two": 20, "Three": 30}
second_value = example_dict.get("Two")
print(second_value)

# a second argument with the get function is what is returned if the first argument isnt in the dict
# this will return 321 since there is no key "Four"
fourth_value = example_dict.get("Four", 321)
print(fourth_value)

#TODO: Section 5 of TODO 6