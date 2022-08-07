"""
Indexing and Ranges
"""

# Range and Indexing go hand in hand because if you remember from our earlier reviews
# when you use index to access items in a list. Well, that index number has to be INSIDE the range
# of the list.

# For this review, we need to know a little bit about for loops:
# for loops iterate through an item that is passed to it. how it iterates depends on the item you pass it.
# for ranges, the variable you set will be equal to the number in the range, starting with the smallest number
# for lists, the variable will iterate through each item in the list, starting with the first item
# for dictionaries, the variable will represent each iterate through each key, starting with the first key

for num in range(5):
    print(num)
# When you print num here, you see that numbers 0 through 4 are printed.
# This goes along with the same concept of indexing
# In a list of 5 items - the first item's index would be 0
# And the last item's index would be 4

for num in range(5,13):
    print(num)

# Here you see that by printing num, you get 5 through 12
# This is because range is inclusive of the first number passed,
# but exclusive of the second number passed

###################################################################################################

# for loops and range can be useful in printing lists

temps_of_week = [72, 68, 67, 56, 70]
for temps in temps_of_week:
    print("On day", str(temps_of_week.index(temps)+1),"it was",temps,"degrees outside.")

# Lets breakdown this code
# We created the list temps_of_week
# Then we used temps to call on each value in a for loop
# Then we used the str() function to convert temps to a string and print an everyday statement.

###################################################################################################

# We can use the same concept as above in dictionaries too!
# Lets make our temperature list a little better

temps_of_week = {
    "Monday": 72,
    "Tuesday": 68,
    "Wednesday": 67,
    "Thursday": 56,
    "Friday": 70
}
# First lets remember how to find Friday's temperature

print("Friday's temperature is:",temps_of_week["Friday"],"degrees.")
# This is greatand all... but we want a smart way to print ALL of the days and their temps.

for day in temps_of_week:
    print("On", day, "it was", str(temps_of_week[day]),"degrees outside.")