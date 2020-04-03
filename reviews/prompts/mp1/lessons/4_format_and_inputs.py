"""
Review lesson for format() and inputs
"""

#  format() is a powerful tool that can be used to format strings and numbers
# Say we wanted to print the statement, "Today I ate a turkey sandwhich for lunch."
# We can print the following:

print("Today I ate a turkey sandwhich for lunch.")

# format() can be used as follows:

print("Today I ate a {} for lunch.".format("turkey sandwhich"))

# You can see be using the {}, we can get the same print statement!
# Lets use a variable to say what we ate now

meal = "turkey sandwhich"

print("Today I ate a {} for lunch.".format(meal))
# Again it's the same!!
# You can use multiple {} with format() also. Watch!

print("Today I ate a {} for {}.".format(meal, "lunch"))

# Now lets see how we can set a sentance to a variable and use format()

lunch_print = "Today I ate a {} for {}."

time_of_meal = "lunch"

print(lunch_print.format(meal, time_of_meal))
# You cans see now how this can start to become useful

# Now lets use format() to manipulate numbers

var1 = 4
print(var1)

print("{:.2f}".format(var1))

# After printing var1 with format(), you can see we added 2 decimal points with the "{:.2f}"
# you can add places in front of the first number as well

print("{:010.3f}, {:.2f}".format(var1, var1))

###################################################################################################

# input allows a user to enter information to be used later

q1 = input("What is your first name? ")
print(q1)

# Allowing for user inputs allows your code to be much more dynamic!
# Lets see how this can be effective with a simple while loop

x = int(input("Pick a number between 1 and 50: "))

while x > 0:
    if(x > 0):
        x -= 1
        print(int(x))
    