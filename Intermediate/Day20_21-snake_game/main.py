import turtle
import time
from snake import Snake
from food import Food
from score import Score

#screen setup
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game 30-04-2024 & high score 06-06-2024')
screen.tracer(0) #turn off tracer



#creating an instance of Snake()
snake = Snake()

#creating an instance of Food()
food = Food()

#creating an instance of Score()
score = Score()


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

    #detecting collision with food
    if snake.head.distance(food) < 15: 
        food.refresh()
        snake.extend_snake()
        score.increase_score()

    #detecting collision with wall (GAME OVER)
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        # game_is_on = False
        # score.game_over()
        score.reset()
        snake.reset()

    #detecting collision with tail (GAME OVER)
    for part_snake in snake.snake_parts[1:]: #omiting the first part of the snake (head)
        if snake.head.distance(part_snake) < 10:
            # game_is_on = False
            # score.game_over()
            score.reset()
            snake.reset()

screen.exitonclick()



