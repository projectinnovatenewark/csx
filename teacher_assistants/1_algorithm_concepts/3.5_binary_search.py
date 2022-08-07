"""Two different implementations of Binary Search"""

# TITLE Iterative Binary Search

def iterative_binary_search(arr, x):
  low = 0
  high = len(arr) - 1
  mid = 0

  while low <= high:
    mid = (high + low) // 2

    # If x is greater, ignore left half
    if arr[mid] < x:
      low = mid + 1

    # If x is smaller, ignore right half
    elif arr[mid] > x:
      high = mid - 1

    # means x is present at mid
    else:
      return mid

  # If we reach here, then the element was not present
  return -1

listy = [1, 3, 4, 7, 9, 10, 15, 16, 20]
print("Iterative Binary Search")
print(iterative_binary_search(listy, 4))

# TITLE Recursive Binary Search

def recursive_binary_search(arr, x, left, right):

  pivot = (left + right) // 2

  if (right >= left):
    # Base Case: pivot, or mid point, is equal to the target
    if (arr[pivot] == x):
      return x
    
    # pivot is less than the target, recurse for right subarray
    elif (arr[pivot] < x):
      return recursive_binary_search(arr, x, pivot+1, right)

    # pivot is greater than the target, recurse for left subarray
    else:
      return recursive_binary_search(arr, x, left, pivot-1)

  else:
    return -1

listy = [1, 3, 4, 7, 9, 10, 15, 16, 20]
print("Recursive Binary Search")
print(recursive_binary_search(listy, 4, 0, len(listy)-1))