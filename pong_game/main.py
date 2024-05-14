from turtle import Turtle,Screen
import time
from paddle import Paddle 
from ball import Ball
from scoreboard import Scoreboard
myScreen=Screen()
myScreen.setup(width=800,height=600)
myScreen.bgcolor('black')
myScreen.tracer(0)

r_paddle=Paddle((370,0))
l_paddle=Paddle((-370,0))
game_ball=Ball()
score_board=Scoreboard()


myScreen.listen()
myScreen.onkey(r_paddle.move_up,'Up')
myScreen.onkey(r_paddle.move_down,'Down')
myScreen.onkey(l_paddle.move_up,'w')
myScreen.onkey(l_paddle.move_down,'s')

is_game_on=True
while is_game_on:
    time.sleep(game_ball.ball_speed)
    myScreen.update()
    game_ball.move_ball()
    if game_ball.ycor()>280 or game_ball.ycor()<-280:
        game_ball.y_bounce_back()
    if game_ball.distance(r_paddle)<50 and game_ball.xcor()>340 or game_ball.distance(l_paddle)<50 and game_ball.xcor()<-340:
        game_ball.x_bounce_back()
    
    if game_ball.xcor()>380:
        score_board.l_point()
        game_ball.reset_position()
        
    if game_ball.xcor()<-380:
        score_board.r_point()
        game_ball.reset_position()

myScreen.exitonclick()