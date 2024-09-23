from enum import Enum, unique


@unique
class Sex(Enum):
    MAN = 1
    WOMAN = 2


if __name__ == '__main__':
    print(Sex.__members__.values())
    print(Sex["MAN"].value)


class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
