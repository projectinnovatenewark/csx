"""
Handling files via read, write, and open
"""

# to open a text file, use
fh = open("hello.txt", "r")

##################################################################################################

# to read a text file, use
fh = open("hello.txt","r")
print fh.read()

##################################################################################################

# to read one line at a time, use
fh = open("hello.txt", "r")
print fh.readline()

##################################################################################################

# to read a list of lines use
fh = open("hello.txt", "r")
print fh.readlines()

##################################################################################################

# to write to a file, use
fh = open("hello.txt","w")
write("Hello World")
fh.close()

##################################################################################################

# to write to a file, use
fh = open("hello.txt", "w")
lines_of_text = ["a line of text ", "another line of text ", "a third line"]
fh.writelines(lines_of_text)
fh.close()

##################################################################################################

# to append to file, use:
fh = open("Hello.txt", "a")
write("Hello World again")
fh.close()

##################################################################################################

# to close a file, use
fh = open("hello.txt", "r")
print fh.read()
fh.close()