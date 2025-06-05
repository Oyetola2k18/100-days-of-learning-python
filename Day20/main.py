#Creating the snake game

from turtle import Turtle, Screen
import time
import snake


screen = Screen()
screen.setup(height=600,width=600)
screen.bgcolor("black") #we use the bgcolor function to change the background color of our screen
#also to change the titile header of our screen we use the .title() function
screen.title("The Snake Game")
screen.tracer(0) #turn off screen animation
segments =[] 

game_is_on = True
snakY = snake.Snake()
#movement
while game_is_on:
    screen.update()
    time.sleep(1)
    
    snakY.move()

screen.exitonclick()