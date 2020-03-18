"""
Creating classes for your classmates
"""

# TODO: Create a class for an Employee, and include basic data
# TODO: like hours worked, salary, first name, last name, age, and title
class Employee:
    def __init__(self, hw, sal, fn, ln, a, t):
        self.hw = hw
        self.sal = sal
        self.fn = fn
        self.ln = ln
        self.a = a
        self.t = t

    def formatter(self):
        stringy = [
        "----------",
        # the f before each string allows for f-string literals
        # these allow for the format() function to be used, and for
        # curly braces to be used for replacement fields. link for reference:
        # https://docs.python.org/3/whatsnew/3.6.html#whatsnew36-pep498
        f"First Name : {self.fn}",
        f"Last Name : {self.ln}",
        f"Age : {self.a}",
        f"Title : {self.t}",
        f"Hours : {self.hw}",
        f"Salay : {self.sal}"
        ]
        return print("\n".join(stringy))

e1= Employee("50", "85000", "Jim", "Doe", "26", "Manager")
e2 = Employee("40", "70000", "Marcus", "Black", "18", "Subordinate")
e1.formatter()
e2.formatter()
# TODO: Create a function inside the class and print out a formatted
# TODO: set of strings explaining the details from the employee. Use the f shorthand
# TODO: for formatting that was used in the previous example.

# TODO: Then, call that function to print out those strings with a class
# TODO: of Employee set equal to a variable employeeOne
