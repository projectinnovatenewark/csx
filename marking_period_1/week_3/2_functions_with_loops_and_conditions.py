# """
# Here we will show a couple of examples of functions that use loops and conditionals
# """

# unsorted_num_list = [3456, 43659, 123, 9029, 750, 5, 100000]

# # theres a million ways to get it- choose one

# # music lyrics aside, theres so many ways to solve the same problem in coding
# # we will start off real complex, then break it down to a built in function

# def sort_a_list(data_list):
#     new_list = []

#     while data_list:
#         minimum = data_list[0]  # arbitrary number in list
#         for x in data_list: 
#             if x < minimum:
#                 minimum = x
#         new_list.append(minimum)
#         data_list.remove(minimum)

#     print(new_list)

# sort_a_list(unsorted_num_list)

# ##################################################################################################

# # this function does the same thing as the function above
# # an important lesson about becoming a programmer is that you need to understand
# # underlying concepts. There will always be a tool for you to automatically accomplish
# # a task, but what will make you a better programmer is knowing how those tools work
# print(sorted(unsorted_num_list))

# # lets try a for loop within a for loop

# adjective = ["red", "big", "tasty"]
# fruits = ["cherry", "coconut", "mango"]

# for word in adjective:
#     for fruit in fruits:
#         print(word, fruit)

# # oops, that doesnt give us exactly what we expected! let's change it to a dictionary
# # and see if that helps?

# # TODO: switch the above problem to a dictionary

# ##################################################################################################

# # below you will see your first sorting algorithm. there are many varieties of sorting algorithms
def insertion_sort(arr):
    """insertion sort visual: https://www.geeksforgeeks.org/insertion-sort/ """
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        print('begin iteration', 'arr:', arr, 'key: ', key, 'iterator: ', i)

        # move elements of arr[0..i-1], that are greater than key, to one
        # position ahead of their current position
        j = i-1
        while j >= 0 and key < arr[j]:
            print('first up--- arr j + 1:', arr[j+1], 'arr j:', arr[j], "j's log:", j)
            arr[j+1] = arr[j]
            print('second up--- arr j + 1:', arr[j+1], 'arr j:', arr[j], 'arr post change:', arr)
            j -= 1
            print('j:', j)
        print('pre assignment', 'arr j + 1:', arr[j+1], 'key', key)
        arr[j+1] = key
        print('post assignment', 'arr j + 1:', arr[j+1], 'key', key)
        print('end iteration- j is: ', j, 'arr j + 1:', arr[j+1], arr)

    print('completed array: ', arr)

arr = [12, 11, 2, 13, 5, 6]
insertion_sort(arr)

# ##################################################################################################

# # below we want to iterate through a list of lists using a nested for loop,
# # or in simpler terms a for loop within a for loop. this is very common
# # in data structures and you will master this in no time!

# my_movies = [
#     ['How I Met Your Mother', 'Friends', 'Silicon Valley'],
#     ['Family Guy', 'South Park', 'Rick and Morty'],
#     ['Breaking Bad', 'Game of Thrones', 'The Wire']
# ]

# for sublist in my_movies:
#     for movie_name in sublist:
#         char_num = len(movie_name)
#         print("The title " + movie_name + " is " + str(char_num) + " characters long.")
        