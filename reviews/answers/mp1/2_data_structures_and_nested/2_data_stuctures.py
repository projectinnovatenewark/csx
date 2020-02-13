"""
Data Structures TODO Answers
"""

#TODO: Create a dictionary of Gatorade colors and flavors named gatorade_flavors 
#TODO: using the following pairs:
#TODO: Red & Fruit Punch, Yellow & Lemon Lime, Purple & Grape, Blue & Cool Blue
# Hint: Each Color/Flavor combo is in order of Key: Value

gatorade_flavors = {
    "Red": "Fruit Punch",
    "Yellow": "Lemon Lime",
    "Purple": "Grape",
    "Blue": "Cool Blue"
}

#TODO: In a coherant statement; Print what flavor is associated with Yellow.

print("Yellow Gatorade is the flavor", gatorade_flavors["Yellow"])

#TODO: Add the color Orange which has the same name for its flavor to the dictionary

gatorade_flavors["Orange"] = "Orange"

#TODO: Print the new dictionary

print(gatorade_flavors)

#TODO: Check the list using the .get() method to see if there is a Green gatorade flavor.
#TODO: If there isn't a green flavor, return "Missing"

green_flavor = gatorade_flavors.get("Green", "Missing")
print("Green is", green_flavor)

#TODO: Create a food shopping list containing: 
#TODO: Milk, Eggs, Spinach, Asparagus, Chicken, Oreos.

shopping_list = [
    "Milk",
    "Eggs",
    "Spinach",
    "Asparagus",
    "Chicken",
    "Oreos"
]

print(shopping_list)

#TODO: Since we are trying to eat healthy, Remove Oreos from the shopping list

shopping_list.remove("Oreos")

# Add salmon via the append method
shopping_list.append("Salmon")

# Replace asparagus with broccolli using the  because its cheaper than asparagus
shopping_list[3] = "Broccoli"
print(shopping_list)

#TODO: Return the 4th item in the shopping list using its index

print("The fourth item in the list is", shopping_list[3])

#TODO: Use the .remove method to remove the last item in the list and print it in the format 
#TODO: '___ is now removed.'
#TODO: Then use the pop method to remove the 2nd item and print a new statement 
# '___ is now removed.'

print("We are removing", shopping_list.pop(1))
print("The new shopping list is", shopping_list)

