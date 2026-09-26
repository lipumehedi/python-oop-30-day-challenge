class NumberUtility:
    
    @staticmethod
    def is_even(number):
        return number %2 == 0
            
        
    @staticmethod
    def is_positive(number):
        return number > 0
        
        

print(NumberUtility.is_even(10))      
print(NumberUtility.is_even(7))       
print(NumberUtility.is_positive(5))   
print(NumberUtility.is_positive(-3))  