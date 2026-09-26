class Employee:
    
    @staticmethod
    def is_valid_salary(salary):
        return salary > 0
    

print(Employee.is_valid_salary(300000))  
print(Employee.is_valid_salary(0))       
print(Employee.is_valid_salary(-5000))   