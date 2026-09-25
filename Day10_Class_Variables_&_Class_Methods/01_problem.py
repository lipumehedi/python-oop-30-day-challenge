class Employee:
    company = "ABC Company"
    
    def __init__(self, name):
       self.name = name

employee1 = Employee("Mehedi")
employee2 = Employee("Rahim")

print(f"{employee1.name} - {employee1.company}")
print(f"{employee2.name} - {employee2.company}")