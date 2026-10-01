import unittest

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

    def give_raise(self, amount):
        self.salary += amount
        return self.salary


class TestEmployee(unittest.TestCase):

    def test_get_salary(self):
        employee = Employee("Mehedi", 350000)
        result = employee.get_salary()
        self.assertEqual(result, 350000)

    def test_give_raise(self):
        employee = Employee("Mehedi", 350000)
        result = employee.give_raise(50000)
        self.assertEqual(result, 400000)

    def test_employee_name(self):
        employee = Employee("Mehedi", 350000)
        self.assertEqual(employee.name, "Mehedi")

if __name__ == "__main__":
    unittest.main()