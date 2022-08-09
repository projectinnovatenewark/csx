"""
Working with for loops in dictionaries and lists
"""

# TODO: Section 1.1:

grades = [60, 73, 80, 87]

# Loop through the list above and "curve" each grade by 3 points and print those
# curved grades.

# TODO: Section 1.2:

# In a new loop, print the statement "Student [num] got a [grade]." use the ".index()" method to
# find the student's position in the list.

# TIP: Make the print statement readable for an end user.

####################################################################################################

# TODO: Section 2:

# Use a "for loop" to print each character in the following string. Your print statement should
# read, "Current letter: [char]".

vroom = "racecar"

####################################################################################################

# TODO: Section 3:

# Loop through a range of numbers between 2 and 9. Within the "for loop", divide each number by 2
# and print the result.

####################################################################################################

# TODO: Section 4: 
# In the following dictionary, keys are associated with days of the week & values represent
# temperatures.

# TIP: 
# Dictionaries can be spread out over multiple line to avoing surpassing character limits, as seen
# below:

temperature_forecast = {
    "Sunday": 65,
    "Monday": 70,
    "Tuesday": 80,
    "Wednesday": 70,
    "Thursday": 67,
    "Friday": 95,
    "Saturday": 100
}

# Create a for loop that prints out each day of the week with its associated temperature in the
# format. "On [day] it will be [temperature] degrees outside."

for day in temperature_forecast:
  print(f"On {day} it will be {temperature_forecast[day]}")