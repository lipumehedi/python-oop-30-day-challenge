class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def __repr__(self):
       return f"Employee(name='{self.name}', salary={self.salary})"
   

employee1 = Employee("Mehedi", 300000)

print(repr(employee1))