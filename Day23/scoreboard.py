FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.color("black")
        self.penup()
        self.level = 0
        self.goto(y=250, x = -280)
        self.update_level()
        
    
    def update_level(self):
        self.clear()
        self.write(f"Level:{self.level}", False,align="left", font=FONT)

    def levelup(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", False,align="Center", font=FONT)