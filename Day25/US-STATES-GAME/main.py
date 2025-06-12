#creating the US states guessing game

import turtle



screen = turtle.Screen()

screen.title("US STATES GUESSING GAME")



#turtle has a function that allows us to load in a shape
image = "Day25/US-STATES-GAME/blank_states_img.gif"
screen.addshape(image)

# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)
turtle.shape(image)

screen.mainloop()