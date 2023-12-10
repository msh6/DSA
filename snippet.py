''''def foo(s, k):
    
    if len(s) < 2:
        return False
    
    if s[0] + s[1] == k:
        return True
    
    return foo(s[1:], k)

seq = [1,2,3,4,5,9,11]
print(foo(seq, 101))


def foobar(s, k, start=0):
    if start < len(s)-1:
        if s[start] + s[start+1] == k:
            return [start, start + 1]
        
    if start < len(s) - 1:
        return foobar(s, k, start+1)

indices = foobar(seq, 14)
print(indices)
        
        
def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n-1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n-1, auxiliary, source, target)

# Example usage:
tower_of_hanoi(3, 'A', 'B', 'C')
'''

'''from time import time               # import time function from time module
def compute_average(n):
    ''''''Perform n appends to an empty list and return average time elapsed.''''''
    data = []
    start = time()                  # record start time in seconds
    for k in range(n):
        data.append(None)
    end = time()                    # record end time in seconds
    return (end-start) /n           # compute average per operation

print(compute_average(100000000))'''
'''
a = ord('A')
b = a + 3
print(chr(b))

c = list('bird')
d = ' '.join(c)
print(d)


data = [[0] * 5 for _ in range(3)]
print(data)


threeDarray = [[1,1,1,1], [2,2,2,2], [3,3,3,3]]
threeDarray1 = [[4,4,4,4], [5,5,5,5], [6,6,6,6]]

addedlist = threeDarray + threeDarray1
#print(addedlist)


def foo(set1, set2):
    temp = list()
    for i in range(len(set1)):
        result_inner = []
        for j in range(len(set1[i])):
            result_inner.append(set1[i][j] + set2[i][j])
        temp.append(result_inner)
    return temp

a = foo(threeDarray, threeDarray1)
print(a)
'''

mylist = "[{(a)}]"
for i in mylist:
    if i == 'a':
        print(mylist.index(i))
print(mylist.index('{'))