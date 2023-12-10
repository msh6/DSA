def recursive_find_max(data, start, stop):
    # Base case: If there are no elements in the range, return None
    if start >= stop:
        return None
    
    # Recursive case: Find the maximum value in the rest of the list
    rest_max = recursive_find_max(data, start + 1, stop)
    
    # Compare the maximum of the rest with the current element
    if rest_max is None or data[start] > rest_max:
        return data[start]
    else:
        return rest_max
   
seq = [5,4,55,1,89]
print(recursive_find_max(seq, 0, len(seq)))