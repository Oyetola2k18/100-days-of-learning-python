#Here we are learning about event listeners

#Event listeners are things that allow the turtle to respond to inputs like keystrokes etc

import turtle

tim = turtle.Turtle()
screen = turtle.Screen()


def moveforward():
    tim.forward(10)

#to make a screen listen to an event , you have to call the listen function with the screen object
screen.listen()

#now the screen is listening , now to handle what it is listening to 
#we use functions like "onkey()", takes in a function and a keybind

screen.onkey(key="space",fun=moveforward) #Here we passing a function as input
#when passing a function as input , we only pass in the name (without the brackets)
screen.exitonclick()

#also learnt about the concept of higher order functions
#this basically means a function that can work with other functions
