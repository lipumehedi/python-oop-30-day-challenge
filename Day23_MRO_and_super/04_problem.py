class Person:
    def __init__(self):
        print("Person constructor")


class Employee(Person):
    def __init__(self):
        print("Employee constructor")
        super().__init__()


class Manager(Employee):
    def __init__(self):
        print("Manager constructor")
        super().__init__()


manager = Manager()