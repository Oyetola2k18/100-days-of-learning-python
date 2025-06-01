#implementing Random walk
import turtle
import random

zeph = turtle.Turtle()
turtle.colormode(255)
def gen_col():
    zeph.pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))

zeph.shape("turtle")
zeph.speed(9)
zeph.pensize(10)
heading = [0,90,180,270]
direct = ["left", "right"]
for x in range(500):
    gen_col()
    # another_dir = random.choice(direct)
    # if another_dir == "left":
    #     zeph.left(random.choice(heading))
    # elif another_dir == "right":
    #     zeph.right(random.choice(heading))
    #or use the setheading function
    zeph.forward(30)
    zeph.setheading(random.choice(heading))




screen = turtle.Screen()
screen.exitonclick()