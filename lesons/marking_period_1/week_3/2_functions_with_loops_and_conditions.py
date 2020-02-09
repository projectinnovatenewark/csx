"""
Here we will show a couple of examples of functions that use loops and conditionals
"""

# functions are blocks of code that execute when called upon. a function definition is the naming
# of these set of instructions. `def functionName([arguments-if-needed]):` is the format.
# functions can take an argument and do things with it inside the function. if you want to
# create a function that adds 10 to any given number and prints the new number, you would
# write something like this:

def addTen(x): # the parameter, in this case 'x', is sometimes called an alias for the actual
               # argument that is passed
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

my_shows = [
    ['How I Met Your Mother', 'Friends', 'Silicon Valley'],
    ['Family Guy', 'South Park', 'Rick and Morty'],
    ['Breaking Bad', 'Game of Thrones', 'The Wire']
]

for sublist in my_shows:
    for show_name in sublist:
        char_num = len(show_name)
        print("The title " + show_name + " is " + str(char_num) + " characters long.")

##################################################################################################

# below we want to iterate through a dictionary of key value pairs- where the values are
# dictionaries! We wil again use a nested for loop here. Here we have the first six
# episodes from the first three seasons each in the show, The Office.

the_office = {
    "Season 1":
    {
        "Episode 1" : "Pilot",
        "Episode 2" : "Diversity Day",
        "Episode 3" : "Health Care",
        "Episode 4" : "The Alliance",
        "Episode 5" : "Basketball",
        "Episode 6" : "Hot Girl",
    },
    "Season 2":
    {
        "Episode 1" : "The Dundies",
        "Episode 2" : "Sexual Harassment",
        "Episode 3" : "Office Olympics",
        "Episode 4" : "The Fire",
        "Episode 5" : "Halloween",
        "Episode 6" : "The Fight",
    },
    "Season 3":
    {
        "Episode 1" : "Gay Witch Hunt",
        "Episode 2" : "The Convention",
        "Episode 3" : "The Coup",
        "Episode 4" : "Grief Counseling",
        "Episode 5" : "Initiation",
        "Episode 6" : "Diwali",
    },
}

# for example, to find the title of episode 1 in season 3, you would use this:
# print(the_office["Season 3"]["Episode 1"])

# TODO: Question 1: What type of data set is the_office? Is it a list, dictionary, string, etc.?

# TODO: Question 2: Find the value of 'Season 3'. Print it. Now Print out 'Episode 6' in Season 3.

# TODO: Question 3: Loop through the the_office object and print out the value of each key.

# TODO: Question 4: Create a nested for loop that would list an output for each episode

# TODO: Question 5: that would state "Episode __ of Season __ is titled '____' "

##################################################################################################

# Lets try looping through a different nested data structure. Imagine having a set of classes
# in a list. However, each class would be an object with info like subject, level, teacher,
# students, and average quarterly grades. Following the data set, we will show a couple examples
# of how to use it.

math_classes = [
    {
        'subject': 'Math',
        'level': 'Geometry',
        'teacher': 'Professor Alisson',
        'students': ['Bill', 'Bob', 'Beatrice', 'Brandi'],
        'averages': {
            'MP1': 89.5,
            'MP2': 82,
            'MP3': 92,
            'MP4': 94,
        }
    },
    {
        'subject': 'Math',
        'level': 'Algebra',
        'teacher': 'Professor Dylan',
        'students': ['Callie', 'Chris', 'Cayla', 'Chantelle'],
        'averages': {
            'MP1': 95,
            'MP2': 86,
            'MP3': 97,
            'MP4': 79,
        }
    },
    {
        'subject': 'Math',
        'level': 'Calculus',
        'teacher': 'Professor Johnson',
        'students': ['Dani', 'Damien', 'Dinesh', 'Dira'],
        'averages': {
            'MP1': 99,
            'MP2': 86,
            'MP3': 77,
            'MP4': 94.8,
        }
    },
]

# for example, to find the value of MP4 in the Calculus level math class, I would run
# print(math_classes[3]['averages]['MP4])

# TODO: Question 1: What type of data set is classes? Is it a list, dictionary, string, etc.?

# TODO: Question 2:   How would I find the entire dictionary for the calculus course?
# TODO: Question 2: How would I find the 2nd student in the list of students from the Algebra class?

# TODO: Question 3: How would I find the MP4 grade from the calculus class?

# TODO: Question 4: How would I print each student's name from all of the classes?

# TODO: Question 5: How could I modify the above to print a statement for each student to say
# TODO: 'Teacher ____ teaches subject _____ to ______'

# TODO: Question 6: How could I find yearly grades average between marking periods for each class?
# TODO: for example, I would want all of the averages added up for each course, then divided by the
# TODO: number of marking periods to determine the average yearly grade for the course.
        