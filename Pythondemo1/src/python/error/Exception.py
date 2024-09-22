import traceback
def calaculate(arg1, arg2):
    add_res = add(arg1, arg2)
    decrease_res = decrease(arg1, arg2)
    power_res = power(arg1, arg2)
    divider_res = divider(arg1, arg2)
    print("加减乘除结果分别是：%.2f，%.2f，%.2f，%.2f" % (add_res, decrease_res, power_res, divider_res))


def power(arg1, arg2):
    return arg1 * arg2


def divider(arg1, arg2):
    return arg1 / arg2


def add(arg1, arg2):
    return arg1 + arg2


def decrease(arg1, arg2):
    return arg1 - arg2


if __name__ == '__main__':
    try:
        calaculate(0.01, 0.1)
    except Exception as e:
        #ranceback.print_exc()打印具体的错误信息
        traceback.print_exc()
        print(e)
        print(str(e))




from functools import reduce

def str2num(s):
    return int(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 76')
    print('99 + 88 + 76 =', r)

main()