"""
Introduce data structures like queue, stack, etc.
"""


# Stacks follow the Last-in-First-Out (LIFO) principle. As if stacking
# coins one on top of the other, the last coin we put on the top
# is the one that is the first to be removed from the stack later.

letters = []

# push - adds an element to the top of the stack:
# Let's push some letters into our list
letters.append('c')
letters.append('a')
letters.append('t')
letters.append('g')

# pop - removes the element at the top of the stack:
# Now let's pop letters, we should get 'g'
last_item = letters.pop()
print(last_item)

# If we pop again we'll get 't'
last_item = letters.pop()
print(last_item)

# 'c' and 'a' remain
print(letters) # ['c', 'a']

##################################################################################################

# Queues follow the First-in-First-Out (FIFO) principle.
# As if waiting in a queue for the movie tickets, the first one to stand in line
# is the first one to buy a ticket and enjoy the movie.

fruits = []

# enqueue - adds an element to the end of the queue:
# Let's enqueue some fruits into our list
fruits.append('banana')
fruits.append('grapes')
fruits.append('mango')
fruits.append('orange')

# dequeue - removes the element at the beginning of the queue:
# Now let's dequeue our fruits, we should get 'banana'
first_item = fruits.pop(0)
print(first_item)

# If we dequeue again we'll get 'grapes'
first_item = fruits.pop(0)
print(first_item)

# 'mango' and 'orange' remain
print(fruits) # ['c', 'a']