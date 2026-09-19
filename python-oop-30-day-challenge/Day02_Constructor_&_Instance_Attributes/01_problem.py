class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
        
        
student1 = Student("Mehedi", 30, "Python")
student2 = Student("Rahim", 25, "Python")
student3 = Student("Karim", 27, "Python")  
    
print(
    f"Name: {student1.name}\n"
    f"Age: {student1.age}\n"
    f"Course: {student1.course}\n"
)

print(
    f"Name: {student2.name}\n"
    f"Age: {student2.age}\n"
    f"Course: {student2.course}\n"
)

print(
    f"Name: {student3.name}\n"
    f"Age: {student3.age}\n"
    f"Course: {student3.course}\n"
)