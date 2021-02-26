"""
Methods you can perform on lists and dictionaries
"""

# TITLE: Section 1.1 - Adding and Removing Items From Lists, Reading List Items and Length (5 minutes)
# The .append() method adds an item to the end of a list.
medals = ["gold", "silver"]
medals.append("bronze")
print(medals)

# As a reminder, index positions are used to access items in a list. You can also set those values
# equal to a variable. We will demo this concept below.
last_medal = medals[2]
print(f"The last medal is {last_medal} and the first medal is {medals[0]}")

# The .insert() method adds an element at a given index. The first argument passed defines the index
# position, and the second argument defines the element you want to add to the list.
priority_list = ["go to sports practice", "hangout with friends", "talk to mom", "eat vegetables"]
priority_list.insert(2, "study computer science") # This will insert "study computer science" into
                                                  # "priority_list" at index position 2.
print(priority_list)

# The .remove() method removes a given item from a list.
fruits = ["apples", "oranges", "asparagus", "bananas"]
fruits.remove("asparagus")
print(fruits)

# The .pop() method removes the last item from a list and returns it's value. Therefore, you could
# set the .pop() method equal to a variable. 

last_fruit = fruits.pop()
print(f"The last fruit in the list is {last_fruit}") # This will remove the last item from the list and
                                                     # set it equal to the variable, "last_fruit".
print(fruits)

# You can also pick an index position to remove from the
# list with the .pop() method by providing an argument defining the desired index position.

first_fruit = fruits.pop(0) # This will remove the first index position's item from the list.

# The len() function is a built-in function that finds the length of a list/dictionary.

waiting_list = ["Candace", "Joe", "Ali", "Miller", "Carla"]

waiting_list_length = len(waiting_list) 
print(f"The waiting list's length is {waiting_list_length}")

person_in_line = waiting_list.pop() # Again, this will remove the last item from the list and set it
                                    # equal to a variable, "person_in_line".

# Let's recalculate the waiting list's length with len() after using pop().
print(f"The waiting list's length is now {len(waiting_list)}")

# Now print the list item and shopping list on different lines.
# TIP: \n creates a new line in the output (Lesson 3 flashback)
print(f"Last person in line: {person_in_line}\nList of people waiting: {waiting_list}.")

####################################################################################################

# TITLE: Section 1.2 - Extending and Modifying Lists (6 minutes)
# The .extend() method adds a list to the end of another list.

languages1 = ['French', 'English', 'German'] # A list of languages.

languages2 = ['Spanish', 'Portuguese'] # Another list of languages.

# Below will add items in "languages2" to the end of "languages1".
languages1.extend(languages2)

print(f'Language List: {languages1}.') # Printing the extended list.

# If you want to replace an item in a list you can simply set it's index position to a new value.
print(f"Language List first variable before change: {languages1[0]}.")

languages1[0] = "Mandarin" # This will assign "Mandarin" to the first index position of 
                           # languages1".

print(f"Language List first variable after change: {languages1[0]}.") # "languages1[0]" will now be
                                                                      # equal to "Mandarin", and
                                                                      # "French" will be removed from
                                                                      # the list.

print(f"Languages List after methods were performed {languages1}.")

# TODO: Section 1 of TODO 6 (5 minutes for students, 2 minute demo)
####################################################################################################

# TITLE: Section 2.1 - Creating Segments, or "Slices", of Lists (7 minutes)

# Slicing is a way to segment items in a list.
table_items = ["cloth", "mug", "newspaper", "magazine", "remote", "coozie"]
#                 0       1         2           3           4         5

# The syntax to slice a list is "list_name[lower_bound:upper_bound]". (Ex. list_example[2:4]) The
# number to the left of the colon ":" is the lower bound of a slice, and the number to the right is
# the upper bound. The upper bound's index position is NOT included in a slice.

# The list slice below would include the first index item and exclude the fifth index
# item. Therefore, this slice of the list would include index positions 1 through 4.
all_but_first_and_last = table_items[1:5] # TODO: Is index position 1 of "table_items" included
                                          # TODO: in this slice? What about index position 5?
print(f"All but first and last: {all_but_first_and_last}.")

# When there is no first number defined, the "lower bound" is equal to zero and will include the
# first item in the list. For example, the following slice would include index items zero, one, and
# two.
first_half = table_items[:3] # The first item in this slice of the list would be "cloth".
                             # and the last item would be "newspaper"

# When there is no secondary number defined, the "upper bound" is the last item in the list.
second_half = table_items[3:] # This slice would include index items three, four, and five.
print(f"The first half: {first_half} | The second half: {second_half}.")

# The third number in a slice is called a stepper. The stepper defines the interval to skip between
# index positions.
list_stepper = table_items[0:5:2] # This would print all items in the list from index zero to five
                                  # while skipping every other number.

print(f"List stepper:  {list_stepper}.")

####################################################################################################

# TITLE: Section 2.2 - List Comprehensions (3 minutes)

# IMPORTANT: List comprehensions are ways to define potentially lengthy lists in one line.
# While you may not recognize the syntax here, just know that you are creating a list of
# squares for all numbers BETWEEN zero and ten, then printing them. "for x in something" means
# that "x" is a variable assigned to the items we are iterating through.

squares = [i**2 for i in range(10)] # Each "iteration" of this loop represents a number between
                                    # 0 and 9, which will be named "i". We square the number "i"
                                    # for each iteration and append it to the list, "squares".

print(f"Squares list {squares}")

# TODO: Section 2 of TODO 6 (3 minutes for students, 2 minute demo)
####################################################################################################

# TITLE: Section 3 - Adding, Removing, Reading and Changing Dictionaries' Key/Value Pairs (7 minutes)

# Let's define a dictionary called "programming_languages".
programming_languages = {"lang_one": "Python", "lang_two": "Java"}
print(programming_languages)

# Here you can see that the len() function calculates the number of key/value pairs in a dictionary.
print(f"The programming language dictionary's length is {len(programming_languages)}")

# Bracket notation is used to create a new key/value pair in a dictionary. The syntax for this is
# "dicty[new_key] = value". For example, we can add a key of "lang_three" with a value of "CSharp" to
# the dictionary "programming_languages", as seen below.
programming_languages["lang_three"] = "CSharp"
print(f"After adding a key/value pair: {programming_languages}")

# Bracket notation is also used to update values of a given key that already exists in
# the dictionary.
programming_languages["lang_two"] = "Golang" # "lang_two" already exists, so its value will change
                                             # from "Java" to "Golang".
print(f"post golang {programming_languages}")

# The pop method removes a key/value pair when you pass the key as an argument.
lang_two = programming_languages.pop("lang_two")
print(f"lang_two is equal to: {lang_two}")
print(f"post pop 2: programming_languages is equal to: {programming_languages}")

# The get method is used to find a value for a key in a dictionary.
example_dict = {"num_one": 10, "num_two": 20, "num_three": 30}
second_value = example_dict.get("num_two")
print(second_value)

# If the key that you provide in the .get() method does not exist in the dictionary, it will
# return "None".
fourth_value = example_dict.get("num_four")
print(fourth_value)

# You can also specify a return value if a given key does not exist in the dictionary.
fourth_value = example_dict.get("num_four", "Does not exist.")
print(fourth_value)

# TODO: Section 3 TODO 6 (7 minutes for students, 3 minute demo)
