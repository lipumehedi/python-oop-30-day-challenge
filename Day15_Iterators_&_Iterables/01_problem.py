class NumberIterator:
    def __init__(self, count):
        self.count = count
        
        
    def __iter__(self):
       return self
   
    def __next__(self):
        if self.count > 5:
           raise StopIteration
        current = self.count
        self.count += 1
        return current


for number in NumberIterator(1):
    print(number)