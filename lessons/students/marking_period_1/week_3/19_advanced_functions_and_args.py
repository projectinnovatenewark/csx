"""
Learning more advanced functions and navigating loops through dictionaries
"""

# *args being set in a function's parameters allows additional arguments to be passed. They will
# turn into a tuple named after what you put following the asterisk. **kwargs being set in a function's
# parameters allows additional arguments to be passed as a key/value pair in a dictionary. The dict
# will be named after what you put following the two asterisks. Remember- the difference between
# *args and **kwargs parameters depends on the number of asterisks you place before the name.

# The "bread" and "meat" parameters are considered positional. They are considered positional
# because the order in which you pass the arguments matters. The first argument passed would assume
# the alias of "bread" and the second would assume the alias of "meat".
def set_sandwich(bread, meat):
    print(f"{bread} bread and {meat} meat")

# These two are considered positional arguments, since their position matters when calling the function.
set_sandwich("Wheat", "Turkey")

# The "ingredients" *args would take all non-positional arguments and create a tuple of them. Recall-
# a tuple is an immutable list (immutable = can't be changed). 
def make_sandwhich(bread, *ingredients):
    print(f"The bread is {bread}")
    print(ingredients)

make_sandwhich("Rye", "Turkey", "Swiss", "Lettuce", "Mayo")
make_sandwhich("Burnt", "Cheese")

#TODO: Section 1 of TODO 19
####################################################################################################

# When you add **kwargs as a parameter in a function, the name of your kwargs becomes a dictionary
# within that function.
def build_profile(f_name, l_name, **user_info):
    # Here we are adding key/value pairs to our "user_info" dictionary
    print(f"user info dict before adding first and last name as key value pairs: {user_info}")
    user_info["first_name"] = f_name
    user_info["last_name"] = l_name

    # This is the way you'll want to iterate through a dictionary moving forward.
    # The way we showed prior was to give a background understanding of dictionaries.
    for key, val in user_info.items():
        print(f"The key is: {key}, and the value is: {val}.")

    # User info is now a dictionary with all relevant values. Let's return that!
    return user_info

user_profile = build_profile("Marky", "Mark", sport = "basketball", residence = "South Orange")
print(user_profile)

#TODO: Section 2 of TODO 19
