list = [1, 2, 3, 4, 5, 6]
list1 = [str(x) + ',' + str(x + 1) for x in list]
print(list1)

d = {'x': 'A', 'y': 'B', 'z': 'C'}
dict = [k + '=' + v for k, v in d.items()]
print(dict)

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x, str)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
