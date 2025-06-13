#creating the US states guessing game
import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("US STATES GUESSING GAME")

#turtle has a function that allows us to load in a shape
image = "Day25/US-STATES-GAME/blank_states_img.gif"
screen.addshape(image)
screen.setup(width=720,height=520)
#code used to get different points on the map mapped to their location on the map
# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)

turtle.shape(image)
 
location  = "Day25/US-STATES-GAME/50-USA-STATES.csv"
data = pd.read_csv(location)

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

data_to_list = data["state"].to_list()
num_of_questions_done = 0
answer_state = (screen.textinput(title="Guess the state", prompt="What's another state's name?")).title()
game_is_on = True
guessed_states = []
while game_is_on:
    if len(guessed_states) == 50:
        game_is_on = False

    if answer_state == "Exit":
        break

    if answer_state not in guessed_states:
        if answer_state in data_to_list:
            state_row= data[data.state == answer_state]
            x_cord = float(state_row['x'])
            y_cord = float(state_row["y"])
            writer.teleport(x=x_cord,y=y_cord)
            writer.color("black")
            writer.write(f"{answer_state}",False,align="center",font=("Courier", 14, "normal"))
            num_of_questions_done +=1
            guessed_states.append(answer_state)

    answer_state = (screen.textinput(title=f"Guessed {num_of_questions_done}/{len(data_to_list)}", prompt="What's another state's name?")).title()

uncheck_lists =[]
for state in data_to_list:
    if state not in guessed_states:
        uncheck_lists.append(state)
    else:
        pass

uncheck_lists_dict ={
    "List of states you missed": uncheck_lists,
}
states_to_learn = pd.DataFrame(uncheck_lists_dict)

states_to_learn.to_csv("Day25/US-STATES-GAME/states_to_learn.csv")