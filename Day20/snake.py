#The snake class
from turtle import Turtle
class Snake:
    def __init__(self):
        self.segments =[]
        x_val = 0
        for x in range(3):
            newturtle = Turtle("square")
            newturtle.color("white")
            newturtle.penup()
            # newturtle.shape("square")
            newturtle.goto(y=0,x=x_val)
            x_val-=20
            self.segments.append(newturtle)

    def move(self):
        for seg_num in range((len(self.segments))-1,0,-1):
            new_x = self.segments[seg_num-1].xcor()#second to last segment
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(x=new_x,y=new_y)#accessing the last element  in the list
        self.segments[0].forward(20)
        self.segments[0].left(90)