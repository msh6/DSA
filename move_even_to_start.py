def move_even_to_start(s):
    # Base case: return the list if only one element
    if len(s) == 0:
        return s
     
    # Recursive case: check for even number and moving to start to newly created list
    if s[0] % 2 == 0:
        return [seq[0]] + move_even_to_start(seq[1:])
    else:
        return move_even_to_start(seq[1:]) + [seq[0]]

seq = [1,2,3,4,5,6,7,8,9,10]
print(move_even_to_start(seq))