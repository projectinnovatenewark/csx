"""
Introduce sorting algorithms including insertion sort, selection sort, and bubble sort.
"""

# FIXME: Explain insertion sort
def insertion_sort(some_list):
    # for every element in our array
    for index in range(1, len(some_list)):
        current = some_list[index]
        position = index

        while position > 0 and some_list[position-1] > current:
            print("Swapped {} for {}".format(some_list[position], some_list[position-1]))
            some_list[position] = some_list[position-1]
            print(some_list)
            position -= 1

        some_list[position] = current

    print("Sorting Completed.")
    print(some_list)

arr = [12, 11, 2, 13, 5, 6, 19, 9, 17]
insertion_sort(arr)

##################################################################################################