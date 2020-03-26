"""
TODO for the Indexing and Range Review Lesson
"""

#TODO: Use a for loop and range to print the numbers 0-10
for num in range(11):
    print(num)

# TODO: Use List Comprehension to add even numbers from range(11) to a list named even_num

even_num = [num for num in range(11) if num % 2 == 0]
print(even_num)

# TODO: Using the .split method create a list off of the variable useless_string named lunch_drinks
# TODO: Then print the new list to make sure it worked!

useless_string = "Gatorade,Water,Soda,Redbull,iced tea"

lunch_drinks = useless_string.split(",")
print(lunch_drinks)

# TODO: Using the new lunch_drinks list; use a for loop to print each item in this format:
# "Today I drank ____ at lunch."

for drinks in lunch_drinks:
    print("Today I drank", drinks, "at lunch.")

#TODO: Using the following dict; print the following statement for each value using a for loop:
# "On _____ I drank ____ at lunch."

lunch_drinks = {
    "Monday": "Gatorade",
    "Tuesday": "Water",
    "Wednesday": "Soda",
    "Thursday": "Redbull",
    "Friday": "iced tea"
}

for day in lunch_drinks:
    print("On", day, "I drank", lunch_drinks[day], "at lunch.")

# TODO: BONUS: Recall earlier lessons and at the key: value pairs
# TODO: "Saturday": "coffee" and "Sunday": "Powerade"
# TODO: Then reprint the statement from above.

lunch_drinks["Saturday"] = "coffee"
lunch_drinks["Sunday"] = "Powerade"
for day in lunch_drinks:
    print("On", day, "I drank", lunch_drinks[day], "at lunch.")