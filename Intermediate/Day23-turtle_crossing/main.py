import time
import turtle as t
from player import Player


#instance of Player()
player = Player()



#instance of Screen()
screen = t.Screen()
#screen setup
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('The Turtle Crossing 20-05-24')

#stops the animation
screen.tracer(0)

screen.listen()
#keyboard
screen.onkey(player.move, 'Up')


#flag 
is_the_game_on = True

while is_the_game_on:
    time.sleep(0.1)
    #turns on the animation
    screen.update()













screen.exitonclick()