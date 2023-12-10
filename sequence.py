from abc import ABCMeta, abstractmethod             # need the functions

class Sequence(metaclass=ABCMeta):
    '''Our own version of collections.Sequence abstract base class.'''
    
    @abstractmethod
    def __len__(self):
        '''Return the length of the sequence.'''
        
    @abstractmethod
    def __getitem__(self, j):
        '''Return at the element at index j of sequence.'''
        
    def __contains__(self, val):
        '''Return True if val found in the sequence, False otherwise.'''
        for i in range(len(self)):
            if self[i] == val:
                return True
        return False
    
    def index(self, val):
        '''Return the left most index at which val is found (or raise error).'''
        for j in range(len(self)):
            if self[j] == val:          # left most match
                return j
        raise ValueError('value not in the sequence')   # never found a match

    def counter(self, val):
        '''Return the number of elements equal to a given value.'''
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
        return k
    
    #def __eq__(self, other):
        
seq = Sequence()