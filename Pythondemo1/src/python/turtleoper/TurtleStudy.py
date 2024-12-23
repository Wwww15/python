from turtle import *


def draw_square():
    width(4)

    # 前进:
    forward(200)
    # 右转90度:
    right(90)

    # 笔刷颜色:
    pencolor('red')
    forward(100)
    right(90)

    pencolor('green')
    forward(200)
    right(90)

    pencolor('blue')
    forward(100)
    right(90)

    # 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
    done()


def draw_circle():
    width(10)
    pencolor("blue")

    circle(100)

    done()


def draw_star_item(x, y):
    pu()
    goto(x, y)
    pd()
    # set heading: 0
    seth(0)
    for i in range(5):
        fd(40)
        rt(144)


def draw_star():
    for x in range(0, 250, 50):
        draw_star_item(x, 0)

    done()


if __name__ == "__main__":
    # draw_square()
    # draw_circle()
    draw_star()
