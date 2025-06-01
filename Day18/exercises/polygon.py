#draw all polygons up to decagon
import turtle
import random
zeph = turtle.Turtle()

def move():
    zeph.forward(100)

turtle.colormode(255)

def gen_col():
    zeph.pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))

gen_col()
for x in range(3):
    zeph.right(120)
    move()

gen_col()
for  x in range(4):
    zeph.right(90)
    move()

gen_col()
for x in range(5):
    zeph.right(360/5)
    move()

gen_col()
for x in range(6):
    zeph.right(360/6)
    move()

gen_col()
for x in range(7):
    zeph.right(360/7)
    move()

gen_col()
for x in range(8):
    zeph.right(360/8)
    move()

gen_col()
for x in range(9):
    zeph.right(360/9)
    move()

gen_col()
for x in range(10):
    zeph.right(360/10)
    move()

#using angela's approach
# def calc(num_of_sides):
#     gen_col()
#     angle = 360/num_of_sides
#     for x in range(num_of_sides):
#         zeph.right(angle)
#         zeph.forward(100)

# for shapes in range(3,11):
#     calc(shapes)

screen = turtle.Screen()
screen.exitonclick()