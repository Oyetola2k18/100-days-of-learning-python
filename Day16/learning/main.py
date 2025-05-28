#Turtle

import turtle
timmy = turtle.Turtle()
#here we just created a new turtle object from the turtle module

#when we talk about object attributes (it means what the object Has (its properties)) 
timmy.shape("turtle")
timmy.color("red")
timmy.forward(100)
my_screen = turtle.Screen()

print(my_screen.canvheight)

#the things an object does, also known as the Methods(functions in classes)

my_screen.exitonclick()#this function allows our screen to stay until we click(then it exits the code)