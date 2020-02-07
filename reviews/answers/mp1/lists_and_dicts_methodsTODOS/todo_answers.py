"""
Answers for Lists & Dictionary Methods Todo
"""

#TODO: Create a dictionary of Gatorade colors and flavors named gatorade_flavors 
#TODO: using the following pairs:
#TODO: Red & Fruit Punch, Yellow & Lemon Lime, Purple & Grape, Blue & Cool Blue
# Hint: Each Color/Flavor combo is in order of Key: Value}
gatorade_flavors = {
    "Red": "Fruit Punch",
    "Yellow": "Lemon Lime",
    "Purple": "Grape",
    "Blue": "Cool Blue"
}

#TODO: In a coherant statement; Print what flavor is associated with Yellow.
print("The yellow colored gatorade is", gatorade_flavors["Yellow"] + "."
)
#TODO: Add the color and flavor combo, Orange and Orange, to the dictionary
#TODO: Print the new dictionary
gatorade_flavors["Orange"] = "Orange"
print(gatorade_flavors)

#TODO: Check the list to see if there is a Green gatorade flavor.
#TODO: If there isn't a green flavor, return "Missing"
green_flavor = gatorade_flavors.get("Green", "Missing")
print(green_flavor)

#TODO: Create a food shopping list containing: 
#TODO: milk, eggs, spinach, asparagus, chicken, oreos.
groceries = [
    "milk",
    "eggs",
    "spinach",
    "asparagus",
    "chicken",
    "oreos"
]

#TODO: Since we are trying to eat healthy, Remove oreos from the shopping list.
groceries.remove("oreos")
print(groceries)

#TODO: Then add: salmon, green beans, and rice and print the new list.
groceries.append("salmon") 
groceries.append("green beans")
groceries.append("rice")
print(groceries)

#TODO: Return the 4th item in the shopping list using its index.
fourth_item = groceries[3]
print(fourth_item)

#TODO: Remove the last item in the list and return it in a coherent sentence.
last_item = groceries.pop()
print("We already have rice at home, so let's remove", last_item, "from the shopping list.")

#TODO: Then print the new list.
print(groceries)