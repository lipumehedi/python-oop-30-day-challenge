class Course:
    def __init__(self, course_name):
        self.course_name = course_name
    
    def show_course(self):
        return self.course_name
       
        
class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course
    
    
course1 = Course("Python OOP")
student1 = Student("Mehedi", course1)

print(student1.name)
print(student1.course.show_course())