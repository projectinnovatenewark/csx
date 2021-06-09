"""
Threads and Multithreading Introduction
"""

# good logical explanation:
# https://medium.com/mineiros/how-to-use-multithreading-and-multiprocessing-a-beginners-guide-to-parallel-and-concurrent-a69b9dd21e9d#608f
# when to use multithread vs process vs asyncio:
# https://stackabuse.com/concurrency-in-python/#:~:text=Both%20concurrency%20and%20parallelism%20are,have%20tasks%20done%20in%20parallel.

# TITLE: Multithreading Programming

# Multithreading is the concept that a CPU is able to execute multiple threads concurrently. This
# could help a computer to execute multiple tasks within a single process with shared memory.
# This allows certain programs to execute faster.

import time
import requests
from threading import Thread

# Define a function that takes some time to execute
def threadly():
  print('hello')
  time.sleep(1)
  print('world')

# Instantiate a thread. The target attribute of a thread should be something
# callable, like a function.
thread_one = Thread(target=threadly)

# This is how to start a thread with your new thread instance.
thread_one.start()

# The join method will await the completion of the thread before continuing the program.
thread_one.join()

# Let's imagine that a function is making a call to some external API. This can be a
# very slow operation under conditions such as bad connection. If our program needs
# to make several of these calls, we would not necessarily want each call to wait
# for the previous call to complete. In this case, we can make use of multithreading.

# The documentation for the dog api can be found here: https://docs.thedogapi.com/

breeds = ["Terrier", "Retriever", "Bulldog"]
breed_purposes = []

def dog_info(breed):
  response = requests.get(f"https://api.thedogapi.com/v1/breeds/search?name={breed}")
  response_jsonified = response.json()
  breed_purpose = response_jsonified[0]["bred_for"]
  breed_purposes.append(breed_purpose)
  print(f"{breed}s are bred for {breed_purpose}")

# Lets call the above function for each of our breeds to discover their purpose.
# This will execute each function call, and subsequently each API call in the function,
# one-by-one. We will use the time package to track how long these function calls
# take to execute.
start_time = time.time()

[dog_info(breed) for breed in breeds]

end_time = time.time()
time_to_run = end_time - start_time
print(f"The time it took for the above to execute was {time_to_run}, and the purposes are \n {breed_purposes}")

# Lets imagine that we want these API calls to be run concurrently in an attempt to speed
# up our program.

breed_purposes = []

# This will instantiate a thread for each of our breeds, and use the dog_info function as our
# callable. Additionally, we will pass an argument to our function with the "args" attribute.
# Note that even if we only pass one argument to our callable function, we still pass it as
# an item in a tuple (hence the parentheses aruond our args variable).
threads = [Thread(target=dog_info, args=(breed, )) for breed in breeds]

start_time = time.time()
[t.start() for t in threads];
[t.join() for t in threads];

end_time = time.time()
time_to_run = end_time - start_time

# Also note that since our function calls were concurrently, the breed purposes may not correspond
# to the same order as they are in the breeds list. This demonstrates that these threads shared
# storage since they accessed the same list in "breed purposes", but it also demonstrates that
# they executed independently in terms of time.
print(f"The time it took for the above to concurrently execute was {time_to_run}, and the purposes are \n {breed_purposes}")







# TITLE: AsyncIO Programming