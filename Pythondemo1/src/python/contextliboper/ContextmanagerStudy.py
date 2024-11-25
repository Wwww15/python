from contextlib import contextmanager


class User(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print("__enter__")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print("error")
        else:
            print("exit")

    def query(self):
        print("Current name is %s" % self.name)


@contextmanager
def create_query(name):
    print("create_query enter")
    user = User(name)
    yield user
    print("create_query exit")


def decorate_method(param):
    print("param %s start" % param)
    yield
    print("param %s end" % param)


if __name__ == "__main__":
    # with User("Jack") as u:
    #     u.query()
    with create_query("zhangsan") as u:
        u.query()
