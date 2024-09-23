class Person(object):
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if type(value) != str:
            raise ValueError("name must be str")
        self.__name = value


if __name__ == "__main__":
    person = Person()
    person.name = "10"
    print(person.name)


class Screen(object):

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def resolution(self):
        return self.__height * self.__width


# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
