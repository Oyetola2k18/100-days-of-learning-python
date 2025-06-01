#Drawing a square using turtle
import turtle


moses_the_bot  = turtle.Turtle()

for x in range(4):
    moses_the_bot.forward(100)
    moses_the_bot.left(90)

screen = turtle.Screen()
screen.exitonclick()