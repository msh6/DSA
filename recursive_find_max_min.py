def recursive_find_max_min(data, start, stop):
    # Base case: If there are no elements in the range, return None
    if start >= stop:
        return None
    
    # Base case: If there's only one element in the range, return that element for both max and min
    elif start == stop - 1:
        return data[start], data[start]
    
    else:
        
        '''Recursive case: Find the maximum and minimum 
        in the rest of the list (excluding the current element)'''
        rest_max, rest_min = recursive_find_max_min(data, start + 1, stop)
        
        # Compare the maximum and minimum of the rest with the current element
        current_element = data[start]
        '''return (current_element if current_element > rest_max else rest_max,
                current_element if current_element < rest_min else rest_min)'''
                
        max_value = current_element if current_element > rest_max else rest_max
        min_value = current_element if current_element < rest_min else rest_min
        return max_value, min_value
    


seq = [5,4,55,1,89]
max, min = recursive_find_max_min(seq, 0, len(seq))
print(max, min)