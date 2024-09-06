# 平方
def power(m, n=2):
    multi = 1;
    while n > 0:
        multi *= m
        n -= 1
    return multi


# 注册学籍信息
def regisStu(name, sex, age=7, location='长沙'):
    print("姓名：", name)
    print("性别：", sex)
    print("年龄：", age)
    print("地址：", location)
