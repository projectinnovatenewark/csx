"""
Introduction to conditionals and covering while loops.
"""

# TITLE: Section 1 Intro to Conditionals

# In programming, conditional statements are used to perform different actions depending on whether
# a specific boolean constraint evaluates to true or false. An "if statement" is a common
# conditional statement. The syntax for an "if statement" is, "if (some_condition):" where
# "some_condition" is the condition to be evaluated.

rectangle_area = 100
if rectangle_area > 50: # if "rectangle_area" is > 50, the print statement will run.
  print("This is a large rectangle")

# Another type of conditional statement is an "else statement". An "else statement" will only
# run if a paired "if statement" is false.

rectangle_area = 43
if rectangle_area > 50:
  print("This is a large rectangle.")
else:
  print("This is a small rectangle.")

# TODO: Section 1 of TODO 10 (3 minutes for students, 2 minutes for demo)

####################################################################################################

# TITLE: Section 2 - While loops

# In the previous lesson we learned how to iterate over an object using a for loop. Another type of
# loop in Python a "while loop", which is used to iterate over a block of code until a given condtion
# is no longer true. The syntax of a "while loop" is "while something_is_true:", where
# "something_is_true" acts as the condition. Below is a simple example of this concept:

num = 0
while num < 10: # This condition will continue to run as long as "num" is less than 10.
  print(num)
  num += 1 # This will increment "num" by 1 in every iteration.

# Since a while loop breaks when a condition is no longer true, all false values would cause the
# loop to terminate. In the loop below, "num" will decrement in each iteration until reaching 0.
# When num is equal to 0, the loop terminates because 0 is evaluated as a false value. This concept
# holds true for all data types. For example, a list or dictionary would return a false value if
# they are empty.

num = 10
while num:
  print(num)
  num -= 1

# The following "while loop" will continue to run until all the items have been removed by the
# .pop() method and "grocery_list" is empty.
grocery_list = ["Bread", "Butter", "Frozen Pizza", "Mozz Sticks", "Ice Cream"]
while grocery_list:
  purchased_item = grocery_list.pop()
  print(f"You purchased {purchased_item} and removed it from your list.")
  print(f"Your remaining items are: {grocery_list}")

# TODO: Section 2 of TODO 10 (15 minutes for students, 8 minutes for demo)
