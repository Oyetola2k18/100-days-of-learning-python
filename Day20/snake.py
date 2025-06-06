#The snake class
from turtle import Turtle
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
UP= 90
LEFT =180
RIGHT = 0
DOWN =270
class Snake:
    #once initiated ,it creates list of turtles to start the game

    def __init__(self):
        self.segments =[]
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segments(position)

    def add_segments(self,position):
        newturtle = Turtle("square")
        newturtle.color("white")
        newturtle.penup()
        # newturtle.shape("square")
        newturtle.goto(position)
        self.segments.append(newturtle) 
    
    def extend(self):
        self.add_segments(self.segments[-1].position())

    def move(self):
        for seg_num in range((len(self.segments))-1,0,-1):
            new_x = self.segments[seg_num-1].xcor()#second to last segment
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(x=new_x,y=new_y)#accessing the last element  in the list
        # self.segments[0].left(90)
        self.segments[0].forward(20)
    
    

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        else:
            pass

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN) 
        else:
            pass
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        else:
            pass

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        