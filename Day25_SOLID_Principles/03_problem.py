# LSP ?
# Child class-কে Parent class-এর জায়গায় ব্যবহার করলেও program-এর behavior ভেঙে যাওয়া উচিত নয়।

# Bad Design
"""
class Bird:

    def fly(self):
        print("Bird is flying")


class Sparrow(Bird):
    pass


class Penguin(Bird):

    def fly(self):
        raise Exception("Penguins cannot fly")
"""

class Bird:
    def eat(self):
        print("Bird is eating")

class FlyingBird(Bird):
    def fly(self):
        print("Bird is flying")

class Sparrow(FlyingBird):
    pass

class Penguin(Bird):
    def swim(self):
        print("Penguin is swimming")

def make_bird_eat(bird):
    bird.eat()

def make_bird_fly(bird):
    bird.fly()

sparrow = Sparrow()
penguin = Penguin()

make_bird_eat(sparrow)
make_bird_eat(penguin)

make_bird_fly(sparrow)