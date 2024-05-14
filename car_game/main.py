import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
cars_manager=CarManager()
player_score=Scoreboard()
screen.listen()
screen.onkey(player.move_up,'Up')
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars_manager.create_car()
    cars_manager.move_cars()
    for cars in cars_manager.all_cars:
        if cars.distance(player)<20:
            game_is_on=False
            player_score.game_over()
    if player.check_player_at_finish():
        player.player_at_start()
        player_score.update_level()


screen.exitonclick()