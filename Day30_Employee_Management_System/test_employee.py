import unittest

from employee import Employee
from manager import EmployeeManager


class TestEmployee(unittest.TestCase):

    # Test Employee Creation
    def test_employee_information(self):
        employee = Employee(
            "Mehedi Lipu",
            "E001",
            "Python Developer",
            350000
        )

        self.assertEqual(employee.name, "Mehedi Lipu")
        self.assertEqual(employee.employee_id, "E001")
        self.assertEqual(employee.position, "Python Developer")
        self.assertEqual(employee.salary, 350000)

    # Test Salary Update
    def test_salary_update(self):
        employee = Employee(
            "Mehedi Lipu",
            "E001",
            "Python Developer",
            350000
        )

        employee.salary = 500000

        self.assertEqual(employee.salary, 500000)

    # Test Invalid Salary
    def test_invalid_salary(self):
        with self.assertRaises(ValueError):
            Employee(
                "Mehedi Lipu",
                "E001",
                "Python Developer",
                -50000
            )

    # Test Empty Name
    def test_empty_name(self):
        with self.assertRaises(ValueError):
            Employee(
                "",
                "E001",
                "Python Developer",
                350000
            )


class TestEmployeeManager(unittest.TestCase):

    # Test Add Employee
    def test_add_employee(self):
        manager = EmployeeManager()

        employee = Employee(
            "Mehedi Lipu",
            "E001",
            "Python Developer",
            350000
        )

        manager.add_employee(employee)

        self.assertEqual(len(manager.employees), 1)
        self.assertEqual(manager.employees[0].name, "Mehedi Lipu")

    # Test Delete Employee
    def test_delete_employee(self):
        manager = EmployeeManager()

        employee = Employee(
            "Mehedi Lipu",
            "E001",
            "Python Developer",
            350000
        )

        manager.add_employee(employee)
        manager.delete_employee("E001")

        self.assertEqual(len(manager.employees), 0)

    # Test Salary Update
    def test_manager_salary_update(self):
        manager = EmployeeManager()

        employee = Employee(
            "Mehedi Lipu",
            "E001",
            "Python Developer",
            350000
        )

        manager.add_employee(employee)
        manager.update_salary("E001", 500000)

        self.assertEqual(manager.employees[0].salary, 500000)

    # Test Invalid Salary Update
    def test_invalid_salary_update(self):
        manager = EmployeeManager()

        with self.assertRaises(ValueError):
            manager.update_salary("E001", -10000)


if __name__ == "__main__":
    unittest.main()