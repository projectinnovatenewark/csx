"""
Introduce sorting algorithms including insertion sort, mergesort, and quicksort.
"""

# Two less common sorting algorithms are bubble sort and selection sort.
# Due to the infrequency with which they're used, we will leave them to
# a future video and detail the methods and time/space complexities there.

# TITLE: Insertion Sort
def insertion_sort(some_list):
  # for every element in our array, execute the following:
  for index in range(1, len(some_list)):
    current = some_list[index]
    position = index

    # if current num is less than previous num, swap them till current num is in sorted position
    while position > 0 and some_list[position-1] > current:
      print("Swapped {} for {}".format(some_list[position], some_list[position-1]))
      some_list[position] = some_list[position-1]
      print(some_list)
      position -= 1

      some_list[position] = current

  return some_list

arr = [12, 11, 2, 13, 5, 6, 19, 9, 17]
print(f"Insertion sort result {insertion_sort(arr)}")

##################################################################################################

# TITLE: Mergesort
def merge(left, right):
  both = []
  left_idx, right_idx = 0, 0
  while left_idx < len(left) and right_idx < len(right):
    if (left[left_idx] < right[right_idx]):
      both.append(left[left_idx])
      left_idx += 1
    else:
      both.append(right[right_idx])
      right_idx += 1
  
  if (left_idx == len(left)):
    both.extend(right[right_idx:])
  else:
    both.extend(left[left_idx:])
  return both

def mergesort(listy):
  if (len(listy) <= 1):
    return listy
  midpoint = len(listy) // 2
  left, right = mergesort(listy[:midpoint]), mergesort(listy[midpoint:])
  return merge(left, right)

arr = [12, 11, 2, 13, 5, 6, 19, 9, 17]
print(f"Mergesort result {mergesort(arr)}")

##################################################################################################

# TITLE: Quicksort
def quicksort(listy):
  if (len(listy) <= 1):
    return listy

  pivot = (len(listy)-1) // 2
  pivot_num = listy.pop(pivot)
  smaller, larger = [], []
  for num in listy:
    if (num < pivot_num):
      smaller.append(num)
    else:
      larger.append(num)
  
  return quicksort(smaller) + [pivot_num] + quicksort(larger)

arr = [12, 11, 2, 13, 5, 6, 19, 9, 17]
print(f"Quicksort result {quicksort(arr)}")