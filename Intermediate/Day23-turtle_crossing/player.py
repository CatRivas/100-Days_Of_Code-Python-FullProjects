STARTING_POINT = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        
        self.shape('turtle')
        self.color('white')
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POINT)

    def move(self):
        self.forward(MOVE_DISTANCE)