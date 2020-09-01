"""
Methods you can perform on lists and dictionaries
"""

# TITLE: Section 1 (5 minutes)
# The .append() method adds an item to the end of a list.
medals = ["gold", "silver"]
medals.append("bronze")
print(medals)

# As a reminder, index positions are used to access items in a list- and you can also
# set those values equal to a variable. We will demo those below by printing them using f shorthand.
last_medal = medals[2]
print(f"The last medal is {last_medal} and the first medal is {medals[0]}")

# The .insert() method adds an item to a specific index. The first argument passed to this
# method is the index position you want to add to, and the second argument is the item you want
# to be added to that position.
priority_list = ["go to sports practice", "hangout with friends", "talk to mom", "eat vegetables"]
priority_list.insert(2, "study computer science")
print(priority_list)

# The .remove() method removes a specific item from a list.
fruits = ["apples", "oranges", "asparagus", "bananas"]
fruits.remove("asparagus")
print(fruits)

# The .pop() method removes the last item from a list and returns it's value. Therefore, you could
# set the .pop() method equal to a variable. You could also pick an index postion to remove from
# the list with .pop() method.
waiting_list = ["Candace", "Joe", "Ali", "Miller", "Carla"]

waiting_list_length = len(waiting_list) # The len() function finds the length of a list/dictionary.
print(f"The waiting list's length is {waiting_list_length}")

person_in_line = waiting_list.pop() # This will remove the last item from the list and set
                                    # it equal to a variable, "list_item".

waiting_list.pop(0) # This will remove the first index position's item from the list.

# Let's recalculate the waiting list's length with len() after using pop() twice.
print(f"The waiting list's length is now {len(waiting_list)}")

# Lets print the list item and shopping list on different lines
# TIP: \n creates a new line in the output (Lesson 3 flashback)
print("Last person in line:", person_in_line, "\nList of people waiting:", waiting_list)

####################################################################################################

# TITLE: Section 1.1 (6 minutes)
# The .extend() method adds a list to the end of another list.
# A list of languages.
languages1 = ['French', 'English', 'German']

# Another list of languages.
languages2 = ['Spanish', 'Portuguese']

# This will add the second list's items to the end of the first list's items.
languages1.extend(languages2)

# Extended List.
print('Language List: ', languages1)

# Or if you want to replace an item in a list you can simply set it's index position to a new value.
print("Language List first variable before change", languages1[0]) # This will be French

languages1[0] = "Malaysian" # This will assign "Malaysian" to the first index position of the list.

print("Language List first variable after change", languages1[0]) # This is now be "Malaysian", and
                                                                  # "French" will be removed from the list.

print("Languages List after methods were performed", languages1)

# TODO: Section 1 of TODO 6 (5 minutes for students, 2 minute demo)
####################################################################################################

# TITLE: Section 2 (7 minutes)
# Slicing is a way to segment items in a list.
table_items = ["cloth", "mug", "newspaper", "magazine", "remote", "coozie"]
#                 0       1         2           3           4         5

# The number to the left of the colon ":" is the lower bound of the slice, & the number to the right
# is the upper bound. The upper bound's number's index position is NOT included in the slice.

# This list slice would include the first index item and exclude the fifth index item.
# Therefore, this slice of the list would include index positions 1 through 4.
all_but_first_and_last = table_items[1:5] # TODO: Is index position 1 of "table_items" included
                                          # TODO: in this slice? What about index position 5?
print("All but first and last: ", all_but_first_and_last)

# This slice would include index items zero, one, and two.
# When there is no first number, the "lower bound" would be zero, thus including the first item.
first_half = table_items[:3] # The first item in this slice of the list would be "cloth".
                             # and the last item would be "newspaper"

# This slice would include index items three, four, and five.
# When there is no secondary number, the "upper bound" would be the last index item in the list.
second_half = table_items[3:]
print("The first half:", first_half, "The second half:", second_half)

# This would print all items in the list from index zero to five.
# The third number is a stepper, which would skip every other number.
list_stepper = table_items[0:5:2]

print("List stepper:", list_stepper)

####################################################################################################

# TITLE: Section 2.1 (3 minutes)
# IMPORTANT: List comprehensions are ways to define potentially lengthy lists in one line.
# While you may not recognize the syntax here, just know that you are creating a list of
# squares for all numbers BETWEEN zero and ten, then printing them. "for x in something" means
# that "x" is a variable assigned to the items we are iterating through.

squares = [i**2 for i in range(10)] # Each "iteration" of this loop represents a number between
                                    # 0 and 9, which will be named "i". We square the number "i"
                                    # for each iteration and append it to the list, "squares".
print("Squares list", squares)

# TODO: Section 2 of TODO 6 (3 minutes for students, 2 minute demo)
####################################################################################################

# TITLE: Section 3 (7 minutes)

# Let's define a dictionary called "programming_languages".
programming_languages = {"lang_one": "Python", "lang_two": "Java"}
print(programming_languages)

# Here you can see that the len() function calculates the number of key/value pairs in a dictionary.
print(f"The programming language dictionary's length is {len(programming_languages)}")

# This would add a key of "lang_three" with a value of "CSharp" to the dictionary "programming_languages"
programming_languages["lang_three"] = "CSharp"
print("After adding a key/value pair: ", programming_languages)

# Here is how you would update the value of a key.
programming_languages["lang_two"] = "Golang"
print("post golang", programming_languages)

# The pop method can remove a key/value pair if you pass the key as an argument.
# Now lets pop the key/value pair of "lang_two": "Golang" and set it equal to a variable. That
# variable will be equal to the value, "Golang".
lang_two = programming_languages.pop("lang_two")
print("lang_two is equal to: ", lang_two)
print("post pop 2: programming_languages is equal to: ", programming_languages)

# The get method will find a value for a key in a dictionary.
example_dict = {"num_one": 10, "num_two": 20, "num_three": 30}
second_value = example_dict.get("num_two")
print(second_value)

# If the key that you provide does not exist in the dictionary, it will return "None".
fourth_value = example_dict.get("num_four")
print(fourth_value)

# You can also specify a return value if the key does not exist in the dictionary.
fourth_value = example_dict.get("num_four", "Does not exist.")
print(fourth_value)

# TODO: Section 3 TODO 6 (7 minutes for students, 3 minute demo)
