class _Node:
    '''Lightweight, nonpublic class for storing a double linked node.'''
    __slots__ = '_element', '_prev', '_next'             # streamline memory
    
    def __init__(self, element, prev, next):            # initialize node's feilds
        self._element = element                         # user's element
        self._prev = prev                               # previous node reference 
        self._next = next                               # next node reference   