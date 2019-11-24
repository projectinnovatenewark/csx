"""
Understanding classes and scope within a class
"""

# The variable Cat could have been named anything. The "Cat()" says to
# create a new object and to run the strangely named function __init__ (two
# underscores before and after 'init').
# __init__ is special Python function that it is called automatically on an object
# creation statement. The computer science term for it is constructor, as its
# job is to build an object of the type specified by the class.
# The 'self' parameter in __init__ just refers to the instance being created, in
# this case Cat. __init__ creates the object, putting in default values for all the
# fields, then returns the object into the variable Cat. The main program then
# goes on to set the various fields of the Cat object, and then access and print
# one of them. Note that the fields of an object can be set/accessed with a
# reference of the form:
# object.field

# As shown below, we also pass an inital value into the object Cat(). We then set
# the input to "name" inside the init constructor and set the Cat's name value
# to the input it receives

class Cat:

    kind = 'feline'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

d = Cat('Fido')
e = Cat('Bella')
print("d.kind", d.kind)                  # shared by all Cats
print("e.kind", e.kind)                  # shared by all Cats
print("d.name", d.name)                  # unique to d
print("e.name", e.name)                  # unique to e

##################################################################################################

class Cat:

    tricks = []  # mistaken use of a class variable shared by all Cats due to scope

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Cat('Fido')
e = Cat('Bella')
d.add_trick('hit yarn')
e.add_trick('attack bird')
d.tricks  # unexpectedly shared by all dogs

##################################################################################################

class Cat:

    def __init__(self, name):
        self.name = name
        self.tricks = []  # creates a new empty list for each Cat

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Cat('Fido')
e = Cat('Bella')
d.add_trick('hit yarn')
e.add_trick('attak bird')
d.tricks
e.tricks
