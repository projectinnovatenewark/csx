"""
Learn the elements of Object Oriented Programming
"""

# Here are the seven(some consider there to only be 4, but we're giving you seven)
# elements of object oriented programming!

##################################################################################################

# 1) Object
# The object is an entity that has state and behavior. It may be any real-world object
# like the mouse, keyboard, chair, table, pen, etc. Everything in Python is an object,
# and almost everything has attributes and methods. All functions also have a built-in attribute
# __doc__, which returns the doc string defined in the function source code.

# EXAMPLE:

# the format function we've used previously is built into Python. Therefore, it should have a
# docstring that we can log using the print function!
print(format.__doc__)

##################################################################################################

# 2) Class
# A Class is like an object constructor, or a "blueprint" for creating objects.

# The class can be defined as a collection of objects. It is a logical entity that
# has some specific attributes and methods. For example: if you have an employee class
# then it should contain an attribute and method, i.e. an email id, name, age, salary, etc.

# Here we will provide a more simple example than the Employee class.

# EXAMPLE:

class MyClass:
  """define some random class and assign it a prop"""
  randomProperty = 10

# lets instantiate an example of this class
instantiatedClass = MyClass()
print(instantiatedClass.randomProperty)

# since this object has a doc string, we can access it using the doc function like in our
# last example
print(instantiatedClass.__doc__)

##################################################################################################

# 3) Method
# The method is a function that is associated with an object. In Python, a method is not
# unique to class instances. Any object type can have methods.

class Doggo:

    # Class Attribute added to all instantiations of the Doggo class
    species = 'mammal'

    # initializer function
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a method of this class
    def description(self):
        return f"{self.name} is {self.age} years old"

    # another method of this class
    def speak(self, sound):
        return f"{self.name} says {sound}"

# Instantiate the Doggo object
pierreTheDog = Doggo("Pierre", 6)

# call our instance methods
print(pierreTheDog.description())
print(pierreTheDog.speak("Wuuf Wuuf"))

# EXAMPLE:

##################################################################################################

# 4) Inheritance
# Specifies that the child object acquires all the properties and behaviors of the
# parent object. By using inheritance, we can create a class which uses all the properties
# and behavior of another class. The new class is known as a derived class or child class,
# and the one whose properties are acquired is known as a base class or parent class.

# EXAMPLE:
# Here is a parent class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

# Use the Person class to create an object, and then execute the printname method:

x = Person("Janet", "Jackson")
x.printname()

# Lets create a child class that will inherit the properties of this parent
class Student(Person):
  pass

# and check to see if the child class inherited the properties of it's parent class, including
# the constructor and printname method
x = Student("Mariano", "Rivera")
x.printname()

# Note: When you add the __init__() function, the child class will no longer inherit the parent's
# __init__() function. That means the constructor will change and the values you pass to the class
# will behave in the way the child class wants it to.

# Lastly, we will tinker with inheritance and use a super() function. If we want to inherit
# the methods and properties from the parent, we add super() to the init of the child.
# since we added this, we now will not need to add these lines that originally appeared
# in the parent:
    # self.firstname = fname
    # self.lastname = lname
# So, instead of having to repeat this in our child's constructor, it assumes the init function
# from it's parent and automatically sets fname and lname to the variables of firstname and lastname.
class NewStudent(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

y = NewStudent("Lonzo", "Ball", 2017)
y.welcome()

##################################################################################################

# 5) Polymorphism
# The word polymorphism means having many forms. In programming, polymorphism means same
# function name (but different signatures) being used for different types.

# EXAMPLE:  
# len() being used for a string 
print(len("geeks")) 
  
# len() being used for a list 
print(len([10, 20, 30]))

##################################################################################################

# 6) Encapsulation
# Encapsulation is also an important aspect of object-oriented programming. It is used to restrict
# access to methods and variables. In encapsulation, code and data are wrapped together within a
# single unit from being modified by accident.
# Reference here: https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces

# EXAMPLE:
def encapsulation_example():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

encapsulation_example()
print("In global scope:", spam)

##################################################################################################

# 7) Data Abstraction
# Data abstraction and encapsulation both are often used as synonyms. Both are nearly synonym
# because data abstraction is achieved through encapsulation. Abstraction is used to hide internal
# details and show only functionalities. Abstracting something means to give names to things so that
# the name captures the core of what a function or a whole program does.

# Abstraction in general in programming refers to the ignoring of details that aren't essential
# to your point of focus. Encapsulation on the other hand is about combining related parts into
# a whole entity. The easiest way to describe encapsulation is in files- if your program requires
# many different files and moving parts to operate, you compartmentalize different functionalities
# into different files.

# A fantastically explained bit on abstraction here:
# https://www.cs.usfca.edu/~wolber/bookChapters/CS_Text_11.pdf

# EXAMPLE:
# Lets create a data abstraction for a 'facebook user'. While there is likely tens of thousands of data
# points tied to a social media account, we can create an abstraction of that by defining the data
# for a person. We can then use this abstraction to create single instances later in the program
# with a new example user.
class Person:
    def __init__(self): # this function called on creation
        self.firstName=""
        self.lastName=""
        self.id=""
        self.email=""
        self.friends=[]

p1 = Person() # object creation statement
p1.firstName = "Shaquille" # setting fields
p1.lastName = "O'Neal"
p1.id = "34"
p1.email = "drshaq@tnt.co"
print(p1.firstName) # accessing a field

# as is the nature of coding, let's do the above in a much simpler way that we began to learn
# in our classes lesson from a few classes ago (yep, that was intentional 😂)

class User:
    def __init__(self,first,last,id,email):
        self.firstName=first
        self.lastName=last
        self.id=id
        self.email=email
        self.friends=[]
# main
u1 = User("Kobe","Bryant","8","laker4life@mamba.co")
print(u1.firstName)

##################################################################################################

# Additional Note on Polymorphism with Inheritance:
# In Python, Polymorphism lets us define methods in the child class that have the same name as the
# methods in the parent class. In inheritance, the child class inherits the methods from the parent
# class. However, it is possible to modify a method in a child class that it has inherited from the
# parent class. This is particularly useful in cases where the method inherited from the parent
# class doesn’t quite fit the child class. In such cases, we re-implement the method in the child
# class. This process of re-implementing a method in the child class is known as Method Overriding.

class Bird: 
  def intro(self): 
    print("There are many types of birds.") 
      
  def flight(self): 
    print("Most of the birds can fly but some cannot.") 
    
# below you can see both the sparrow and ostrich classes overriding the flight method from Bird
class sparrow(Bird): 
  def flight(self): 
    print("Sparrows can fly.") 
      
class ostrich(Bird): 
  def flight(self): 
    print("Ostriches cannot fly.") 
      
obj_bird = Bird() 
obj_spr = sparrow() 
obj_ost = ostrich() 
  
obj_bird.intro() 
obj_bird.flight() 
  
obj_spr.intro() 
obj_spr.flight() 
  
obj_ost.intro() 
obj_ost.flight() 

##################################################################################################

# Additional Note on implementing Polymorphism with a Function:
# It is also possible to create a function that can take any object, allowing for polymorphism. In
# this example, let’s create a function called “func()” which will take an object which we will name
# “obj”. Though we are using the name ‘obj’, any instantiated object will be able to be called into
# this function. Next, lets give the function something to do that uses the ‘obj’ object we passed
# to it. In this case lets call the three methods, viz., capital(), language() and type(), each of
# which is defined in the two classes ‘India’ and ‘USA’. Next, let’s create instantiations of both
# the ‘India’ and ‘USA’ classes if we don’t have them already. With those, we can call their action
# using the same func() function:

class India(): 
    def capital(self): 
        print("New Delhi is the capital of India.") 
   
    def language(self): 
        print("Hindi the primary language of India.") 
   
    def type(self): 
        print("India is a developing country.") 
   
class USA(): 
    def capital(self): 
        print("Washington, D.C. is the capital of USA.") 
   
    def language(self): 
        print("English is the primary language of USA.") 
   
    def type(self): 
        print("USA is a developed country.") 
  
def func(obj): 
    obj.capital() 
    obj.language() 
    obj.type() 
   
obj_ind = India() 
obj_usa = USA() 
   
func(obj_ind) 
func(obj_usa) 