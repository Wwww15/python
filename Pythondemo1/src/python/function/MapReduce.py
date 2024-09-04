def normalize(name):
    return name[:1].upper() + name[1:].lower()


# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

from functools import reduce


def prod(L):
    def cj(a, b):
        return a * b

    return reduce(cj, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


def str2float(s):
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    def char2num(s):
        return DIGITS[s]

    def float(a, b):
        return a * 0.1 + b

    def int(a, b):
        return a * 10 + b

    index = s.index('.')
    return reduce(int, map(char2num, s[:index])) + reduce(float, map(char2num, reversed(s[index + 1:])))/10


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
