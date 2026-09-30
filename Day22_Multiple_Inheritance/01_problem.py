class Father:
    def father_skill(self):
        return "Father can drive."
    

class Mother:
    def mother_skill(self):
        return "Mother can cook."
    
class Child(Father, Mother):
        pass   
child = Child()
    
print(child.father_skill())
print(child.mother_skill()) 