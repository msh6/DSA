def recursive_reverse_string(s):
    # Base case: if string empty or contains only one character
    if not s or len(s) == 1:
        return s
    else:
        return s[-1] + recursive_reverse_string(s[1:-1]) + s[0]
    
print(recursive_reverse_string("castle"))