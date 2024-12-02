import random
import turtle


def draw_flower(t, x, y, petal_color, center_color):
    """绘制单朵花"""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(petal_color)

    # 绘制花瓣
    t.begin_fill()
    for _ in range(6):  # 六片花瓣
        t.circle(20, 60)  # 半径20，弧度60度
        t.left(120)
        t.circle(20, 60)
        t.left(60)
    t.end_fill()

    # 绘制花心
    t.penup()
    t.goto(x, y - 10)
    t.pendown()
    t.color(center_color)
    t.begin_fill()
    t.circle(10)
    t.end_fill()


def draw_stem(t, x, y, length, color="green"):
    """绘制花茎"""
    t.penup()
    t.goto(x, y - 20)
    t.setheading(-90)  # 设置方向向下
    t.pendown()
    t.color(color)
    t.pensize(3)
    t.forward(length)


def draw_flower_bouquet():
    """绘制一束花"""
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("A Bouquet of Flowers")

    t = turtle.Turtle()
    t.speed(10)

    # 随机绘制花朵
    for _ in range(5):  # 5 朵花
        x = random.randint(-200, 200)
        y = random.randint(0, 200)
        petal_color = random.choice(["red", "purple", "blue", "orange", "pink"])
        center_color = "yellow"

        draw_flower(t, x, y, petal_color, center_color)
        draw_stem(t, x, y, random.randint(100, 200))

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    draw_flower_bouquet()