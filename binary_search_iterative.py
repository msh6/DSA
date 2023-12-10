def binary_search_iterative(data, target):
    '''Return True if target is found in the given Python list.'''
    low = 0
    high = len(data)-1
    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:         # found a match
            return True
        elif target < data[mid]:
            high = mid - 1              # only consider values left of mid
        elif target > data[mid]:
            low = mid + 1               # only consider values right of mid
    return False                        # loop ended without success

nums = [n for n in range(35)]
print(nums)

print(binary_search_iterative(nums, 131))