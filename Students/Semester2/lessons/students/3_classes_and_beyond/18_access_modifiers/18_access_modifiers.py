"""
Taking a more in depth look at classes
"""

# TITLE: Section 1 - Encapsulation and Access Modifiers

# In object orientated programming, access modifiers are used to modify the default scope of
# attributes and methods of a class. The purpose of access modifiers is to implement encapsulation.
# Encapsulation refers to the wrapping of code and data together into a single unit. Doing so
# restricts the access of certain variables and methods. Encapsulation can be thought of as a
# protective shield that prevents data from being accessed by the code outside of this shield.

# Access modifiers are identified by the use of the underscore (_) symbol. There are 3 types of
# access modifiers in Python: public, protected, and private. In the following sections, we will
# look over each type listed.

####################################################################################################

# TITLE: Section 2 - Public Access Modifiers

# By default, all the attributes and methods of a class are public. The members declared as "public"
# are accessible from outside a class through an instantiation/object of the class. Attributes and
# methods that have public access do not use an underscore. As an example, below we define the class
# "Pet".

# TODO: Hey Teacher, have the students walk you through this example to reinforce what we already
# TODO: know about classes.

class Pet: # This class will look familiar to examples from the previous classes lesson.

  def __init__(self, animal_type, num_legs, food):
    self.animal_type = animal_type # This is a public attribute.
    self.num_legs = num_legs # This is also a public attribute.
    self.food = food # This is another public attribute.

  def printer(self): # This is a public method.
    print(f"The pet {self.animal_type} has {self.num_legs} legs and eats {self.food}.")

class Dog(Pet): # This is a child class derived from "Pet".
  def __init__(self, animal_type, num_legs, food, dog_type):
    super().__init__(animal_type, num_legs, food)
    self.dog_type = dog_type

doggy = Dog("dog", "3", "spaghetti", "pitbull")
pet = Pet("dog", "3", "spaghetti")
pet.printer()
doggy.printer()

####################################################################################################

# TITLE: Section 3 - Protected Access Modifiers

# Protected access modifiers are used on attributes and methods to restrict their access to the
# class they are defined in or a child class derived from that class. Protected access modifiers are
# indicated with a single underscore (_) in its definition. Below we are redefining the "Pet" and
# "Dog" classes to demonstrate this concept.

class Pet:

  def __init__(self, animal_type, num_legs, food):
    # IMPORTANT: Take note of the underscore in the definition of "self._animal_type". This
    # IMPORTANT: defines "animal_type" as a protected instance attribute.
    self._animal_type = animal_type # This instance attribute is "protected". It will now only be
                                    # accessible within the "Pet" class or a class derived from it.
    self.num_legs = num_legs
    self.food = food

  def printer(self):
    # The underscore is also inlcuded when referencing protected variables.
    print(f"The pet {self._animal_type} has {self.num_legs} legs and eats {self.food}.")

class Dog(Pet):
  def __init__(self, animal_type, num_legs, food, dog_type):
    super().__init__(animal_type, num_legs, food)
    self.dog_type = dog_type
    self.tricks = []

  # Methods can also be defined using a protected access modifier through the use of a leading
  # underscore (_).
  def _add_trick(self, trick):
    self.tricks.append(trick)
    print(f"Current tricks: {self.tricks}")

  def dog_printer(self):
    # We can reference the protected variable, "_animal_type", here because "Dog" is a child class
    # derived from "Pet".
    print(f"A {self.dog_type} is a {self._animal_type} that eats {self.food}.")

doggy = Dog("dog", "3", "spaghetti", "pitbull")
# The protected variable 'animal_type', which is equal to 'dog', will print when the "printer()"
# method is called.
doggy.printer()
doggy.dog_printer()
print("Calling a protected method.")
doggy._add_trick("roll over")
print("Calling a protected method a second time.")
doggy._add_trick("stay")

# TIP: #1
# The only difference between a public and private attribute/method is that a protected
# attribute/method cannot be referenced outside of its package. A Python package is a collection of
# Python modules, or files ending with the extension ".py", within the same directory. You will
# learn more about Python packages and modules in a future lesson.

####################################################################################################

# TITLE: Section 4 - Private Access Modifiers

# Private access modifiers are indicated with a double underscore (__) in its definition. Private
# access modifiers are used on attributes and methods to restrict their access to only the class
# they are defined in. Below we are redefining the "Pet" and "Dog" classes to demonstrate this
# concept.

class Pet:
  # Notice we are instantiating new objects with keyword parameters now. This is because we will use
  # a private method to store instance attribute values and then a public method to print them.
  def __init__(self, animal_type=None, num_legs=None, food=None):
    self.animal_type = animal_type
    self.num_legs = num_legs
    self.food = food

  def __set_attributes(self): # This is a method to set all instance attributes. Please note the use
                              # of 2 underscores (__) which defines the "set_attributes()" method as
                              # a private method.
    self.animal_type = input("What is your animal? ")
    self.num_legs = input("How many legs does it have? ")
    self.food = input("What does it eat? ")

  def printer(self):
    self.__set_attributes() # We call the private method, "__set_attributes()" within the public
                            # method to access its functionality without exposing it.
    print(f"animal_type: {self.animal_type}\nnum_legs: {self.num_legs}\nfood: {self.food}")

class Dog(Pet):
  def __init__(self, animal_type=None, num_legs=None, food=None, dog_type=None):
    super().__init__(animal_type, num_legs, food)
    self.dog_type = dog_type

  def dog_printer(self):
    __set_attributes() # This will cause an error when "dog_printer()" is called.
    print(f"A {self.dog_type} is a {self.animal_type} that eats {self.food}.")

new_pet = Pet()
new_pet.printer()

# The below code will return an error because "__set_attributes()" is defined in the parent class.
# As we learned in this section, private methods can not be referenced or called outside of the
# class it is defined in.
new_dog = Dog()
new_dog.dog_printer()

# TODO: Section 3 of TODO 17 (X min for students, Y min for demo)
