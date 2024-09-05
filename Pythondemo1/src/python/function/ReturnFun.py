def lazy_sum(*nums):
    def sum():
        total = 0
        for item in nums:
            total += item
        return total

    return sum


f = lazy_sum(1, 2, 3, 4, 5, 6)
print(f())


def count():
    fs = []
    for i in range(1, 4):
        def f(i):
            return i * i

        fs.append(f(i))
    return fs


f1, f2, f3 = count()
print(f1)
print(f2)
print(f3)


def inc():
    x = 0

    def fn():
        nonlocal x
        x = x + 1
        return x

    return fn


f = inc()
print(f())  # 1
print(f())  # 2


def createCounter():
    decrease = 0

    def counter():
        nonlocal decrease
        decrease += 1
        return decrease

    return counter


# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
