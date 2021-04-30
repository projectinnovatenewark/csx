"""
Use employees.txt to perform operations on a list of employees
"""

# SETUP STEPS:
# 1) Go to https://github.com/projectinnovatenewark/csx/tree/master/lessons/students/2_functions_and_conditions/15_file_handling
# 2) Copy contents of the file employees.txt
# 3) Create a new file in your directory that contains the todo for the file handling lesson
# 4) Paste in the contents to your newly created employees.txt file
# 5) Save the file
# 6) Write your Python code
# 7) Change directories into your directory with the Python program
# 8) Run the program with this command in your terminal, `python3 program_name.py`

# IMPORTANT:
# Make sure your terminal is using the same working directory is in the same working directory as
# "employees.txt". Also, the spacing in "employees.txt" may look off, but it will not impact your
# ability to complete the todos.

# TODO: Section 1.1

# Use the "open" function to read the contents of "employees.txt" and print them to the terminal
# using the ".read()" method. Then close the file.

# TODO: Section 1.2

# Reopen "employees.txt". Then read each line in the file seperately using the ".readlines()" method
# and print them out to the terminal. Lastly close the file.

####################################################################################################

# TODO: Section 2

# Open "employees.txt". Then write to the file without overwriting its contents and add a new 
# employee. The format of the employee information should be:
# "John (tab) Smith (tab) Public Relations (tab) 50000". Then open the file again to read its
# contents and print them to the terminal. Lastly close the file.
fh = open("employees.txt", "a")
message = "\nJohn\tSmith\tPublic Relations\t50,000"
fh.write(message)

fh = open("employees.txt", "r")
print(fh.read())
fh.close()

# HINT: Use "\t" in strings to create a tab.
