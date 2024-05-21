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
        self.player_go_home()

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def player_go_home(self):
        self.goto(STARTING_POINT)

    def car_colision(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
        
    def game_over(self):
        self.hideturtle()
        self.color('white')
        self.home()
        self.write(arg='GAME OVER', align='center',font=('Comic Sans MS', 60, 'bold'))


            