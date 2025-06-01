#creating a spirograph
import turtle
import random
zeph = turtle.Turtle()
zeph.speed("fastest")

turtle.colormode(255)
def gen_col():
    zeph.pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))

#basically how i got the value in my range is 360 divided by the number of times i shift(5)
for _ in range(72):
    gen_col()
    zeph.circle(100)
    zeph.left(5)



screen = turtle.Screen()
screen.exitonclick()