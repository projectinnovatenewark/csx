"""
Here we will cover lists and dicts
"""

# A 'list' is a grouping of values that are ordered and changeable.
# In Python lists are written with square brackets, as shown below:
CLASS_LIST = ["Andy", "Bronny", "Carlos", "Denisa", "Enrique"]

# An index refers to a position within an ordered list. 
# For the following list, the indexes break down like this:
CLASS_LIST = ["Andy", "Bronny", "Carlos", "Denisa", "Enrique"]
#               0        1         2          3         4 
# As you can see, the first item in any list has an index of ZERO
# and the next item is 1, followed by 2, etc.. 

# In addition, Python supports negative indexes, in which case it counts from the end. 
# So the last character can be indexed with -1, the second to last with -2, etc.:
CLASS_LIST = ["Andy", "Bronny", "Carlos", "Denisa", "Enrique"]
#               -5       -4        -3        -2        -1 

# You can access single elements from a list using the name followed by a number in [], like so:
print(CLASS_LIST[0]) # first element

#You can also save a single element from the list as variable, like so:
second = CLASS_LIST[1] # second element
print(second)

# To add an item to a list, you use the append function as such:
CLASS_LIST.append("Susan")
print(CLASS_LIST)

# The append function adds an item to the end of the list. For this reason, the index value of 
# "Susan" in the example above will be both '5' and '-1'. You can check this with the following code:
print(CLASS_LIST[5])
print(CLASS_LIST[-1])

#TODO: Section 1 of TODO 2.1
####################################################################################################

# Dictionaries have keys which in turn have values similarly to how a real life dictionary
# has words with definitions, the keys represent the words and values represent the definitions.
GRADES_DICT = {"Andy": 87, "Bronny": 95, "Carlos": 75, "Denisa": 55, "Enrique": 100}

# In dictionaries, however, values can only be accessed by their key. The format to finding
# a key's value is `dictionary[key]`
print("Bronny's grade: ", GRADES_DICT["Bronny"])
print("Denisa's grade: ", GRADES_DICT["Denisa"])

# To add a key/value pair to a dictionary, you simply place a new key in brackets and set
# it equal to the desired value
GRADES_DICT["Susan"] = 92
print(GRADES_DICT)

#TODO: Section 2 of TODO 2.1
####################################################################################################

# Lets think more about how variable assignments can play in here.
CLASS_LIST = ["Aaron", "Bello", "Carla", "Droov", "Ebron"]
GRADES_DICT = {"Aaron": 87, "Bello": 95, "Carla": 75, "Droov": 55, "Ebron": 100}

# Hmm. so, the first student in class can be found using CLASS_LIST[0]. We can set that equal
# to a variable like this.
first_student = CLASS_LIST[0] # this will equal "Aaron"

# Now, since this student has a grade in the grades list, let's use this variable to find the
# value of their grade in the list!
first_student_grade = GRADES_DICT[first_student] # this is the equivalent of GRADES_DICT["Aaron"]

# Lets print this out together in a readable way. Reminder- when you combine strings with commas,
# a space is placed between the strings. However, when you use a `+` , there are no spaces added
print(first_student + "'s grade was", first_student_grade)

####################################################################################################

# Tuples are lists that cannot have their values modified and they are denoted with parentheses
months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

# FIXME: Uncomment the code below if you want to show the error that would run
# Here is an example of trying to change a tuple's value. It will throw you an error.
# months[0] = "June" # Will output "TypeError: 'tuple' object does not support item assignment"

####################################################################################################

# What about 'nested' data types? What if a list's items are all dictionaries? What if values in dictionaries
# are lists? How would we handle that?

# Lets look at this data here. You can see that each item in the list
# is a dictionary that represents a class.
classes = [
    {
        'subject': 'math',
        'level': 'linear algebra',
        'students': ['billy', 'beatrice', 'bronny', 'bart'],
        'teacher_description': {
            'name': 'Betty',
            'education': ['Masters of Math', 'Bachelors of Science']
        },
        'classTime': ['11:00 AM', '12:30 PM']
    },
    {
        'subject': 'english',
        'level': 'composition',
        'students': ['chris', 'callie', 'crysta', 'calista'],
        'teacher_description': {
            'name': 'Joanny',
            'education': ['PHD of English', 'Masters of Literacy', 'Bachelors of Biology']
        },
        'classTime': ['1:00 PM', '2:45 PM']
    }
]

# Crazy data! How would we find the math teacher's level, the first student listed in her class, and her education?
# Lets go through that here. Since the dictionary with 'math' is the first ITEM in the LIST of classes, lets
# set a variable math equal to the first item in the classes list.
math = classes[0]
print('math: ', math)

# Here is how to find the math classes' level- by using either the math variable above OR the classes list directly
math_level = math['level']
math_level2 = classes[0]['level']
print('math level: ', math_level, 'should equal this', math_level2)

# We will do the same for the first student
math_first_student = math['students'][0]
math_first_student_again = classes[0]['students'][0]
print('math first student: ', math_first_student, 'should equal this', math_first_student_again)

# Lastly, lets find the teacher's education level
math_teacher_education = math['teacher_description']['education']
math_teacher_education_again = classes[0]['teacher_description']['education']
print('math teacher education: ', math_teacher_education, 'should equal this', math_teacher_education_again)
