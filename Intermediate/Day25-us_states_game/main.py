import pandas as pd
import turtle

us_image = 'blank_states_img.gif'
screen = turtle.Screen()
screen.title('U. S. States Game (22-07-24)')
screen.addshape(us_image) 

turtle.shape(us_image) 


# any click on the window prints the x & y coordinates on the console
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

# keeps the window open
# turtle.mainloop()

# my writer
tommy = turtle.Turtle()
tommy.hideturtle()

# read the .csv file
path = '50_states.csv'
df = pd.read_csv(path)
# print(df.head(3)) 

#      state    x    y
# 0  Alabama  139  -77
# 1   Alaska -204 -170
# 2  Arizona -203  -40


# states list
states = df['state'].to_list() 

score = 0

while score < 51:
    # user input
    answer = screen.textinput(title=f'{score}/50 States Correct', prompt="Give me the name of a US state?").strip().title()

    if answer == 'Exit':
        # print(states)
        break

    # checking if the user answer exists in the dataframe
    if answer in states:
        state_row = df[df['state'] == answer]
        # print(state_row) 
        #      state    x   y
        # 0  Alabama  139 -77

        # x_index = state_row['x'].index
        # print(x_index) #Index([0], dtype='int64')
        
        # x_coor = state_row['x'].values
        # print(x_coor) #[139]
        
        # taking the coordinates
        x_coor = state_row['x'].values[0]
        y_coor = state_row['y'].values[0]

        # writting the coordinates on the map 
        tommy.penup()  
        tommy.goto(x = x_coor, y = y_coor)
        tommy.write(answer)

        score += 1

        states.remove(answer)
    else:
        continue

 
# first: convert my list into a dataframe or series
df_missing_states = pd.DataFrame(states)
# print(df_missing_states.head())

# second: exporting the .csv file
df_missing_states.to_csv('user_missing_states.csv')



















    























