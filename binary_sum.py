def binary_sum(S, start, stop):
    '''Return the sum of the numbers in implicit slice S[start:stop].'''
    if start>stop:                  # Zero elements in slice
        return 0
    elif start == stop-1:           # one element in slice
        return S[start]
    else:
        mid = (start + stop) // 2
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)
    
seq = [1,2,3,4]
seq1 = binary_sum(seq, 0, len(seq))

print(seq1)