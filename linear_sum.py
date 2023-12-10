def linear_sum(S, n):
    '''Return the sum of the first n numbers of sequence S.'''
    if n == 0:
        return 0
    else:
        return linear_sum(S, n-1) + S[n-1]
    
seq = [1,2,3,4]
seq1 = linear_sum(seq, len(seq))

print(seq1)