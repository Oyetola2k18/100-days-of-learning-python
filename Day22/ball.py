#my ball class
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.x_move = 10 #rate of movement 
        self.y_move = 10 #rate of movement
        self.move_speed = 0.1


    def move(self):
        new_x = self.xcor() +self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x,y=new_y)
    
    def bounce_y(self):
        self.y_move = self.y_move * -1

    def bounce_x(self):
        self.x_move = self.x_move * -1
        if self.move_speed > 0:
            self.move_speed *= 0.9
        else:
            pass
    
    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()