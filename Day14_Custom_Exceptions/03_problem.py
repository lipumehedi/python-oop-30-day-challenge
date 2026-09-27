class InvalidMarksError(Exception):
    pass


class Student:
    def __init__(self, marks):
        self.marks = marks

    def validate_marks(self):
        if self.marks < 0 or self.marks > 100:
            raise InvalidMarksError("Marks must be between 0 and 100")


student = Student(134)

try:
    student.validate_marks()
    print("Marks are valid.")
except InvalidMarksError as e:
    print("Error: ", e)