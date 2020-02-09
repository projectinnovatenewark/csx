"""
Here we will cover lists and dicts
"""

# lists are a grouping of values
CLASS_LIST = ["Andy", "Bronny", "Carlos", "Denisa", "Enrique"]

##############################################################################################

# dictionaries are similar, except they have keys which in turn have values
# similarly to how a dictionary has words with definitions, the keys represent
# the words and values represent the definitions.
GRADES_DICT = {"Andy": 87, "Bronny": 95, "Carlos": 75, "Denisa": 55, "Enrique": 100}

##############################################################################################

# below is an example of indexing. the first item in any list has an index of ZERO
# and the next item is 1, followed by 2, etc.

# Note: Accessing values from something with square brackets [] in Python is called
# bracket notation. In the next lesson, lesson 2, you will see "dot notation".
print("The first student in the class class list is " + CLASS_LIST[0])

# in dictionaries, however, values can only be accessed by their key. The format to finding
# a key's value is `dictionary[key]`

print("Bronny's grade: " + str(GRADES_DICT["Bronny"]))

print("Denisa's grade: " + str(GRADES_DICT["Denisa"]))

# hm. so, the first student in class can be found using CLASS_LIST[0] . We can set that equal
# to a variable like this.

first_student = CLASS_LIST[0]

# now, since this student has a grade in the grades list, let's use this variable to find the
# value of their grade in the list!

first_student_grade = GRADES_DICT[first_student]

# lets print this out together in a readable way. Tip- when you combine strings with commas,
# a space is placed between the strings. However, when you use a `+` , there are no spaces added
print(first_student + "'s grade was", first_student_grade)

##############################################################################################

# tuples are lists that cannot have their values modified and they are denoted with parentheses
months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

# what about 'nested' data types? a list can be made up of dictionaries. Values in dictionaries
# can be lists. How would we handle that? Lets look at this data here. You can see that each item in the list
# is a dictionary that represents a class
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

# crazy data! how would we find the math teacher's level, the first student listed in her class, and her education?
# lets go through that here. since the dictionary with 'math' is the first ITEM in the LIST of classes.
math = classes[0]
print('math: ', math)
# here is how to find the math classes' level- by using either the math variable above OR the classes list directly
math_level = math['level']
math_level2 = classes[0]['level']
print('math level: ', math_level, 'should equal this', math_level2)

# we will do the same for the first student
math_first_student = math['students'][0]
math_first_student_again = classes[0]['students'][0]
print('math first student: ', math_first_student, 'should equal this', math_first_student_again)

# lastly, lets find the teacher's education level
math_teacher_education = math['teacher_description']['education']
math_teacher_education_again = classes[0]['teacher_description']['education']
print('math teacher education: ', math_teacher_education, 'should equal this', math_teacher_education_again)
