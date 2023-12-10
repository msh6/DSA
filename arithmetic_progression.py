from progression import Progression
class ArithmeticProgression(Progression):           # inherit from progression
    '''Iterator producing an arithmetic progression.'''
    
    def __init__(self, start=0, increment=1,):
        '''Create a new arithmetic progression.
        
        increment       the fixed constant to add to each term(default 1)
        start           the first term of progression (default 0)
        '''
        
        super().__init__(start)     # initialize the base
        self._increment = increment
        
    def _advance(self):             #override inherited version
        '''Update current value by adding the fixed increment.'''
        self._current += self._increment