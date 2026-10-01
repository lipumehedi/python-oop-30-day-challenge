from employee import Employee
from manager import EmployeeManager


# Create Employees
employee1 = Employee(
    "Mehedi Lipu",
    "E001",
    "Python Developer",
    350000
)

employee2 = Employee(
    "Rahim",
    "E002",
    "Backend Developer",
    400000
)


# Create Employee Manager
manager = EmployeeManager()


# Add Employees
manager.add_employee(employee1)
manager.add_employee(employee2)


# Show All Employees
print("=== All Employees ===")
manager.show_all_employees()


# Search Employee
print("\n=== Search Employee ===")
manager.search_employee("E002")


# Update Salary
print("\n=== Update Salary ===")
manager.update_salary("E001", 500000)


# Show Updated Employee
print("\n=== Updated Employee ===")
manager.search_employee("E001")


# Delete Employee
print("\n=== Delete Employee ===")
manager.delete_employee("E002")


# Show Employees After Delete
print("\n=== Employees After Delete ===")
manager.show_all_employees()


# Save Employees
print("\n=== Save Employees ===")
manager.save_to_file()


# Load Employees
print("\n=== Load Employees ===")

new_manager = EmployeeManager()
new_manager.load_from_file()

print("\n=== Loaded Employees ===")
new_manager.show_all_employees()


# Exception Handling Test
print("\n=== Validation Test ===")

try:
    invalid_employee = Employee(
        "Test User",
        "E003",
        "Developer",
        -50000
    )

except ValueError as e:
    print(f"Error: {e}")


# Invalid Salary Update Test
print("\n=== Salary Validation Test ===")

try:
    new_manager.update_salary("E001", -10000)

except ValueError as e:
    print(f"Error: {e}")