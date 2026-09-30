class Father:
    def __init__(self):
        self.father_name = "Mr. Rahman"

class Mother:
    def __init__(self):
        self.mother_name = "Mrs. Rahman"

class Child(Father, Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)

    def show_father(self):
        print(f"Father: {self.father_name}")

    def show_mother(self):
        print(f"Mother: {self.mother_name}")


child = Child()

child.show_father()
child.show_mother()