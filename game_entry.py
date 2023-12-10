class GameEntry:
    '''Represent one entry of a list of highscores.'''
    
    def __init__(self, name, score) -> None:
        self._name = name
        self._score = score
        
    def get_name(self):
        return self._name
    
    def get_score(self):
        return self._score
    
    def __str__(self):
        return f'({self._name}, {self._score})'
    
# Create a GameEntry object
entry1 = GameEntry("Player1", 1000)

# Get the name and score from the object
name = entry1.get_name()
score = entry1.get_score()

# Print the GameEntry object as a string
print(entry1) 