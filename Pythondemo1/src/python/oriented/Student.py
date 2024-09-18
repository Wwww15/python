class Student(object):
    def __init__(self, name, age, *, height=18):
        self.name = name
        self.age = age
        self.__height = height

    def print_info(self):
        s = "name:%s,age:%d" % (self.name, self.age)
        print(s)


if __name__ == '__main__':
    studentA = Student('zhangsan', 18)
    studentB = Student('lisi', 80)
    studentA.print_info()
    studentB.print_info()

    studentA.location = '成都高新区'
    print(studentA.location)
