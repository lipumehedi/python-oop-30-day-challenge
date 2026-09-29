class MyMeta(type):
    def __new__(mcs, name, bases, namespace):
        print(f"Creating class: {name}")

        return super().__new__(mcs, name, bases, namespace)


class Student(metaclass=MyMeta):
    name = "Lipu"


student = Student()
print(student.name)