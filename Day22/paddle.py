#my paddle class
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,location_tuple):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.color("white")
        self.penup()
        self.teleport(x=location_tuple[0], y= location_tuple[1])

    # right_paddle.setheading(90)
    # right_paddle.shapesize(stretch_len=5,stretch_wid=1)
   
    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)
        # screen.update()

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)
        # screen.update()