import turtle
my_screen =  turtle.Screen()

pen = turtle.Turtle()
pen.penup()
pen.hideturtle()


my_screen.title('U.S. States Game')
image = 'blank_states_img.gif'
my_screen.addshape(image)
turtle.shape(image)


# read from the csv file using pandas
# tap into the series of the file and store the x and y colums of the answer text
# make sure that the text is case-insensitive
# check the user's guess against the file's state name columns
# make the answer text goto the position of the x and y coordinate on the map
# a way to keep prompting the user for a guess
# keep track of states guessed

import pandas
data_file = pandas.read_csv('./50_states.csv')


guessing = True
all_states = data_file['state'].to_list()
total_guessed = []
while guessing:

    answer = my_screen.textinput(title=f'{len(total_guessed)}/ {len(data_file['state'])} States guessed', prompt="What's another state name?").title()

    state_exist  = (data_file['state'] == answer).any()

    if answer == 'Exit':
        missing_states = [state for state in all_states  if state not in total_guessed]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        guessing = False


    if state_exist:
        state_row = data_file[data_file['state'] == answer]
        state_x = state_row.x
        state_y = state_row.y

        #move the pen to the x and y position
        if answer not in total_guessed:
            pen.goto(state_x.item(), state_y.item())
            total_guessed.append(answer)


        #write the text at the specified location
        pen.write(answer, align='left', font=('Arial', 8, 'normal'))

    if len(total_guessed) == len(data_file['state']):
        guessing = False

# states_to_learn.csv









