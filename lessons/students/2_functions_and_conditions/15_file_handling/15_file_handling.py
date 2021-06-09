"""
Handling files via read, write, and open
"""

# TITLE: Section 1.1 - Opening and Reading Text Files

# TODO:
# Hey Teacher, make sure your working directory of your terminal is in the same working directory
# as hello.txt and my_name_is.txt to access the contents of the files.

# We have previously learned about using the terminal to create, read, edit, and delete text files.
# Python also provides an inbuilt function that allows programmers to perform these same operations
# on files.

# To open a text file we can use the "open()" function. The "open()" function opens a file and
# returns it as a file object. The syntax for opening a file is "open("file_name.txt", mode)"
# where the mode is the method used to open the file. The methods available include
# read, write, append, or create. Below, the argument "r" is used to open the file for reading.
fh = open("hello.txt", "r") # This is just an example of the syntax for using the "open()" function,
                            # but will not provide an output.

# We can use the ".read()" method to read a text file using dot (.) notation and store the contents
# in a variable.
contents = fh.read()
print(f"Contents .read() method:\n{contents}\n") # This prints the contents of "hello.txt" to the terminal.

# IMPORTANT:
# The "open()" function must be called on a file before any operations can be performed on it.

# The "close()" method is used to close open file objects. The "close()" method should be used
# to close a file that is no longer in use. Doing so will reflect any changes made to the file
# after it was opened. The syntax for "close()" is "file_object.close()" as seen below.
fh.close()

####################################################################################################

# TITLE: Section 1.2 - Additional Use Cases for Text Files

# In Python, you can use the ".readline()" method to read each line of a text file one at a time.
# The first call of the ".readline()" method returns the first line of a file and each subsequent
# call returns the next line in the file.
fh = open("hello.txt", "r")
first_line = fh.readline()
second_line = fh.readline()
print(f"Contents .readline() method:\nFirst Line - {first_line}\nSecond Line - {second_line}")
fh.close()

# You can also seperate each line of a file into elements of a list using the ".readlines()" method.
# The newly created list can then be iterated over to view its output.
fh = open("hello.txt", "r")
contents_list = fh.readlines()
print("Contents .readlines() method: \n", contents_list, "\n")
for line in contents_list:
  print(line)
fh.close()

# TODO: Section 1 of TODO 15 (6 min for students, 3 min for demo)

####################################################################################################

# TITLE: Section 2 - Writing and Appending

# The ".write()" method is used to write to a text file. To use "write()", the mode in the "open()"
# function needs to be set to "w". Writing to a file will overwrite its contents with the argument
# passed. The syntax for using the "write()" method is "file_object.write("string")". 
fh = open("hello.txt", "w")
fh.write("Goodbye World") # This overwrites the contents of hello.txt with "Goodbye World"

# After overwriting the file we can open it using the "r" mode to read the file's contents.
fh = open("hello.txt", "r") 
contents = fh.read()
print(f"Contents .read() method:\n{contents}\n")
fh.close()

# You can also write to multiple lines of a text file by using the ".writelines()" method. The
# syntax of the ".writelines" method is "file_object.writelines(text_list)" where "text_list" is
# a list made up of strings.
fh = open("hello.txt", "w")
lines_of_text = ["a line of text \n", "another line of text \n", "a third line \n"]
fh.writelines(lines_of_text)
fh.close()

# Lastly, we can write to a file without overwriting its contents by using the "a" mode in the
# "open()" function. The "write()" method is then used to append to the file.
fh = open("hello.txt", "a") # IMPORTANT: Using append mode vs write mode determines whether
                            # IMPORTANT: or not you overwrite the existing file contents.
message = "Hello World, again."
fh.write(message)
fh.close()

# TODO: Hey Teacher, run this final code block to return the .txt file to its
# TODO: original state.
fh = open("hello.txt", "w")
fh.write("Hello World") # This overwrites the contents of hello.txt with "Hello World".
fh.close()

# TODO: Section 2 of TODO 15 (6 min for students, 3 min for demo)
