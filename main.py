import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("US States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pd.read_csv("50_states.csv")
list_of_states = states_data.state.to_list()
x = states_data.x.to_list()
y = states_data.y.to_list()


score = 0
guessed_states = []

while score < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's a state name?").title()

    if answer_state == "Exit":
        states_to_learn = [state for state in list_of_states if state not in guessed_states]
        # Refactored from below to use list comprehension:
        # for state in list_of_states:
        #     if state not in guessed_states:
        #         states_to_learn.append(state)
        s = pd.Series(states_to_learn)
        s.to_csv("states_to_learn.csv")
        break
    if answer_state not in guessed_states:
        if answer_state in list_of_states:
            state_title = turtle.Turtle()
            state_title.hideturtle()
            state_title.penup()
            i = list_of_states.index(f"{answer_state}")
            state_x = x[i]
            state_y = y[i]
            # state_data = states_data[states_data.state == answer_state]
            # state_title.goto(int(state_data.x), int(state_data.y))
            state_title.goto(state_x, state_y)
            state_title.write(answer_state)
            score += 1
            guessed_states.append(answer_state)
    else:
        answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="You guessed that state already. "
                                                                                   "What's another state?").title()

