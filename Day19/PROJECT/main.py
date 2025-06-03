#TUrtle race game

import turtle
import random

screen = turtle.Screen()
is_race_on = False
#cuz we dont want to use the default screen height and width, we use the setup function to change it
screen.setup(width=500,height=400)

#also to get user input on the  screen we use screen.text input, if its a number , then screen.numINput
user_bet = screen.textinput(title="Make your Bet", prompt="Which TUrtle will win the race? Enter a color: ")
print(user_bet)
color = ["red", "orange", "yellow", "green", "blue", "purple"]

y_val = -100
all_turtles =[]
for x in range(0,6):
    new_turtle = turtle.Turtle()
    new_turtle.penup()
    new_turtle.color(color[x])
    new_turtle.shape(name="turtle")
    #height/2 = 200 , width / 2= 250
    new_turtle.goto(x=-230,y=y_val)
    y_val+=30
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on=True

while is_race_on:

    for turtle in all_turtles:
        #xcor means xcordinate
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner")
            else:
                print(f"You have lost! The {winning_color} turtle is the winner")
            
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick() 