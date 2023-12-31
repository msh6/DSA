'''def power(x, n):
    """Compute the value x n for integer n."""
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)
    
print(power(5, 4))'''


def power(x, n):
    '''Compute the value x n for integer n.'''
    if n == 0:
        return 1
    else:
        partial = power(x, n//2)        # rely on truncated division
        result = partial * partial
        if n % 2 == 1:                  # if n odd, include extra factor of x
            result *= x
        return result
            
print(power(2, 9))