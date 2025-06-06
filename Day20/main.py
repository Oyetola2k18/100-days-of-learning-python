#Creating the snake game

from turtle import Turtle, Screen
import time
import snake
import food
import scoreboard

screen = Screen()
screen.setup(height=600,width=600)
screen.bgcolor("black") #we use the bgcolor function to change the background color of our screen
#also to change the titile header of our screen we use the .title() function
screen.title("The Snake Game")
screen.tracer(0) #turn off screen animation
segments =[] 

game_is_on = True
snakY = snake.Snake()
snake_food = food.Food()

screen.listen()
screen.onkey(key="Up",fun=snakY.up)
screen.onkey(key="Down",fun=snakY.down)
screen.onkey(key="Left",fun=snakY.left)
screen.onkey(key="Right",fun=snakY.right)

scboard = scoreboard.Scoreboard()
#movement
while game_is_on:
    scboard.writing()
    screen.update()
    time.sleep(0.1)
    snakY.move()
    
    #detecting collision with the food
    #the distance fucntion return the distance between a turtle and a particular area on the screen
    if snakY.head.distance(snake_food) < 15:
        snake_food.refresh()
        scboard.update_score()
        snakY.extend()
    
    #detect collision with wall
    if snakY.head.xcor() > 290 or snakY.head.xcor() <-290 or snakY.head.ycor() >290 or snakY.head.ycor() <-290:
        game_is_on = False
        scboard.gameOver()
    
    #detect collision with snake body
    for segment in snakY.segments[1:]:
        # if segment == snakY.head:
        #     pass
        if snakY.head.distance(segment) < 10:
            game_is_on = False
            scboard.gameOver()

        
screen.exitonclick()