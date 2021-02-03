# Binary search on a one dimensional list

def binary_search(low, high, target):
    if (low == high or low + high <= 0):
        if (nums[low] == target):
            return low
        else:
            return -1
        
    else:
        mid_point = (low + high) / 2
        mid_point = int(mid_point)

        if (target == nums[mid_point]):
            return mid_point
        if (target < nums[mid_point]):
            return binary_search(low, mid_point-1, target)
        else:
            return binary_search(mid_point+1, high, target)
        
return binary_search(0, len(nums)-1, target)