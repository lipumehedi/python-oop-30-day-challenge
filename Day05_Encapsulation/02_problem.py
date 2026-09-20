class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
    
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, new_salary):
        self.__salary = new_salary
        

employee1 = Employee("Mehedi", 300000)

print(employee1.get_salary())

employee1.set_salary(350000)

print(employee1.get_salary())      