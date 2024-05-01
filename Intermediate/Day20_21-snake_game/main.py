import turtle
import time
from snake import Snake

#screen setup
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game 30-04-2024')
screen.tracer(0) #turn off tracer

#creating an instance of Snake()
snake = Snake()

#keybord
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


#moving the snake
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    
    

screen.exitonclick()



