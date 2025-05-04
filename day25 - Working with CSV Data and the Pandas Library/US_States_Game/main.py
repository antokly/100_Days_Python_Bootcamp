# Check if the answer_state match with one of the states in the list of 50_states.csv
# The program should work with all of these cases : ex: Ohio OR ohio
# if the written state match with one of these states, the state should be written in the map at the appropriate location
# if the written state doesn't match with one of these states : nothing happen and pop up asking for a new input
# in the title of the pop up keep in track correct states number : ex: 4/50 States Correct (and everytime we find a new state, this number update)

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor) # listener
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

correct_cnt = 0

while correct_cnt != len(data["state"]):

    answer_state = screen.textinput(title="Guess the State",
                                    prompt=f"{correct_cnt} / {len(data["state"])} What's another state's name ?").title()

    if answer_state == "exit":
        missing_states = []
        for state in all_states:
            if state not in all_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break

    # Check if the answer matches any state
    if answer_state in data.state.values:
        correct_cnt += 1
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        state_x = int(state_data["x"])
        state_y = int(state_data["y"])

        # Create a turtle to write the state name
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        writer.goto(state_x, state_y)
        writer.write(answer_state, align="center", font=("Arial", 8, "normal"))
    else:
        continue

