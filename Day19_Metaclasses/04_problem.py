class RequireNameMeta(type):
    def __new__(mcs, name, bases, namespace):

        if name != "Base" and "name" not in namespace:
            raise TypeError(
                f"{name} must have a 'name' attribute"
            )

        return super().__new__(mcs, name, bases, namespace)


class Base(metaclass=RequireNameMeta):
    pass


class Student(Base):
    name = "Lipu"


student = Student()

print(student.name)