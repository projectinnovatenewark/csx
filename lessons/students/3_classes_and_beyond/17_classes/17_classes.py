"""
Understanding classes and scope within a class
"""
# TITLE: Section 1.1 - Constructing Classes

# As we have covered previously, Python is an object oriented programming (OOP) language. Therefore,
# almost everything in Python is an object. An object consists of various data and the methods that
# perform operations on those data. To create user-defined objects in Python, we can use an object
# constructor known as a "class".

# Both objects and classes are comprised of attributes and methods. There are two types of
# attributes; class attributes and instance attributes. Class attributes are shared by all
# instances of a class while instance attributes are specific to a given instance of a class.
# Methods are functions defined within the scope of and bound to classes.

# The syntax for constructing a custom class is "class ClassName:". Below is an example of creating
# a class called "TenClass".

class TenClass: # Define class names starting with a capital letter and use CamelCase as a best
                # practice.
  x = 10 # This is a class attribute because all instances of "TenClass" will have the value x be
         # equal to 10.

  def x_plus_five(self): # This is a method. Methods always take at least one parameter of self to
                         # access the instance of the object it is called on.
    print(f"x_plus_five Called{self.x + 5}") # We use "self" to print a given instance's value of
                                             # x + 5.

# Just as other means of storing values in variables, we can instantiate an instance of the "TenClass"
# class and store it in a variable.

instance1 = TenClass()
instance2 = TenClass()

# You can access class methods and attributes by using dot (.) notation. Below is an example of
# manually printing each instance's "x" attribute. Since "x" is a class attribute, it will have the
# same value for each instance of "TenClass".
print(f"instance1: {instance1.x}")
print(f"instance2: {instance2.x}")

# Below is an example of using dot notation to call the "x_plus_five()" method.
# IMPORTANT: The instance object is read as the first argument of "self" in the method call, so it
# IMPORTANT: is not necessary to add an argument for "self".

instance1.x_plus_five()
instance2.x_plus_five()

####################################################################################################

# TITLE: Section 1.2 - The __init__ Function

# The "__init__()" function is a special Python function that is called automatically by an object
# creation statement. In OOP, the "__init__()" function is known as a constructor, as its job is to
# build (construct) an object of the type specified by the class. Below we are defining the class
# "Cat" and want to give it instance attributes of "name" and "color". Remeber that instance
# attributes are defined in each individual class instantiation.

class Cat:
  animal_type = 'feline' # This is a class attribute that will be shared by all instances of "Cat".

  def __init__(self, name, color): # Our constructor takes 3 parameters: "self" (the instance of
                                   # the class), name, and color.
    # Using the syntax "self.var", where "var" is a given parameter, we can set attributes of a
    # given instantiation of a class during its creation.
    self.name = name
    self.color = color

# Below we are intantiating a class of "Cat" and setting the "name" attribute to "Simba" and the
# "color" attribute to "orange".
simba = Cat("Simba", "orange")
grumpy = Cat("Grumpy Cat", "brown and white")

# Again, we can use dot notation to access the attributes of "simba" and "grumpy".
print(f"{simba.name} is a(n) {simba.color} {simba.animal_type}.")
print(f"{grumpy.name} is a(n) {grumpy.color} {grumpy.animal_type}.")

# TODO: Section 1 of TODO 17 (8 min for students, 4 min for demo)

####################################################################################################

# TITLE: Section 2 - Using methods to mutate attributes

# In Python, we can use class methods to change the value of an instance's attribute. Below we are
# defining a class called 'Dog' that will have a class attribute of "animal_type" equal to "canine",
# as well as 3 instance attributes: "name", "color", and "tricks". The attribute "tricks" will be a
# list of tricks where each element is a different trick. To add tricks to the "tricks" attribute,
# we will call the "add_trick()" method.

class Dog:

  animal_type = 'canine' # This is a class attribute.

  def __init__(self, name, color):
    self.name = name
    self.color = color
    self.tricks = []  # Creates a new empty list for each Dog.

  def add_trick(self, trick):
    self.tricks.append(trick) # We pass "trick" as a parameter and append it to the "tricks" list.

dog_1 = Dog("Fido", "brown")
dog_1.add_trick("sit")
dog_1.add_trick("roll over")

dog_2 = Dog("Bella", "black")
dog_2.add_trick("shake")

# Now that tricks are added for each instantiation of the Dog class, we can print each associated
# list.
print(f"{dog_1.name}'s list of tricks: {dog_1.tricks}")
print(f"{dog_2.name}'s list of tricks: {dog_2.tricks}")

# TODO: Section 2 of TODO 17 (7 min for students, 4 min for demo)

####################################################################################################

# TITLE: Section 3 - Inheritance

# Inheritance is a powerful feature in object oriented programming that refers to defining a new
# class that inherits all methods and properties from another class. The original class is referred
# to as the parent class, or base class, while the new class is referred to as a child class, or
# derived class.

# Below we have a parent class of Person. We will use this class to create a child class called
# "Student".
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def identifier(self):
        print(f"My name is {self.first_name} {self.last_name}.")

# Below the "Student" class is defined. The "Student" class will be instantiated to include both
# instance attributes as well as the method defined in "Person".

class Student(Person): # To inherit funcitonality of the "Person" class, we pass it as a parameter.
    def __init__(self, first_name, last_name, grad_year):

        # The "super()" function is a built-in Python function that allows programmers to access the
        # functionality of a parent class without naming it explicitely.
        super().__init__(first_name, last_name) # The "super()" function is used to inherit the
                                       # attributes defined in the "Person" class.
                                                
        self.grad_year = grad_year # The attribute "grad_year" is specific to the "Student" class.
                                   #  This attribute would not be accessible by the "Person" class.

    def print_grad_year(self):
        print(f"{self.first_name} {self.last_name} will graduate in {self.grad_year}.")

student_1 = Student("Joey", "Walnut", 2023) # This is an instantion of the child class, "Student".

# Methods from either the parent class or child class can be called on instantiations of the child
# class.
student_1.identifier() # This was defined in the parent class.
student_1.print_grad_year() # This was defined in the child class.

# TODO: Section 3 of TODO 17 (10 min for students, 6 min for demo)
