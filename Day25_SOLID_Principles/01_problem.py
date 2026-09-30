class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary


class EmployeeRepository:
    def save(self, employee):
        print("Employee saved to database")


class EmailService:
    def send_email(self, employee):
        print("Email sent")


employee = Employee("Mehedi", 350000)

repository = EmployeeRepository()
email_service = EmailService()

print(f"Salary: {employee.calculate_salary()}")

repository.save(employee)
email_service.send_email(employee)