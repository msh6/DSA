def recursive_mul(m, n):
    # Base case
    if n == 0:
        return 0
    else:
        # recursive case
        prod = m + recursive_mul(m, n-1)    
        return prod
    
    
print(recursive_mul(10, 99))