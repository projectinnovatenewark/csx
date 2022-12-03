"""
Introduce data structures like queue and stack
"""

# Python lists breakdown: https://developers.google.com/edu/python/lists
# Python dicts breakdown: https://developers.google.com/edu/python/dict-files
# and methods for dicts: 


# Stacks follow the Last-in-First-Out (LIFO) principle. As if stacking
# coins one on top of the other, the last coin we put on the top
# is the one that is the first to be removed from the stack later.

letters = []

# Push - add element to the top of the stack:
# Let's push some letters into our list
letters.append('c')
letters.append('a')
letters.append('t')
letters.append('g')

# Pop - remove element at the top of the stack:
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

# Enqueue - add element to the end of the queue:
# Let's enqueue some fruits into our list
fruits.append('banana')
fruits.append('grapes')
fruits.append('mango')
fruits.append('orange')

# Dequeue - removes the element at the beginning of the queue:
# Now let's dequeue our fruits, we should get 'banana'
first_item = fruits.pop(0)
print(first_item)

# If we dequeue again we'll get 'grapes'
first_item = fruits.pop(0)
print(first_item)

# 'mango' and 'orange' remain
print(fruits) # ['c', 'a']

# checkout from master, pull master, add/commit changes on local branch, push changes to branch on remote repository, create pull request,
# get pull request (or PR as its referred to) reviewed by a collaborator, address any changes that might need to be made, have 
# collaborator approve, merge the code to master, checkout to master on local computer, pull from master to update local branch,
# checkout to new branch for some new code to be written, rinse and repeat!
