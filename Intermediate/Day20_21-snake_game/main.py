import turtle

#screen setup
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game 30-04-2024')


#snake body 
x_positions = [0, -20, -40]

for position in range(3):
    sub_snake = turtle.Turtle()
    sub_snake.shape('square')
    sub_snake.color('white')

    sub_snake.teleport(x= x_positions[position] , y=0)


screen.exitonclick()