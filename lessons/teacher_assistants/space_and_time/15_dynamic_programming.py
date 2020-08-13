"""
Fibinocci Sequence and Dynamic Programming
"""

import time

# Lets implement a basic fib sequence that we went over in the workshop
def fib(n):
    if(n < 2):
        return n
    elif(n >= 2):
        return fib(n-1) + fib(n-2)

# We will use the time package here to calculate how long it will take for our function to run
start = time.time()
print(fib(7))
stop = time.time()

print(f"Time Elapsed for normal implemenation: {stop - start}")

###################################################################################################

# Now, lets implement this same solution using dynamic programming to see how quickly it runs
# in comparison to the above method. Dynamic Programming is mainly an optimization over plain
# recursion. Wherever we see a recursive solution that has repeated calls for same inputs, we can
# optimize it using Dynamic Programming. 

# We will store our fibonacci results in this dictionary and "cache" them, or store them in temporary memory.
# With this technique, also called memoization, we will store the function calls' return values
# to prevent running the same operations again and again.
fib_cach = {}

def dyno_fib(n):
    """

    """
    if(n in fib_cach): # if we have already ran fib(n), return the cached value for the key of "n"
        return fib_cach[n]
    # if fib of n has not been cached already, continue with the normal fibonnaci implementation
    elif(n == 0):
        value = 0
    elif(n == 1 or n == 2):
        value = 1
    elif(n > 2):
        value = dyno_fib(n-1) + dyno_fib(n-2)

    # Once you find fib(n), store the key of n with the value it returned. This means that
    # any future call of this fib(n) will not require additional recursive calls. For example,
    # in fib(7), fib(2) would be called 8 times and require 16 subsequent recursive calls. To avoid
    # that redundancy, we store fib(2)'s value the first time it is found and will save our function
    # from running 14 unnecessary function calls.
    fib_cach[n] = value
    return value

start = time.time()
print(dyno_fib(7))
stop = time.time()

print(f"Time Elapsed for Dynamic Version: {stop - start}")

###################################################################################################

fib_dict = {}
def downUpFib(n):
    for k in range(1, n+1):
        if k <= 2:
            f = 1
            # print("Base: ", k, f)
        else:
            f = fib_dict[k-1] + fib_dict[k-2]
        fib_dict[k] = f
        # print("recursive: ", k, f)
    return fib_dict[n]

start = time.time()
print(downUpFib(7))
stop = time.time()

print(f"Time Elapsed for Bottom - Up Version: {stop - start}")