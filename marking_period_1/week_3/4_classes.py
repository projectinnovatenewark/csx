"""
Understanding classes and scope within a class
"""

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

# class Cat:

#     tricks = []  # mistaken use of a class variable shared by all Cats due to scope

#     def __init__(self, name):
#         self.name = name

#     def add_trick(self, trick):
#         self.tricks.append(trick)

# d = Cat('Fido')
# e = Cat('Bella')
# d.add_trick('hit yarn')
# e.add_trick('attack bird')
# d.tricks  # unexpectedly shared by all dogs

# class Cat:

#     def __init__(self, name):
#         self.name = name
#         self.tricks = []  # creates a new empty list for each Cat

#     def add_trick(self, trick):
#         self.tricks.append(trick)

# d = Cat('Fido')
# e = Cat('Bella')
# d.add_trick('hit yarn')
# e.add_trick('attak bird')
# d.tricks
# e.tricks
