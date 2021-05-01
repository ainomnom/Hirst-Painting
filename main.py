from colorgram import extract
from random import choice
from turtle import Turtle, Screen


def generate_colors(number_of_colors):
    extracted_colors = extract("image.jpg", number_of_colors)
    list_of_colors = []
    for color in extracted_colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        list_of_colors.append((r, g, b))
    return list_of_colors


def draw_dot():
    for j in range(9):
        painter.dot(20, choice(colors))
        painter.forward(50)
    painter.dot(20, choice(colors))


def move_up():
    painter.setheading(90)
    painter.forward(50)
    painter.setx(x)
    painter.setheading(0)


colors = generate_colors(20)
colors.remove(colors[0])

painter = Turtle()
screen = Screen()

screen.colormode(255)
painter.hideturtle()

painter.penup()
x = -235
y = -215
painter.setposition(x, y)

for i in range(10):
    draw_dot()
    move_up()

screen.exitonclick()