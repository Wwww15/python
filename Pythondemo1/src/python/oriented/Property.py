class Person():
    name = 'Person'
    age = 18
    __sex = "男"
    _height = 190


class Child(Person):
    pass


person = Person()

print(person.name)
setattr(person, "name", "zhangsan")
print(getattr(person, "name"))
del person.name
print(person.name)

child = Child()
print(child.name)
print(hasattr(child, "age"))
print(getattr(child, "age"))
print(hasattr(child, "__sex"))
print(hasattr(child, "_height"))
print(getattr(child, "_height"))


class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1


# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')
