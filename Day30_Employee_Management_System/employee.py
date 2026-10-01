class Employee:
    def __init__(self, name, employee_id, position, salary):
        if not name:
            raise ValueError("Employee name cannot be empty.")
        
        if not employee_id:
            raise ValueError("Employee ID cannot be empty.")
        
        if not position:
            raise ValueError("Employee position cannot be empty.")
        
        if salary <= 0:
            raise ValueError("Salary must be greater than 0.")
        
        self.name = name
        self.employee_id = employee_id
        self.position = position
        self.salary = salary
    
    def show_employee(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Position: {self.position}")
        print(f"Salary: ¥{self.salary}")        