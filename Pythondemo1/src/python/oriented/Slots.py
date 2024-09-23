from types import MethodType


class Student(object):
    pass


def set_name(self, name):
    self.name = name


class Person(object):
    __slots__ = ('name', 'age')


if __name__ == "__main__":
    student = Student()
    student.set_name = MethodType(set_name, student)
    student.set_name("zhangsan")
    print(student.name)

    # studentA = Student()
    # studentA.set_name("lisi")
    # print(studentA.name)
    Student.set_name = set_name
    studentA = Student()
    studentA.set_name("lisi")
    print(studentA.name)

    person = Person()
    person.name = '测试a'
    person.age = "10"
