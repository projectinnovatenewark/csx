"""
Race Conditions, Locks, and Deadlocks
"""

import time
import threading
from threading import Thread
import random
import sys

# TITLE: Race Conditions

timer = 0

def add_time(seconds):
  global timer
  for _ in range(seconds):
    timer += 10
    time.sleep(0.1)

control = 500
# As we previously explained, threads are lightweight processes that can share
# resources. It can pose a problem, however, when they refer to outdated data.
# If these different threads try to read outdated versions of the timer
# variable, then our assertion of timer after our threads start will throw an
# error. This is called a "race condition".
threads = [Thread(target=control, args=(control, )) for _ in range(10)]

[t.start() for t in threads]

# The += operation in the add_time function runs two operations, it calculates
# the new value for "timer" then assigns it that new value. This causes a
# race condition as it is reading outdated values of this variable.
# TODO: comment this in to demonstrate assertion error for race condition.
# assert timer == (len(threads) * control), f"Invalid value for timer: {timer}"

# TITLE: Locks

# FIXME: THIS DOESNT WORK YET.

# A Lock works in the same way as a four-way stop sign. The first "car" that
# "arrives" to that "intersection", meaning the given resource, has the right of way,
# meaning it "acquires the lock". Any other "cars" reaching that "intersection", or threads
# reaching that now locked resource, must wait for that lock to be released to access the
# resource.

lock = threading.Lock()

def car_driving(lock, sleep=5):
  print(f"Car has reached intersection and has right of way on sleep {sleep}.")
  lock.acquire()
  print("Driver is very rude. Will not drive and is holding up the intersection")
  if sleep:
    time.sleep(sleep)
  print("Driver realizes he is late. Decides to drive and release the lock.")
  lock.release()

t1 = Thread(target=car_driving, args=(lock, ))

t1.start()

lock.acquire()
print("Lock acquired.")

t2 = Thread(target=car_driving, args=(lock, 0))

t2.start()

# print(f"1) Is the lock locked? {lock.locked()}")
# lock.release()
# print(f"2) Is the lock locked? {lock.locked()}")
t1.join()
t2.join()

# THIS IS A GOOD EXAMPLE
# # Importing the threading module
# import threading 
# # Declraing a lock
# lock = threading.Lock()
# deposit = 100
# # Function to add profit to the deposit
# def add_profit(): 
#     global deposit
#     for i in range(100000):
#         lock.acquire()
#         deposit = deposit + 10
#         lock.release()
# # Function to deduct money from the deposit
# def pay_bill(): 
#     global deposit
#     for i in range(100000):
#         lock.acquire()
#         deposit = deposit - 10
#         lock.release()
# # Creating threads
# thread1 = threading.Thread(target = add_profit, args = ())
# thread2 = threading.Thread(target = pay_bill, args = ())
# # Starting the threads  
# thread1.start() 
# thread2.start() 
# # Waiting for both the threads to finish executing 
# thread1.join()
# thread2.join()
# # Displaying the final value of the deposit
# print(deposit)

# TODO: FIX THE TIMER FUNCTION FROM SECTION ONE

# TODO: IMPLEMENT CONTEXT SWITCHING

# TODO: FIX THE TIMER FUNCTION WITH CONTEXT SWITCHING

# TITLE: Deadlocks

