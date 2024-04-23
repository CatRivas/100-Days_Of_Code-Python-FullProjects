import turtle
import random

#creating an object of Screen()
screen = turtle.Screen()
screen.setup(width = 500, height = 400) #keyword arguments
user_choose_contestant = screen.textinput(title = 'Make your bet', prompt = 'Which turtle will win the race? Enter a color: ')
colors = ['cyan', 'coral', 'azure4', 'hotpink', 'green', 'RoyalBlue']

#creating intances of the class Turtle()
# contestant_1 = turtle.Turtle('turtle')
# contestant_1.teleport(x = -230, y = -120)
# contestant_1.color(colors[0])

# contestant_2 = turtle.Turtle('turtle')
# contestant_2.teleport(x = -230, y = -70)
# contestant_2.color(colors[1])

# contestant_3 = turtle.Turtle('turtle')
# contestant_3.teleport(x = -230, y = -20)
# contestant_3.color(colors[2])

# contestant_4 = turtle.Turtle('turtle')
# contestant_4.teleport(x = -230, y = 30)
# contestant_4.color(colors[3])

# contestant_5 = turtle.Turtle('turtle')
# contestant_5.teleport(x = -230, y = 80)
# contestant_5.color(colors[4])

# contestant_6 = turtle.Turtle('turtle')
# contestant_6.teleport(x = -230, y = 130)
# contestant_6.color(colors[5])



#creating instances of the class Turtle() with a more DRY approach
constestant_list = []
y_position = -120

for item in range(6):
    constestant = turtle.Turtle(shape = 'turtle')
    constestant.teleport(x = -230, y = y_position)
    constestant.color(colors[item])
    y_position = y_position + 50
    constestant_list.append(constestant)

# print(constestant_list)  #[<turtle.Turtle object at 0x00000295C1457BC0>, <turtle.Turtle object at 0x00000295C1457E90>, <turtle.Turtle object at 0x00000295C1484170>, <turtle.Turtle object at 0x00000295C1484440>, <turtle.Turtle object at 0x00000295C14846E0>, <turtle.Turtle object at 0x00000295C1484980>]

#race
if user_choose_contestant:
    race_on = True

while race_on:
    for turtle in constestant_list:
        if turtle.xcor() > 230:
            race_on = False

            winner_color = turtle.pencolor()
            if winner_color == user_choose_contestant:
                print(f"You've won! The {winner_color} turtle is the winner!")
                    
            else:
                print(f"You've lost! The {winner_color} turtle is the winner!")
        
            
        random_speed = random.randint(0, 10) #contestant random speed
        turtle.penup()
        turtle.forward(random_speed)



screen.exitonclick()
