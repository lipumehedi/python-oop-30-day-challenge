class Father:
    def drive(self):
        return "Father can drive."
    
class Mother:
    def cook(self):
        return "Mother can cook."
    
class Teacher:
    def teach(self):
        return "Teacher can teach."
    
class Child(Father, Mother, Teacher):
    pass

child = Child()

    
print(child.drive())
print(child.cook())
print(child.teach()) 