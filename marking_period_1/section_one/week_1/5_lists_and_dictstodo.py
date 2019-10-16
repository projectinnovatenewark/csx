"""
Working with lists and dictionaries to convey a weather forecast
"""

# create a list with days from Monday through Sunday
DAYS_OF_WEEK = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# in the following dictionary, the keys are associated with days of the week while values represent temps
# the first value of 1 represents sunday's temperature all the way to 7 which represents Saturday
TEMPERATURE_FORECAST = {1: 65, 2: 70, 3: 80, 4: 70, 5: 67, 6: 95, 7: 100}

# print out Wednesday by accessing it through the list days of week, then print out wednesday's temperature
# by accessing the forecast dictionary

print(DAYS_OF_WEEK[3] + " is going to be roughly " + str(TEMPERATURE_FORECAST[4]) + " degrees.")
