"""
Here we will show a couple of examples of functions that use loops and conditionals
"""

# Below we want to iterate through a list of lists using a nested for loop,
# or in simpler terms a for loop within a for loop. This is very common
# in data structures and you will master this in no time! The first sublist in
# my_shows would be the entire list of ['How I Met Your Mother', 'Friends', 'Silicon Valley']
# Then, second for loop of "for show_name in sublist:" would iterate through each of those
# items in the list. Once the second for loop is completed, the program will return to the first
# for loop and move on to the second list of ['Family Guy', 'South Park', 'Rick and Morty'] and
# repeat the second for loop for that list's items.

my_shows = [
    ['How I Met Your Mother', 'Friends', 'Silicon Valley'],
    ['Family Guy', 'South Park', 'Rick and Morty'],
    ['Breaking Bad', 'Game of Thrones', 'The Wire']
]

for sublist in my_shows:
    for show_name in sublist:
        char_num = len(show_name)
        print("The title " + show_name + " is " + str(char_num) + " characters long.")

####################################################################################################

# Below we want to iterate through a dictionary of key value pairs - where the values are
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

# For example, to find the title of episode 1 in season 3, you would use this:
# print(the_office["Season 3"]["Episode 1"]). Starting from the beginning, 'the_office' 
# is a dictionary. Each key in 'the_office' is paired with another dictionary as its value.

# Lets find the value of 'Season 3' and print it.

print(the_office["Season 3"])

# Now lets print out the title of 'Episode 6' in Season 3.
season_3 = the_office["Season 3"]
print(season_3["Episode 6"])

# Let's remember something when using a nested for loop here. The first iteration of our
# top level for loop would be "Season 1" since it is the first key in our dictionary. You
# might want to set a variable between the top level for loop and the nested loop just as we did above. Remember,
# if the iteration of each loop is a key, that variable you'd set between loops should follow
# the format of variableName = dictionaryName[keyName]. Then, you can iterate through that new
# variable, since it should equal the value of the key which is a dictionary. The first iteration of the below
# will print "Season 1, Episode: 1 Pilot"


for season_num in the_office:
    season = the_office[season_num] # Setting variables can be very helpful in making your code more readable
    for episode_num in season:
        episode = season[episode_num]
        print(f"{season_num}, {episode_num}: {episode}")

# TODO: Section 1 of TODO 12

####################################################################################################

# Lets try looping through a different nested data structure. Imagine having a set of math classes
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

# Using what we learned from the previous section, we want to put our for loops 
# inside meaningful functions; that way we can call on them whenever we need to use them.
# This allows our program to be a little more dynamic if we have other data sets besides
# 'math_classes' that have a similar structure. Lets see how to find the entire dictionary 
# for the Calculus course. To do so, we will set up a for loop with a conditional 
# statement in it to test which level we are iterating on. Then we can go ahead 
# and print the entire calculus dictionary, also known as 'math_classes' third key. We want to 
# put this inside a funciton 'findCalc' and pass the parameter of data so it's versatile.
# Then when we call the function to run, we pass the argument of 'math_classes' to loop through.

def findCalc(data):
    for key in data:
        level = key["level"]
        if (level == "Calculus"):
            print(key)

findCalc(math_classes)

# Now lets find the 2nd student in the list of students from the Algebra class.
# Remember to keep in mind setting variables is important! It gives 
# readability to your code and it's easier to get your desired output. Note how the 
# name of the function stays relevant to the purpose of your code. Just like variable
# naming, we want to give useful names to our functions. 

def findSecond(data):
    for key in data:
        level = key["level"]
        student = key["students"]
        if (level == "Algebra"):
            print(student[1])

findSecond(math_classes)

# Lets print each student from every class inside the funciton 'printStudents'. We want to iterate
# through each classand then iterate through each student in the class and print their name.

def printStudents(data):
    for key in data:
        students = key["students"]
        for student in students:
            print(student)

printStudents(math_classes)

# Lets make the above a little more coherent. Now we want to print the statement,
# '{Teacher} teaches {subject} to {student}'. First we need to set our variables just like
# in previous examples, and a simple nested for loop can be used!

def printStatement(data):
    for key in data:
        students = key["students"]
        teacher = key["teacher"]
        subject = key["subject"]   
        for student in students:
            print("{} teaches {} to {}".format(teacher, subject, student))

printStatement(math_classes)

# TODO: Section 2 of TODO 12
