from collections.abc import Iterable

print(isinstance(123, Iterable))
print(isinstance((1,), Iterable))
print(isinstance({1: 1}, Iterable))

likes = ['篮球', '排球', '网球']
extra = {'height': 190, 'weight': 180}

for i, item in enumerate(likes):
    print(i, item)

for k, v in extra.items():
    print(k, v)


def findMinAndMax(L):
    min = None
    max = None
    for item in L:
        if min is None or item < min :
            min = item
        if max is None or item > max :
            max = item
    return (min, max)


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
