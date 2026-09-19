class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def show_info(self):
        print(f"Name: {self.name} \nSalary: {self.salary}\n")
    
    def increase_salary(self, amount):
        self.salary += amount

employee1 = Employee("Mehedi", 280000)
employee2 = Employee("Rahim", 300000)
employee3 = Employee("Karim", 350000)

employee1.show_info()
employee1.increase_salary(30000)
employee1.show_info()
employee2.show_info()
employee3.show_info()
