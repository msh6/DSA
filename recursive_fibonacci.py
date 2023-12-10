# recursive fibonacci

def recursive_fibonacci(n):
    '''”Return pair of Fibonacci numbers, F(n) and F(n-1).'''
    if n <= 1:
        return(n, 0)
    else:
        (a, b) = recursive_fibonacci(n-1)
        return (a+b, a)
    
print(recursive_fibonacci(10))