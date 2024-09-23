class Student(object):

    def __init__(self,name):
        self.__name = name

    def __str__(self):
        return 'Student(name=%s)' % self.__name

    def __getattr__(self, item):
        if item == 'age':
            return  11
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % item)

    def __call__(self, *args, **kwargs):
        print("current name is %s" % self.__name)

    __repr__ = __str__

if __name__ == '__main__':
    student = Student("张三")
    print(student)
    print(student.age)
    # print(student.sex)
    student()
    print(callable(student))
    print(callable("123"))
