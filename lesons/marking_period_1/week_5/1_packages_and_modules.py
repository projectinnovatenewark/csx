"""
Introduction to the packages Numpy, Pandas, Matplotlib, Scikit-Learn, Scipy, Asyncio and Time
"""

# packages are a really useful way to expand what your program is capable of
# dealing with things like handling multi demensional arrays and table visualizations
# are really hard to do with "vanilla" python (using plain code without packages)

# lets introduce these packages one by one with simple examples

####################################################################################################

# Let's start with the numpy package. We can install this package using pip (the python package
# installer). The command is `pip install numpy`. Numpy is the fundamental package for scientific
# computing with Python. It contains various features including these important ones:
# 1) A powerful N-dimensional array object
# 2) Sophisticated (broadcasting) functions
# 3) Tools for integrating C/C++ and Fortran code
# 4) Useful linear algebra, Fourier transform, and random number capabilities

# Python program to demonstrate  
# basic array characteristics 
import numpy as np 
  
# Creating array object 
arr = np.array( [[ 1, 2, 3], 
                 [ 4, 2, 5]] ) 
  
# Printing type of arr object 
print("Array is of type: ", type(arr)) 
  
# Printing array dimensions (axes) 
print("No. of dimensions: ", arr.ndim) 
  
# Printing shape of array 
print("Shape of array: ", arr.shape) 
  
# Printing size (total number of elements) of array 
print("Size of array: ", arr.size) 
  
# Printing type of elements in array 
print("Array stores elements of type: ", arr.dtype) 


####################################################################################################

# pandas is a Python package providing fast, flexible, and expressive data structures designed to
# make working with “relational” or “labeled” data both easy and intuitive. It aims to be the
# fundamental high-level building block for doing practical, real world data analysis in Python.
# The two primary data structures of pandas, Series (1-dimensional) and DataFrame (2-dimensional),
# handle the vast majority of typical use cases in finance, statistics, social science, and many
# areas of engineering.
# Install package with: pip install pandas

import numpy as np
import pandas as pd


# this example will create a nice data frame to present this data in a readable way
df2 = pd.DataFrame({'A': 1.,
    'B': pd.Timestamp('20130102'),
    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
    'D': np.array([3] * 4, dtype='int32'),
    'E': pd.Categorical(["test", "train", "test", "train"]),
    'F': 'foo'})

print(df2)

# to get a zippy run through on pandas, feel free to check out this link:
# https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html

####################################################################################################

# Matplotlib

####################################################################################################

# Scikit-Learn

####################################################################################################

# Scipy

####################################################################################################

# asyncio allows you to create async-await functions. async is what you declare before the function
# and it stands for "asynchronous". What this function does is await the execution of the command
# denoted after the await declaration.
# link for reference: https://docs.python.org/3/library/asyncio-task.html

# we also use the time package. dealing with time in code is one of the more consistent, horribly
# annoying things you'd deal with in your career as a software engineer
# link for reference: https://docs.python.org/3/library/time.html

import asyncio
import time

async def hey():
    """async.sleep creates a timer, in this case of 3 seconds"""

    print('hello')
    await asyncio.sleep(3)
    print('world')

asyncio.run(hey())


async def say_after(delay, word):
    """this function takes in two arguments: a number and a string"""

    await asyncio.sleep(delay)
    print(word)

async def clock():
    """this function calls the say after function twice to print 'hello world'"""
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

asyncio.run(clock())

async def task_clock():
    """uses asyncio function create_task to run the tasks concurrently"""
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

asyncio.run(task_clock())
