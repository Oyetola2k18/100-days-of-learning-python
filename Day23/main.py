import time
from turtle import Screen
from player import *
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

car_m = CarManager()
score_bd = Scoreboard()

screen.listen()
screen.onkey(key="Up",fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_m.create_car()
    car_m.move()

    
    #detect collision with car
    for car in car_m.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score_bd.game_over()
    
    #detect when player gets to the Finish line
    if player.ycor() >= 290:
        player.goto(STARTING_POSITION)
        car_m.increase_speed()
        score_bd.levelup()
    
        
screen.exitonclick()