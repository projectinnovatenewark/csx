"""
A quick review of scope
"""

# the 'global' declares that the variable which comes after it is in reference
# to the global variable. global variables exist within the whole file,
# whereas local variables are limited to the scope of a function

def f():
    global s
    print(s)
    s = "I'm from the North Ward"
    print(s)

# since the function f() is called after the variable s is declared, then
# there wont be an error thrown
s = "My parents are from there!" 
f()
print(s)