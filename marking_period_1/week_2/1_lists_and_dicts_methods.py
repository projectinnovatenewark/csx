"""
Actions you can perform on lists and dictionaries
"""

# LIST

# the append method adds an item to the end of a list
medals = ["gold", "silver"]
medals.append("bronze")
print(medals)

##############################################################################################

# the insert method adds an item to a specific index
priority_list = ["go to sports practice", "hangout with friends", "talk to mom", "eat vegetables"]
priority_list.insert(2, "study computer science")
print(priority_list)

##############################################################################################

# the remove method will remove a specific item from a list
fruits = ["apples", "oranges", "asparagus", "bananas"]
fruits.remove("asparagus")
print(fruits)

##############################################################################################

# the pop method will remove the last item from a list and return it's value
# you could also pick an index item to remove. i.e. removing the first item and
# returning it's value would be .pop(0)
shopping_list = ["t-shirt", "laptop", "belt", "dress", "mousepad"]
last_item = shopping_list.pop()
print("last item:", last_item, "and shopping list:", shopping_list)

##############################################################################################

# the extend method adds a list to the end of another list
# language list
languages1 = ['French', 'English', 'German']

# another list of language
languages2 = ['Spanish', 'Portuguese']

languages1.extend(languages2)

# Extended List
print('Language List: ', languages1)

##############################################################################################

# # slicing is a way to segment items in a list
table_items = ["cloth", "mug", "newspaper", "magazine", "remote", "coozie"]

# this slice would include index items zero, one, and two
first_half = table_items[:3]

# this slice would include index items three, four, and five
second_half = table_items[3:]
print("The first half:", first_half, "The second half:", second_half)

# you can include negative numbers when indexing which start at the end of the list
# this item would be the last item in the list
last_item = table_items[-1]

# this list would include all items except the last one
all_but_last_item = table_items[:-1]

# this list would include the first index item and exclude the fifth index item
all_but_first_and_last = table_items[1:5]

# this would print all items in the list from index zero to five
# and the third number is a stepper, which would skip every other number
list_stepper = table_items[0:5:2]
print("List stepper:", list_stepper)

##############################################################################################

# list comprehensions are ways to define potentially lengthy lists in one line
# while you may not recognize the syntax here, just know that you are creating a list of
# squares for all numbers between zero and ten and printing them. for ___ in something means
# that ____ is what we call the items we are iterating through.
squares = [i**2 for i in range(10)]
print("Squares list", squares)

# what if we wanted to only find the squares of odd numbers? lets add a condition to the list
# comprehension. the order of a list comprehension is action - for loop - conditional (optional)
squares_of_odd_numbers = [i**2 for i in range(1, 10) if i % 2 != 0]
print("Squares of odd numbers list", squares_of_odd_numbers)

# lets throw an extra condition in there. what if we want ONLY even numbers NOT including 4?
# we can simply use 'and'! also, since zero does not have a remainder when divided by two,
# 
squares_of_even_numbers_without_4 = [i**2 for i in range(1, 10) if i % 2 == 0 and i != 4]
print("Squares of even numbers without 4 list", squares_of_even_numbers_without_4)

##############################################################################################

# DICTIONARIES

# the equivalent of an append method for dictionaries is shown here
programming_languages = {1 : "Python", 2 : "Java"}
print(programming_languages)

programming_languages[3] = "CSharp"
print("post c sharp", programming_languages)

# the update method will update the value of a key
programming_languages.update({2: "Golang"})
print("post golang", programming_languages)

##############################################################################################

# while the pop can remove a key-value pair
programming_languages.pop(1)
print("post pop 1", programming_languages)

##############################################################################################

# the get method will find a value for a key in a dictionary
# you can also specify a return value if the key does not exist in the dictionary
example_dict = {"One": 10, "Two": 20, "Three": 30}
second_value = example_dict.get("Two")
print(second_value)

# a second argument with the get function is what is returned if the first argument isnt in the dict
# this will return 321 since there is no key "Four"
fourth_value = example_dict.get("Four", 321)
print(fourth_value)
