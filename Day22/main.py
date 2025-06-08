#creating the famous pong game
import turtle

screen = turtle.Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game")

#stretch_wid =20 * how tall
#stretch_len = 20 * how wide
screen.tracer(0)
def up():
    new_y = right_paddle.ycor() + 20
    right_paddle.goto(right_paddle.xcor(),new_y)
    # screen.update()

def down():
    new_y = right_paddle.ycor() - 20
    right_paddle.goto(right_paddle.xcor(),new_y)
    # screen.update()

right_paddle = turtle.Turtle("square")
# right_paddle.setheading(90)
# right_paddle.shapesize(stretch_len=5,stretch_wid=1)
right_paddle.shapesize(stretch_len=1,stretch_wid=5)
right_paddle.color("white")
right_paddle.penup()
right_paddle.goto(x=350,y=0)
# screen.update()

screen.listen()
screen.onkey(key="Up",fun=up)
screen.onkey(key="Down",fun=down)

game_is_on = True
while game_is_on:
    screen.update()
screen.exitonclick()