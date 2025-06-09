COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random
class CarManager:
    def __init__(self):
        super().__init__()
        self.all_cars =[]
        self.movement_speed = 0


    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len= 2, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_y = random.randint(-250,250)
            new_car.goto(300,new_y)
            self.all_cars.append(new_car)
        
    
    def move(self):
       for car in self.all_cars:
           car.backward(STARTING_MOVE_DISTANCE + self.movement_speed)

    def increase_speed(self):
        self.movement_speed += MOVE_INCREMENT