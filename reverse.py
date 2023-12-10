def reverse(S, start, stop):
    '''Reverse elements in implicit slice S[start:stop].'''
    if start < stop -1:
        S[start], S[stop-1] = S[stop-1], S[start]
        reverse(S, start+1, stop-1)
        
seq = [1,2,3,4]
seq1 = reverse(seq, 0, 4)
print(seq)