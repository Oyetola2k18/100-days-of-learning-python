#Learning more on how the the turtle library works

import turtle
#imported the Turtle and the Screen Class
zeph_the_turtle = turtle.Turtle()


turtle.colormode(255)
zeph_the_turtle.shape("turtle")
zeph_the_turtle.color("midnight blue")
# zeph_the_turtle.pencolor(83,58,27)

zeph_the_turtle.forward(100)
zeph_the_turtle.left(270)



screen = turtle.Screen()
screen.exitonclick()