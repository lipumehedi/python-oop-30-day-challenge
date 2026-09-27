class EvenNumberIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.end < self.start:
            raise StopIteration
        if self.start % 2 != 0:
            self.start += 1
        current = self.start
        self.start += 2
        return current
    
for even in EvenNumberIterator(1,10):
    print(even)