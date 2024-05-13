from turtle import Turtle

#The default size of a Turtle object is 20 pixels and the default position is Home at (0, 0), so just leave it

class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape('square')
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10

        self.ball_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        # print(new_x, new_y)
        self.goto(new_x, new_y)


    #the ball touch the y axis
    def bounce_y(self):
        self.y_move *= -1
    

    #the ball touch a paddle
    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.bounce_x()



