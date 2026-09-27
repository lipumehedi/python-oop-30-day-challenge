class CountdownIterator:
    def __init__(self, start):
        self.start = start
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start < 1:
            raise StopIteration
        current = self.start
        self.start -= 1
        return current
    
for count in CountdownIterator(5):
    print(count)
        
        