"""
Handling files via read, write, and open
"""

# IMPORTANT!!! YOUR WORKING DIRECTORY OF YOUR TERMINAL MUST BE IN THE WEEK_3 FOLDER FOR THE PROGRAM
# TO RUN. IT WILL NOT RECOGNIZE THE HELLO.TXT FILE UNTIL YOUR WORKING DIRECTORY IS WITHIN WEEK_3

# to open a text file, use
fh = open("hello.txt", "r")

####################################################################################################

# to read a text file, use
fh = open("my_name_is.txt", "r")
contents = fh.read()
print(contents)

####################################################################################################

# to read one line at a time, use
fh = open("my_name_is.txt", "r")
contents = fh.readline()
print(contents)

####################################################################################################

# to separate each line into items in a list, use the .readlines() function.
fh = open("my_name_is.txt", "r")
contents = fh.readlines()
print(contents)

# if you want to iterate through the list, do it as such
for line in contents:
    print(line)

####################################################################################################

# to write to a file, use
fh = open("hello.txt", "w")
fh.write("Hello World")
fh.close()

####################################################################################################

# to write to a file, use
fh = open("hello.txt", "w")
lines_of_text = ["a line of text ", "another line of text ", "a third line "]
fh.writelines(lines_of_text)
fh.close()

####################################################################################################

# to append to file, use:
fh = open("hello.txt", "a")
message = "Hello world, again"
fh.write(message)
fh.close()

####################################################################################################

# after you are done reading or writing to a file, you should close it using the .close() function.
fh = open("hello.txt", "r")
contents = fh.read()
print(contents)
fh.close()
