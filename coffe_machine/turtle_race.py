from turtle import Turtle,Screen
import random



turtles=[]
game_on=False
colors=['red','green','yellow','blue','orange','purple','black']
y_axis=[-100,-70,-40,-10,20,50]
my_screen=Screen()
my_screen.setup(width=500,height=400)
user_choice=my_screen.textinput('Make your bit','Who will win, Enter color')
if user_choice:
    game_on=True
for indexes in range(0,6):
    tim=Turtle(shape='turtle')
    tim.color(colors[indexes])
    tim.penup()
    tim.goto(x=-230,y=y_axis[indexes])
    turtles.append(tim)
while game_on:
    for turtle in turtles:
        if turtle.xcor()>230:
            game_on=False
            winning_turtle=turtle.pencolor()
            if winning_turtle==user_choice:
                print(f'You have won! The {winning_turtle} Turtle is the Winner.')
            else:
                print(f'You have Lost! The {winning_turtle} Turtle is the Winner.')
        turtle.forward(random.randint(0,10))
my_screen.exitonclick()