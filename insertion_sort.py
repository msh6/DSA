def insertion_sort(A):
    '''Sort list of comparable elements into nondecreasing order.'''
    for k in range(1, len(A)):              # from 1 to -1
        current = A[k]                      # current element to inserted
        j = k                               # find correct index j for current
        while j > 0 and A[j-1] > current:   # element A[j-1] must be after current
            A[j] = A[j-1]
            j -= 1
        A[j] = current                      # current is now in the right place
        
    #return A

mylist = ['B', 'C', 'D', 'A', 'E', 'H', 'G', 'F']
insertion_sort(mylist)
print(mylist)