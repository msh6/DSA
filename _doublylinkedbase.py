from _node import _Node
class _DoublyLinkedBase:
    '''A base class providing a doubly linked list representation.'''
    
    def __init__(self):
        '''Create an empty list.'''
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer              # trailer is after header
        self._trailer._prev = self._header              # header is before trailer
        self._size = 0                                  # number of elements
        
    def __len__(self):
        '''Return the number of elements in the list.'''
        return self._size
    
    def is_empty(self):
        '''Return True if list is empty.'''
        return self._size == 0
    
    def _insert_between(self, e, predecessor, successor):
        '''Add element e between two existing nodes and return new node.'''
        newest = self._Node(e, predecessor, successor)      # linked to neighbors
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest
    
    def _delete_node(self, node):
        '''Delete nonsentinel node from the list and return its element.'''
        predecessor, successor = node._prev, node._next
        predecessor._next, successor._prev = successor, predecessor
        self._size -= 1
        element = node._element                         # record deleted element
        node._prev = node._next = node._element = None  # deprecate node
        return element                                  # return deleted element