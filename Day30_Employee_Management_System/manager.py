import json

from employee import Employee


class EmployeeManager:

    def __init__(self):
        self.employees = []

    # Add Employee
    def add_employee(self, employee):
        self.employees.append(employee)

    # Show All Employees
    def show_all_employees(self):
        if not self.employees:
            print("No employees found.")
            return

        for employee in self.employees:
            employee.show_employee()
            print("------------------------")

    # Search Employee
    def search_employee(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                employee.show_employee()
                return

        print("Employee not found.")

    # Update Salary
    def update_salary(self, employee_id, new_salary):
        if new_salary <= 0:
            raise ValueError("Salary must be greater than 0.")

        for employee in self.employees:
            if employee.employee_id == employee_id:
                employee.salary = new_salary
                print(f"Salary updated to: ¥{employee.salary}")
                return

        print("Employee not found.")

    # Delete Employee
    def delete_employee(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                self.employees.remove(employee)
                print(
                    f"Employee {employee_id} deleted successfully."
                )
                return

        print("Employee not found.")

    # Save Employees
    def save_to_file(self):
        data = []

        for employee in self.employees:
            employee_data = {
                "name": employee.name,
                "employee_id": employee.employee_id,
                "position": employee.position,
                "salary": employee.salary
            }

            data.append(employee_data)

        with open("employees.json", "w") as file:
            json.dump(data, file, indent=4)

        print("Employees saved successfully.")

    # Load Employees
    def load_from_file(self):
        try:
            with open("employees.json", "r") as file:
                data = json.load(file)

            self.employees = []

            for employee_data in data:
                employee = Employee(
                    employee_data["name"],
                    employee_data["employee_id"],
                    employee_data["position"],
                    employee_data["salary"]
                )

                self.employees.append(employee)

            print("Employees loaded successfully.")

        except FileNotFoundError:
            print("employees.json file not found.")

        except json.JSONDecodeError:
            print("Invalid JSON file.")