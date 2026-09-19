class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        
employee1 = Employee("Mehedi", 30, 280000)
employee2 = Employee("Rahim",  28, 300000)
employee3 = Employee("Karim",  32, 350000)

print(f" Name: {employee1.name} Age: {employee1.age} Salary: {employee1.salary}")
print(f" Name: {employee2.name} Age: {employee2.age} Salary: {employee2.salary}")
print(f" Name: {employee3.name} Age: {employee3.age} Salary: {employee3.salary}")

employee2.salary = 330000

print(f" Name: {employee1.name} Age: {employee1.age} Salary: {employee1.salary}")
print(f" Name: {employee2.name} Age: {employee2.age} Salary: {employee2.salary}")
print(f" Name: {employee3.name} Age: {employee3.age} Salary: {employee3.salary}")