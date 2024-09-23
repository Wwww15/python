class Animal(object):
    pass


class FlyableMixIn(object):
    def fly(self):
        print('fly')


class RunnableMixIn(object):
    def run(self):
        print('run')


class Dog(Animal, RunnableMixIn):
    pass


class Bird(Animal, FlyableMixIn):
    pass


if __name__ == '__main__':
    dog = Dog()
    dog.run()
    bird = Bird()
    bird.fly()
