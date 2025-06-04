#Creating the snake game

from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(height=600,width=600)

screen.bgcolor("black") #we use the bgcolor function to change the background color of our screen

#also to change the titile header of our screen we use the .title() function
screen.title("The Snake Game")
x_val =0
screen.tracer(0)
segments =[] 
screen.numinput("Poker", "Your stakes:", 1000, minval=10, maxval=10000)
for x in range(3):
    newturtle = Turtle("square")
    newturtle.color("white")
    newturtle.penup()
    # newturtle.shape("square")
    newturtle.goto(y=0,x=x_val)
    x_val-=20
    segments.append(newturtle)
    
screen.update()
game_is_on = True

while game_is_on:
    for seg in segments:
        seg.forward(20)
screen.exitonclick()