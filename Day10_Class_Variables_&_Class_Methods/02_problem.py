class Student:
    school = "ABC School"
    
    def __init__(self, name):
        self.name = name
        

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school
     
     
student1 = Student("Mehedi")
student2 = Student("Rahim")

print(student1.school)
print(student2.school)

Student.change_school("XYZ School")

print(student1.school)
print(student2.school)