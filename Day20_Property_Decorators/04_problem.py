class Student:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.deleter
    def name(self):
        del self._name


student = Student("Lipu")

print(student.name)

del student.name

print("Name deleted successfully!")