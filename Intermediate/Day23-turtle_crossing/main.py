import time
import turtle as t
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#instance of Screen()
screen = t.Screen()
#screen set up
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('The Turtle Crossing 20-05-24')

#stops the animation
screen.tracer(0)

#instance of Player()
player = Player()

#listen for the keyboard
screen.listen()
#up key
screen.onkey(player.move_up, 'Up')

#instance of CarManager()
car_manager = CarManager()

#instance of CarManager()
scoreboard = Scoreboard()


#game flag 
is_the_game_on = True

while is_the_game_on:
    time.sleep(0.1)
    #turn on the animation
    screen.update()
    
    #create and move the cars
    car_manager.create_car()
    car_manager.car_move()

    #car collision?
    for car in car_manager.cars:
        if player.distance(car) < 20:
            is_the_game_on = False
            player.game_over()

    #the player reached the other side? 
    if player.car_colision(): #if this is true
        player.player_go_home()
        car_manager.car_move_incremeant()   
        scoreboard.level_up() 
    
            
screen.exitonclick()