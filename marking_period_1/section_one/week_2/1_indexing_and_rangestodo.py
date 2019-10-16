"""
Working with for loops in dictionaries and lists
"""

# in the following dictionary, the keys are associated with days of the week while values represent temps
TEMPERATURE_FORECAST = {"Sunday": 65, "Monday": 70, "Tuesday": 80, "Wednesday": 70, "Thursday": 67, "Friday": 95, "Saturday": 100}

# create a for loop that prints out each day of the week with the temperate=ure
for day in TEMPERATURE_FORECAST:
    print(day + " will be " + str(TEMPERATURE_FORECAST[day]) + " degrees.")
