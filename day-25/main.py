import turtle

import pandas

screen = turtle.Screen()
screen.title("U.S. STATES GAME")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data=pandas.read_csv("50_states.csv")
states=data.state.to_list()
guessed=[]

while len(guessed)<50:
    answer=screen.textinput(title="Guess the state",
                            prompt="What is another state's name?").title()
    
    if answer=="Exit":
        missing_states=[]
        for state in states:
            if state not in guessed:
                missing_states.append(state)
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer in states:
        guessed.append(answer)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer)


screen.exitonclick()
