import functools

i = int('12345', base=8)
print(i)

int2 = functools.partial(int, base=2)

i = int2('11111111')
print(i)

max10 = functools.partial(max, 10)
maxNum = max10(1, 2, 3, 4, 5, 6, 7, 9)
print(maxNum)

