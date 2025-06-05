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
    time.sleep(0.1)
    screen.listen()
    screen.onkey(key="Up",fun=snakY.up)
    screen.onkey(key="Down",fun=snakY.down)
    screen.onkey(key="Left",fun=snakY.left)
    screen.onkey(key="Right",fun=snakY.right)
    snakY.move()

screen.exitonclick()