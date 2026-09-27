class NameIterator:
    def __init__(self, names):
        self.names = names
        self.index = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.names):
            raise StopIteration
        current = self.names[self.index]
        self.index += 1
        return current 
for name in NameIterator(["Lipu", "Rahim", "Karim", "Hasan"]):
    print(name) 