#code to draw dotted line

import turtle

zeph_the_tee = turtle.Turtle()

# zeph_the_tee.color('red')
# zeph_the_tee.forward(100)

for x in range(10):
    zeph_the_tee.pendown()
    zeph_the_tee.forward(10)
    zeph_the_tee.penup()
    zeph_the_tee.forward(10)

screen = turtle.Screen()
screen.exitonclick()