from turtle import Screen,Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import random,time

game_screen=Screen()
game_screen.setup(width=600,height=600)
game_screen.bgcolor('black')
game_screen.title('Snake Game')
game_screen.tracer(0)
game_screen.listen()

snake=Snake()
food=Food()
game_score=Scoreboard()
game_screen.onkey(snake.move_up,'Up')
game_screen.onkey(snake.move_down,'Down')
game_screen.onkey(snake.move_left,'Left')
game_screen.onkey(snake.move_right,'Right')
is_game_on=True
while is_game_on:
    time.sleep(0.1)
    game_screen.update()
    snake.move_snake()
    if snake.Segments[0].xcor()>290 or snake.Segments[0].xcor()<-290 or snake.Segments[0].ycor()>290 or snake.Segments[0].ycor()<-290:
        
        game_score.reset_scorecard()
        snake.hide_old_snake()
        snake.move_snake()
    if food.distance(snake.Segments[0])<20:
        food.create_food()
        game_score.increase_score()
        game_score.increase_speed()
        snake.extend_snake()
    
    for segment in snake.Segments[1:]:
        if snake.head.distance(segment)<10:
            game_score.reset_scorecard()
            snake.hide_old_snake()
            snake.move_snake()
game_screen.exitonclick()