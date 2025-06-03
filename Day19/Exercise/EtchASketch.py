#Building an etch a sketch app
import turtle

zeph = turtle.Turtle()
screen = turtle.Screen()

#function declarations to perform movements
def move_fd():
    zeph.forward(10)

def move_bd():
    zeph.backward(10)

def move_left():
    # zeph.left(30)
    new_heading = zeph.heading()+10
    zeph.setheading(new_heading)

def move_right():
    # zeph.right(30)
    new_heading = zeph.heading()-10
    zeph.setheading(new_heading)

def end():
    zeph.clear()
    zeph.penup()
    zeph.home()
    zeph.pendown()

screen.listen()
#key bindings
screen.onkey(fun=move_fd,key="w")
screen.onkey(fun=move_bd, key="s")
screen.onkey(fun=move_left, key="a")
screen.onkey(fun=move_right, key="d")
screen.onkey(key="c",fun=end)

screen.exitonclick()