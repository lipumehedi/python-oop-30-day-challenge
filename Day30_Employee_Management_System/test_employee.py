import unittest

from employee import Employee


class TestEmployee(unittest.TestCase):

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

    def test_salary_update(self):
        employee = Employee(
            "Mehedi Lipu",
            "E001",
            "Python Developer",
            350000
        )

        employee.salary = 500000
        self.assertEqual(employee.salary, 500000)

if __name__ == "__main__":
    unittest.main()