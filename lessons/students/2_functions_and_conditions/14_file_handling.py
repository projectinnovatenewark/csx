"""
Handling files via read, write, and open
"""

# FIXME: IMPORTANT! YOUR WORKING DIRECTORY OF YOUR TERMINAL MUST BE IN THE
# FIXME: "2_functions_and_conditions" FOLDER FOR THE PROGRAM TO RUN. IT WILL NOT
# FIXME: RECOGNIZE THE HELLO.TXT FILE UNTIL YOUR WORKING DIRECTORY IS WITHIN WEEK_3.

# to open a text file, use
fh = open("hello.txt", "r")

####################################################################################################

# create a new file in this directory called "my_name_is.txt" and place your first name on the first
# line followed by your last name on the second line.
# to read a text file, use
fh = open("my_name_is.txt", "r")
contents = fh.read()
print("Contents .read() function: \n", contents, "\n")

# TODO: Section 1 of TODO 14
####################################################################################################

# to read one line at a time, use
fh = open("my_name_is.txt", "r")
contents = fh.readline()
print("Contents .readline() function: \n", contents, "\n")

####################################################################################################

# to separate each line into items in a list, use the .readlines() function.
fh = open("my_name_is.txt", "r")
contents = fh.readlines()
print("Contents .readlines() function: \n", contents, "\n")

# if you want to iterate through the list, do it as such
print("Below is iterating through each line in contents")
for line in contents:
    print(line)

print("\n")

# TODO: Section 2 of TODO 14
####################################################################################################

# to write to a file, use
fh = open("hello.txt", "w")
fh.write("Hello World")
fh.close()

####################################################################################################

# to write to a file, use
fh = open("hello.txt", "w")
lines_of_text = ["a line of text \n", "another line of text \n", "a third line \n"]
fh.writelines(lines_of_text)
fh.close()

####################################################################################################

# to append to file, use:
fh = open("hello.txt", "a")
message = "Hello world, again"
fh.write(message)
fh.close()

# TODO: Section 3 of TODO 14
####################################################################################################

# after you are done reading or writing to a file, you should close it using the .close() function.
fh = open("hello.txt", "r")
contents = fh.read()
print("Last print of the contents to show updated txt file: \n")
print(contents)
fh.close()

# TODO: Section 4 of TODO 14
