import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

player=Player()
car= CarManager()
score= Scoreboard()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(player.move,"Up")



game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    car.create()
    car.move_cars()

    #Detect collision
    for i in car.all_cars:
        if i.distance(player)<20:
            car.game_over()
            game_on=False
    # Detect wall collison
    if player.finish():
        player.reset()
        car.level_up()
        score.increase_level()

screen.exitonclick()