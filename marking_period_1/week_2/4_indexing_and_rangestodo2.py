"""
Working with for loops in dictionaries and lists
"""

# in the following dictionary, keys are associated with days of the week & values represent temps
# notice how, when in one line, the characters surpass our self-imposed 100 character limit
# therefore, we can format our dictionary like such to stick to our format!

# here is a random forecast of what a week might look like with highs and lows set in a list
TEMPERATURE_FORECAST = {
    "Sunday": [65, 73],
    "Monday": [70, 78],
    "Tuesday": [80, 86],
    "Wednesday": [70, 90],
    "Thursday": [67, 73],
    "Friday": [95, 102],
    "Saturday": [85, 88]
}

print(TEMPERATURE_FORECAST["Friday"][1])

# TODO: create a for loop that prints out each day of the week with the high and low of each day

ADVANCED_FORECAST = {
    "Sunday": {"morning": [40, 55], "afternoon": [57, 64], "evening": [59, 43]},
    "Monday": {"morning": [38, 50], "afternoon": [52, 66], "evening": [54, 47]},
    "Tuesday": {"morning": [46, 65], "afternoon": [50, 58], "evening": [59, 39]},
    "Wednesday": {"morning": [30, 35], "afternoon": [35, 56], "evening": [48, 29]},
    "Thursday": {"morning": [32, 41], "afternoon": [48, 62], "evening": [60, 37]},
    "Friday": {"morning": [42, 50], "afternoon": [45, 52], "evening": [54, 35]},
    "Saturday": {"morning": [40, 43], "afternoon": [52, 64], "evening": [60, 37]},
}
