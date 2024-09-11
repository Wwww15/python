class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def set_gender(self, gender):
        self.__gender = gender


# 测试:
if __name__ == '__main__':
    bart = Student('Bart', 'male')
    if bart.get_gender() != 'male':
        print('测试失败!')
    else:
        bart.set_gender('female')
        if bart.get_gender() != 'female':
            print('测试失败!')
        else:
            print('测试成功!')

    # 测试私有属性的赋值
    print(bart.get_name())
    bart.__name = '张三'
    print(bart._Student__name)
    print(bart.__name)
