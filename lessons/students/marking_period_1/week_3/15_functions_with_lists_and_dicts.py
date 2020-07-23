"""
In This lesson, we will go over using functions to perform actions on lists and dictionaries.
"""

unsorted_num_list = [10, 22, 8, 15, 7, 18, 3]

# Here is a long way to create a function and solve the problem above by sorting them.

# unsorted_num_list and putting the sorted items in a new list.
def sort_a_list(data_list):
    """
    This function removes the minimum of out input list, in this case it is 
    'unsorted_num_list' and appends it, (inserts at the 0 index position), 
    to the new list. This is used to sort the integers in the original list into a new list.
    """
    new_list = []

    while data_list:
        minimum = data_list[0]  # arbitrary number in list
        for x in data_list:
            print('x: ', x, 'minimum: ', minimum)
            if x < minimum:
                print('X is less than MIN. x: ', x, 'minimum: ', minimum)
                minimum = x
        new_list.append(minimum)
        data_list.remove(minimum)
        print('End while loop iteration. new_list: ', new_list, 'data_list: ', data_list)

    print(new_list)

sort_a_list(unsorted_num_list)

# This function does the same thing as the function above function.

# An important lesson about becoming a programmer is that you must understand underlying concepts.
# There's always tools to solve your problem quickly with imported functions, but what matters
# is that you understand how those functions work!
print(sorted(unsorted_num_list))