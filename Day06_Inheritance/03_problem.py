class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show_person_info(self):
        return f"{self.name} - {self.age} years old"
    

class Employee(Person):
    def __init__(self, name, age, job):
        super().__init__(name, age)
        self.job = job
    def show_employee_info(self):
        return f"{self.name} - {self.age} years old - {self.job}"
          

employee1 = Employee("Mehedi", 30, "Software Engineer")

print(employee1.name)
print(employee1.age)
print(employee1.job)
print(employee1.show_person_info())
print(employee1.show_employee_info())