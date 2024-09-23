import logging

logging.basicConfig(level=logging.DEBUG)


def devider(num1, num2):
    assert num2 and num2 != 0, '被除数不能为 0'
    return num1 / num2


def devider1(num1, num2):
    logging.debug("被除数为 %d" % num2)
    return num1 / num2


if __name__ == '__main__':
    # devider(1, 0)
    devider1(1, 0)
