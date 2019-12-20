"""
Here we will show a couple of examples of functions that use loops and conditionals
"""

# functions are blocks of code that execute when called upon. a function definition is the naming
# of these set of instructions. `def functionName([arguments-if-needed]):` is the format.
# functions can take an argument and do things with it inside the function. if you want to
# create a function that adds 10 to any given number and prints the new number, you would
# write something like this:

def addTen(x):
    newNum = x + 10
    print(newNum)

# then to call this function and pass it an argument of a number, do this
addTen(5)

# remember, if we wanted to set a number equal to a variable and pass that variable, it would be
# doing the same thing
num = 23
addTen(num)

##################################################################################################

unsorted_num_list = [3456, 43659, 123, 9029, 750, 5, 100000]

# here is a long way to create a function and solve the problem above by sorting the above list
# and putting the sorted items in a new list
def sort_a_list(data_list):
    new_list = []

    while data_list:
        minimum = data_list[0]  # arbitrary number in list
        for x in data_list: 
            if x < minimum:
                minimum = x
        new_list.append(minimum)
        data_list.remove(minimum)

    print(new_list)

sort_a_list(unsorted_num_list)

# this function does the same thing as the function above
# an important lesson about becoming a programmer is that you need to understand
# underlying concepts. There will always be a tool for you to automatically accomplish
# a task, but what will make you a better programmer is knowing how those tools work
print(sorted(unsorted_num_list))

##################################################################################################

# lets try a for loop within a for loop. we want the output to be "red cherry", "big coconut", etc.

adjective = ["red", "big", "tasty"]
fruits = ["cherry", "coconut", "mango"]

for word in adjective:
    for fruit in fruits:
        print(word, fruit)

# TODO: oops, that doesnt give us exactly what we expected! let's change it to a dictionary
# TODO: and see if that helps?

# TODO: switch the above problem to a dictionary and get the desired output

##################################################################################################

# below you will see your first sorting algorithm. there are many varieties of sorting algorithms
# reference link here: https://tutorialedge.net/compsci/sorting/insertion-sort-in-python/
def insertion_sort(some_list):
    # for every element in our array
    for index in range(1, len(some_list)):
        current = some_list[index]
        position = index

        while position > 0 and some_list[position-1] > current:
            print("Swapped {} for {}".format(some_list[position], some_list[position-1]))
            some_list[position] = some_list[position-1]
            print(some_list)
            position -= 1

        some_list[position] = current

    print("Sorting Completed.")
    print(some_list)

arr = [12, 11, 2, 13, 5, 6, 19, 9, 17]
insertion_sort(arr)

##################################################################################################

# below we want to iterate through a list of lists using a nested for loop,
# or in simpler terms a for loop within a for loop. this is very common
# in data structures and you will master this in no time!

my_movies = [
    ['How I Met Your Mother', 'Friends', 'Silicon Valley'],
    ['Family Guy', 'South Park', 'Rick and Morty'],
    ['Breaking Bad', 'Game of Thrones', 'The Wire']
]

for sublist in my_movies:
    for movie_name in sublist:
        char_num = len(movie_name)
        print("The title " + movie_name + " is " + str(char_num) + " characters long.")
        