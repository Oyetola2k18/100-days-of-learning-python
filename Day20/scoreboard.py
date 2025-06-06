#scoreboard class
from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(y=260,x=0)
        self.color("white")
        
    
    def writing(self):
        self.write(f"Score:{self.score}",False,"center",font=('Courier',24,'normal'))

    def update_score(self):
        self.clear()
        self.score+=1
    
    def gameOver(self):
        self.goto(0,0)
        self.write("GAME OVER",False,"center",font=('Courier',24,'normal'))