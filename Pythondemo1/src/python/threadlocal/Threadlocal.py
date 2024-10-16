import threading


class Student(object):

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("name must be str")
        self.__name = value


local = threading.local()


def save_local(name):
    student = Student(name)
    local.student = student
    print("线程：%s，设置的名称：%s" % (threading.current_thread().name, name))


def get_local():
    name = local.student.name
    print("线程：%s，获取到的名称：%s" % (threading.current_thread().name, name))


def do_local_test(name):
    save_local(name)
    get_local()


if __name__ == '__main__':
    thread_one = threading.Thread(target=do_local_test, args=("张三",))
    thread_two = threading.Thread(target=do_local_test, args=("李四",))
    thread_one.start()
    thread_two.start()
    thread_one.join()
    thread_two.join()
    print("当前主线程结束")
