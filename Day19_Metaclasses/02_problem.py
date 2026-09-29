def greet(self):
    print("Hello, Lipu!")


Student = type("Student", (), {"name": "Lipu", "greet": greet})

student = Student()

print(student.name)
student.greet()