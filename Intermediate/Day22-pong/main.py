import turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('PONG (13-05-2024)')
screen.tracer(0) #turning off the animation

#instances of Paddle
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

#instance of Ball
ball = Ball()

#instance of Scoreboard
scoreboard = Scoreboard()

#keyboards
screen.listen()

#right paddle
screen.onkey(right_paddle.up, 'Up')
screen.onkey(right_paddle.down, 'Down')

#left paddle
screen.onkey(left_paddle.up, 'w')
screen.onkey(left_paddle.down, 's')


#is the game running?
is_game_on = True

while is_game_on:
    time.sleep(ball.ball_speed)
    screen.update() #turning on the animation
    ball.move()

    #is there a collision with the ceiling or floor (y axis)?
    if ball.ycor() > 280 or ball.ycor() < -280:
        # print('hit')
        ball.bounce_y()

    #is there a collision with any paddle?
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    #did the ball pass the x axis?
    #rigth_paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()

    #left_paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()
    
screen.exitonclick()