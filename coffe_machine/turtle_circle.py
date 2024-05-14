import random
import turtle

from turtle import Turtle
turtle.colormode(255)

def random_colors():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    mycolor=(r,g,b)
    return mycolor
def draw_circles(position_change):
    for _ in range(int(360/position_change)):
        timmy.color(random_colors())
        timmy.circle(100)
        timmy.setheading(timmy.heading()+position_change)


timmy=Turtle()
timmy.speed('fastest')
draw_circles(5)


my_screen=turtle.Screen()


my_screen.exitonclick()
