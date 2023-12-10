from progression import Progression

class FibonacciProgression(Progression):
    '''Iterator producing a generalized Fibonacci Progression.'''
    
    def __init__(self, first=0, second=1):
        '''Create a new Fibonacci progression.
        
        first       the first term of the progression (default 0)
        second      the second term of the progression (default 1)
        '''
        super().__init__(first)     # start progression at first
        self._prev = second - first
        
    def _advance(self):
        self._prev, self._current = self._current, self._prev + self._current
        
fib = FibonacciProgression(0, 1)
fib.print_progression(30)