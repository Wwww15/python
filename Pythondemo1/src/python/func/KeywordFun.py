def person(name, age, **other):
    print('name:', name)
    print('age:', age)
    other['college'] = '西南交大'
    print('other:', other)


def personTwo(name, age, *, height, city):
    print('name:', name)
    print('age:', age)
    print('height:', height)
    print('height:', city)


def personThree(name, age, *likes, height, city):
    print('name:', name)
    print('age:', age)
    print('likes:', likes)
    print('height:', height)
    print('city:', city)
