class Person(object):

    def sayHello(self):
        print("hello Person")


class Child(Person):

    def sayHello(self):
        print("hello,I amd  child")


class OldMan(Person):

    def sayHello(self):
        print("hello,I am old man")


class Ox(object):

    def sayHello(self):
        print("hello,I am ox")


def communicate(person):
    print("Hello,I amd alien,Who are you?")
    person.sayHello()


if __name__ == "__main__":
    oldMan = OldMan()
    child = Child()
    communicate(oldMan)
    print(isinstance(oldMan, Person))
    print(isinstance('1', Person))

    ox = Ox()
    communicate(ox)
    print(isinstance(ox, Person))
