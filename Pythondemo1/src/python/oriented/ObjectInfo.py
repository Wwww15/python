import types
from Student import *

print(type(123))

print(isinstance(123, int))

print(abs)

print(int)

a = set()
print(type(a))

b = {}
print(type(b))


def testFun():
    print("hello,function")


print(type(testFun) == types.FunctionType)

print(dir(1))

print(dir("1"))

print("123".__len__())

studentA = Student("zhangsan", 10)
print(hasattr(studentA, 'name'))
print(hasattr(studentA, '__height'))
print(hasattr(studentA, '_Student__height'))
print(getattr(studentA, "name"))
print(setattr(studentA, "__weight", 180))
print(hasattr(studentA, "__weight"))
print(getattr(studentA, "__weight"))
print(studentA.__weight)
print(studentA._Student__height)
