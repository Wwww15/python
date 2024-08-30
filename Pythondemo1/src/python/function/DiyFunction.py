from AbsFun import absFun
from DefaultFun import power
from DefaultFun import regisStu
from KeywordFun import person
from KeywordFun import personTwo
from KeywordFun import personThree
from SumAndMulti import sumAndMulti
from VariableParam import sumCalc
from Recursion import factorial

print(absFun(1))

print(sumAndMulti(-1, 2))

print(power(2, 3))

regisStu('张三', '男', location='成都', age=30)

print(sumCalc(*[1, 3]))
print(sumCalc())

person('王麻子', 13, height='182cm', weight='190斤')
person('张四', 20)
extra = {'location': '湖南长沙沙坪坝', 'college': '山西农大', 'id-card': 198776554211}
person('老六', 40, **extra)
print(extra)

extraTwo = {'height': 170, 'city': '成都'}
personTwo('老三', 70, **extraTwo)
# personTwo('老三', 70)

likes = ('排球', '篮球', '乒乓球')
personThree('可变人名', 1200, *likes, height=190, city='大上海')


def mul(*nums):
    if nums is None or len(nums) < 1:
        raise TypeError('请至少传入一个数')
    result = 1
    for item in nums:
        result *= item
    return result


# 测试
print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('mul(5)测试失败!')
elif mul(5, 6) != 30:
    print('mul(5, 6)测试失败!')
elif mul(5, 6, 7) != 210:
    print('mul(5, 6, 7)测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('mul(5, 6, 7, 9)测试失败!')
else:
    try:
        mul()
        print('mul()测试失败!')
    except TypeError:
        print('测试成功!')


print(factorial(10))

