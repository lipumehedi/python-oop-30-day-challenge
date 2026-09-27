class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def __eq__(self, other):
        return self.marks == other.marks
    
student1 = Student("Mehedi", 90)
student2 = Student("Rahim", 90)
student3 = Student("Karim", 75)

print(student1 == student2)  
print(student1 == student3)  