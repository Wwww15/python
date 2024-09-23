class Student(object):

    def study(self, subject):
        print("学生正在学习 %s" % subject)


def workFn(self, subject):
    print("学生正在写 %s 作业" % subject)


class ListMetaClass(type):

    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, item: self.append(item)
        return type.__new__(cls, name, bases, attrs)

class TestList(list,metaclass=ListMetaClass):
    pass

if __name__ == '__main__':
    student = Student()
    student.study("数学")
    print(type(Student))
    print(type(student))

    Student = type("Student", (object,), dict(work=workFn))
    studentA = Student()
    studentA.work("语文")

    test_list = TestList()
    test_list.add(1)
    print(test_list)

