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

# DICTIONARIES

# the append method also works for dicionaries
programming_languages = {1 : "Python", 2 : "Java"}
print(programming_languages)

programming_languages[3] = "CSharp"
print("post c sharp", programming_languages)

# the update method will update the value of a key
programming_languages.update({2: "Golang"})
print("post golang", programming_languages)

# while the pop can remove a key-value pair
programming_languages.pop(1)
print("post pop 1", programming_languages)
