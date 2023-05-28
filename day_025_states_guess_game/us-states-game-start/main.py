# This is a state guess game
# player inputs a state name, if guessed right, the name will be displayed on the map, if wrong, player can keep trying
# scores are tracked based on the number of guessed states
# input 'exit' to exit the game and see all the fifty states of the U.S.
# SKILLS: pandas, turtle, list comprehension

import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('U.S. States Game')

image = 'blank_states_img.gif'
screen.addshape(image)

turtle_0 = turtle.Turtle()
turtle_0.shape(image)

with open('50_states.csv', 'r') as file:
    states_df = pd.read_csv(file)
print(states_df)

all_states = states_df['state'].to_list()
# all_states = [state.lower() for state in all_states]
print(all_states)

states_guessed_n = 0
guessed_states = []
answer_state = ''
tt = turtle.Turtle()
tt.hideturtle()
tt.penup()
tt.speed(10)

# main loop
while not len(guessed_states) > 50:
    try:    # ask for guess input
        answer_state = screen.textinput(title=F'Guess a state {states_guessed_n}/50',
                                        prompt='What is another state in the U.S.?').capitalize()
        print(answer_state)
    except Exception as E:
        print(f'Error: {E}')

    # exit game
    if answer_state == 'Exit':
        break

    # right guess without duplicate
    if (answer_state in all_states) and (answer_state not in guessed_states):
        states_guessed_n += 1
        print('correct')
        print(f'score = {states_guessed_n}')

        # write down the name of the guessed state
        guessed_state_info_df = states_df[states_df.state == F'{answer_state}']
        tt.goto(int(guessed_state_info_df.x), int(guessed_state_info_df.y))
        tt.write(f'{answer_state}')

        guessed_states.append(answer_state)

# record all states that are not guessed
unguessed_states = [state for state in all_states if state not in guessed_states]
print(unguessed_states)

# display every state
for state_str in unguessed_states:
    unguessed_state_info_df = states_df[states_df.state == state_str]
    tt.goto(int(unguessed_state_info_df.x), int(unguessed_state_info_df.y))
    tt.write(state_str)

screen.mainloop()