"""
try/except/finally with error handling
"""

# here, we will try to open a test.txt file. Since there is no test.txt file,
# we will raise an exception using "except". Since our try creates an error then the
# exception will be raised, and the finally code block executes thereafter.

try:
    f = open("test.txt", 'r')
    data = f.read()
    print("Trying")
except:
    print("Fiddlesticks! Failed")
finally:
    print("Finally!")
    print("All Done")

# This is the same code as above, except that the "else" block will ONLY happen if there is no error.
# Finally will happen whether there is an error or not. Else will only happen if there is no error.

try:
    f = open("test.txt", 'r')
    data = f.read()
    print("Trying")
except:
    print("Fiddlesticks! Failed")
else:
    print("Finally!")
    print("All Done")

# when using explicit error handling, its important to handle errors efficiently.
# With try/except/finally's, an IOError is the most common type to be served.
# So, let's try it this way

try:
    f = open("test.txt", "r")
    try:
        data = f.read()
        print(data)
    except IOError as e:
        print("IO Error", e)
    except:
        print("unknown error")
    finally:
        f.close()
except:
    print("Fiddlesticks! Failed")
finally:
    print("All Done")

# this is a cleaner way to do the same thing as above.
# When we use the "with-as" tags, it automatically executes the
# open and subsequent "close" tag. Now the above function looks
# a lot cleaner and can be done in less lines of code

try:
    with open("test.txt", "r") as f:
        data = f.read()
        print(data)
except IOError as e:
    print(e)
except:
    print("Fiddlesticks! Failed")
finally:
    print("Finally! We iz done!")

print("All Done")

# this function does something similar to a try/except
# In the code above, you can see we created a class called BadNumbrersError.
# Then in our function, we added a check. If x==3, then raise a BadNumbersError
# exception and pass in the text “We don’t like the number 3”.
# This is a simple way to raise a custom exception using a python class.
# 'pass' is used for no particular reason. It is there purely for syntax reasons.
class BadNumbersError(Exception):
    pass

def addnumbers(x, y):
    if x == 3:
        raise BadNumbersError("We don't like the number 3")
    return x+y

print(addnumbers(3, 2))
