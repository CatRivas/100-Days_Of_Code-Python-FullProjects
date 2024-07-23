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

# mi escritor
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

# lista de states
states = df['state'].values 

score = 0

while True:
    # user input
    answer = screen.textinput(title=f'{score}/50 States Correct', prompt="Give me the name of a US state?").strip().title()
    # print(answer)
    # verificando si existe el answer en el dataframe
    if answer in states:
        state_row = df[df['state'] == answer]
        # print(state_row) 
        #      state    x   y
        # 0  Alabama  139 -77

        # x_index = state_row['x'].index
        # print(x_index) #Index([0], dtype='int64')
        
        # x_coor = state_row['x'].values
        # print(x_coor) #[139]
        
        # handling the coordinates
        x_coor = state_row['x'].values[0]
        y_coor = state_row['y'].values[0]

        # writting the coordinates on the map 
        
        tommy.penup()  
        tommy.goto(x = x_coor, y = y_coor)
        tommy.write(answer)


        score += 1
    else:
        # print('bitch ese state no es de USA')
        continue


    # screen.exitonclick()















# states = df['state'].to_list()
# # print(state)# ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

# x_coor = df['x'] 
# y_coor = df['y'] 

# states_dict = df.to_dict()

# print(states_dict['state'][0]) #alabama




    























