"""
Working with nested data.
"""

# TITLE: Section 1 - Nested Lists and Nested Loops

# In programming, nesting is a popular way of storing information and/or objects in layers. In this
# lesson we will cover a few examples of different nested data structures and how to iterate through
# them.

# In the following example, "my_shows" is considered a nested data structure because it is a list
# where each element is also a list. To iterate through "my_shows" we would use a "for loop". Then,
# to iterate through each sublist, we can use a second "for loop".

my_shows = [
  ['How I Met Your Mother', 'The Office', 'Silicon Valley'],
  ['Family Guy', 'South Park', 'Rick and Morty'],
  ['Breaking Bad', 'Game of Thrones', 'The Wire']
]

# The below nested for loop will first print the sublist of shows for the current iteration followed by
# each individual show within the sublist.
for sublist in my_shows: # The variable "sublist" represents each list of shows in "my_shows".
  print(f"Current sublist: {sublist}")
  for show_name in sublist: # The variable "show_name" represents each show in a given "sublist".
    print(f"Current show: {show_name}")

# TODO: Complete Section 1 of TODO 13 (7 min for students, 4 min for demo)

####################################################################################################$

# TITLE: Section 2 - Nested Dictionaries and Nested Loops

# In the next example we will iterate through a nested dictionary called "spongebob". A nested
# dictionary consists of key value pairs where the value of each key is another dictionary. Just as
# in section 1, we can use a nested for loop to iterate through each nested dictionary. The
# dictionary "spongebob" includes 3 seasons with 6 episodes in each season.

spongebob = {
  "Season 1": {
    "Episode 1": "Help Wanted",
    "Episode 2": "Bubblestand",
    "Episode 3": "Jellyfishing",
    "Episode 4": "Naughty Nautical Neighbors",
    "Episode 5": "Pizza Delivery",
    "Episode 6": "Mermaid Man and Barnacle Boy",
  },
  "Season 2": {
    "Episode 1": "Your Shoe's Untied",
    "Episode 2": "Something Smells",
    "Episode 3": "Big Pink Loser",
    "Episode 4": "Dying for Pie",
    "Episode 5": "Wormy",
    "Episode 6": "Grandma's Kisses",
  },
  "Season 3": {
    "Episode 1": "The Algae's Always Greener",
    "Episode 2": "Club SpongeBob",
    "Episode 3": "Just One Bite",
    "Episode 4": "Nasty Patty",
    "Episode 5": "Mermaid Man and Barnacle Boy IV",
    "Episode 6": "Snowball Effect",
  },
}

# To find the title of episode 1 in season 3 of "spongebob", you would use the following syntax:
# "spongebob["Season 3"]["Episode 1"]".

# Let's use the above syntax to find the value of "Season 3" and print it:
print(spongebob["Season 3"])

# Now lets print out the title of "Episode 6" in Season 3:
season_3 = spongebob["Season 3"]
print(season_3["Episode 6"])

# Let's walk through the control of the nested "for loop" below. The first iteration of our top
# level "for loop" is "Season 1" since it is the first key in our dictionary. To make iterating
# through each season easier to read, we use the following syntax: variable = dictionary[key]. In this
# example the variable is called "season", which is the iterable object in the second "for loop".
# The first iteration of "season" will be the key/value pair "Episode 1: "Help Wanted"".

for season_num in spongebob:
  season = spongebob[season_num] # Here we create the variable "season" to use as the iterable for
                                 # the second "for loop".
  for episode_num in season:
    episode = season[episode_num]
    print(f"{season_num}, {episode_num}: {episode}") # IMPORTANT: You can reference variables
                                                     # IMPORTANT: in the top level "for loop".

# TODO: Complete Section 2 of TODO 13 (7 min for students, 4 min for demo)

####################################################################################################

# TITLE: Section 3 - Additional Nested Data Structures

# Lets try looping through a nested data structure that uses both lists and dictionaries. The
# following example includes a list of math classes, where each class is an object with associated
# information such as subject, level, teacher, students, and average quarterly grades. Following the
# data set, we will show a couple examples of how to use it.

math_classes = [
  {
    "subject": "Math",
    "level": "Geometry",
    "teacher": "Professor Alisson",
    "students": ["Bill", "Bob", "Beatrice", "Brandi"],
    "averages": {
      "MP1": 89.5,
      "MP2": 82,
      "MP3": 92,
      "MP4": 94,
    }
  },
  {
    "subject": "Math",
    "level": "Algebra",
    "teacher": "Professor Dylan",
    "students": ["Callie", "Chris", "Cayla", "Chantelle"],
    "averages": {
      "MP1": 95,
      "MP2": 86,
      "MP3": 97,
      "MP4": 79,
    }
  },
  {
    "subject": "Math",
    "level": "Calculus",
    "teacher": "Professor Johnson",
    "students": ["Dani", "Damien", "Dinesh", "Dira"],
    "averages": {
      "MP1": 99,
      "MP2": 86,
      "MP3": 77,
      "MP4": 94.8,
    }
  },
]


# To find the entire dictionary for the Calculus course, we can use a for loop with a conditional
# statement in it to test which level we are iterating over. Then we can print the entire calculus
# dictionary, also known as the third key in "math_classes".

for key in math_classes:
  level = key["level"]
  if level == "Calculus":
    print(key)

# We can use the same approach to find the 2nd student in the list of students from the Algebra
# course.

# IMPORTANT: Remember that setting variables is important for making your code more readable.

for key in math_classes:
  level = key["level"]
  student = key["students"]
  if level == "Algebra":
    print(student[1])

# Next, lets print each student from every course. To do so we can iterate through each course,
# then iterate through each student in the course, and finally print each name.

for key in math_classes:
  students = key["students"]
  for student in students:
    print(student)

# Lastly, let's use what we have learned to print the following statement for each iteration:
# "[Teacher] teaches [subject] to [student]".
# TIP: Setting variables will not only help in readability, but will also keep track of your
# TIP: program's functionality.

for key in math_classes:
  students = key["students"]
  teacher = key["teacher"]
  subject = key["subject"]   
  for student in students:
    print(f"{teacher} teaches {subject} to {student}.")

# TODO: Complete Section 3 of TODO 13 (7 min for students, 4 min for demo)
