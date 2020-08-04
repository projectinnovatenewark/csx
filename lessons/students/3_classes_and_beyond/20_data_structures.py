"""
Introduce data structures like stacks and queues.
"""

# A stack is a linear data structure that stores items. Often times a list can be used as a stack.
# Stacks follow the Last-in-First-Out (LIFO) principle. You can think of this as if you were 
# stacking coins one on top of the other, the last coin we put on the top is the one that is the 
# first to be removed from the stack later. We can perform two operations on stacks; push() and 
# pop(). When a list is neing used as a stack though, we will use append() instead of push(). 
# If you remember from earlier in the semester, pop() will remove and return the last item 
# in a list.

letters = []

# push() - adds an element to the top of the stack:
# Let's push some letters into our list, but with append().
letters.append('c')
letters.append('a')
letters.append('t')
letters.append('g')

# Now Let's print our stack!
print(f"Initialized Stack: \n {letters}")

# pop() - removes the element at the top of the stack:
# Now let's pop 'letters'.When we print, we should get 'g' as our output.
last_item = letters.pop()
print(f"Removed: {last_item}")

# If we pop again we'll get 't' as our output.
last_item = letters.pop()
print(f"Removed: {last_item}")

# Now we can print our finalized stack.
print(f"Finalized Stack: \n {letters}") # The output should read as ['c', 'a'].

# TODO: Complete Section 1 of TODO 20

##################################################################################################

# A queue is also a linear data structure that stores items. Like stacks, lists can be used
# as a queue. Queues follow the First-in-First-Out (FIFO) principle. You can think of this as 
# waiting in line for movie tickets; the first one to stand in line is the first one to buy 
# a ticket and enjoy the movie. We can perform two operations on queues; enqueue() and dequeue(). 
# When a list is being used as a queue though, we will use append() instead of enqueue() and 
# pop() instead of dequeue().

fruits = []

# enqueue() - adds an element to the end of the queue:
# Let's enqueue some fruits into our list, but with append().
fruits.append('banana')
fruits.append('grapes')
fruits.append('mango')
fruits.append('orange')

# Let's print our initialized queue!
print(f"Initialized Queue: \n {fruits}")

# dequeue - removes the element at the beginning of the queue:
# Now let's dequeue our fruits, but with pop(). Don't forget which 
# item you are looking to remove! We should get 'banana' in our print output.
first_item = fruits.pop(0)
print(f"Removed: {first_item}")

# If we dequeue again we'll get 'grapes'.
first_item = fruits.pop(0)
print(f"Removed: {first_item}")

# Now let's print our finalized queue.
print(f"Finalized Queue: \n {fruits}") # ['mango', 'orange'] is our output.

# TODO: Complete Section 2 of TODO 20
