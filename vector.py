class Vector:
    '''Represent a vector in a multi dimensional space.'''
    
    def __init__(self, d):
        '''Create a d-dimensional vector of zeros.'''
        self._coords = [0] * d
        
    def __len__(self):
        '''Return the dimension of the vector.'''
        return len(self._coords)
    
    def __getitem__(self, j):
        '''Return jth coordinate of the vector.'''
        return self._coords[j]
    
    def __setitem__(self, j, val):
        '''Set the jth coordinate of vector to given value.'''
        self._coords[j] = val
        
    def __add__(self, other):
        '''Return sum of two vectors'''
        if len(self) != len(other):     # relies on __len__() method
            raise ValueError("Dimensions must agree.")
        result = Vector(len(self))      # start with vector of zeroes
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    
    def __sub__(self, other):
        '''Return difference of two vectors'''
        if len(self) != len(other):     # relies on __len__() method
            raise ValueError("Dimensions must agree.")
        result = Vector(len(self))      # start with vector of zeroes
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result
    
    def __mul__(self):
        self._coords = 
    
    def __neg__(self):
        '''Return all values as negatives.'''
        for j in range(len(self)):
            self[j] *= -1
        return self
    
    def __eq__(self, other):
        '''Return True if vector has same coordinates as the other.'''
        return self._coords == other.__coords
    
    def __ne__(self, other):
        '''Return True if vector differs from other.'''
        return not self == other    # rely on existing __eq__ definition
    
    def __str__(self):
        '''Produce string representation of vector.'''
        return '<' + str(self._coords)[1:-1] + '>'      # adapt list representation
    
    
        
    
v = Vector(5)
v[1] = 23
v[-1] = 45
print(v[4])
u = v + v
print(v)
print(u)
total = 0
for entry in v:
    total += entry
print(total)
u = u - v
print(v)
print(u)
total = 0
for entry in v:
    total += entry
print(total)
x = -u
print(x)