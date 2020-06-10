import math
import turtle

t = turtle.Turtle()


# 编写一个函数名为square，参数t。画一个四边形。

def square(sq: turtle.Turtle, length: int):
    for i in range(4):
        sq.fd(length)
        sq.lt(90)  # 90°


def polygon(po: turtle.Turtle, length: int, n: int):
    angle = 360 / n
    polyline(po, n, length, angle)


def circle(ci, r):
    arc(ci, r, 360)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    polyline(t, n, step_length, step_angle)


def polyline(t, n, length, angle):
    """
    Draws n line segments with the given length and angle (in degrees) between them. t is a turtle.
    :param t:
    :param n:
    :param length:
    :param angle:
    :return:
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)


arc(t, 100, 360)

turtle.mainloop()
