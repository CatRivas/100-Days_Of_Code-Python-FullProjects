from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.right_score = 0
        self.left_score = 0
        
        self.color('white')
        self.hideturtle()
        self.penup()
        self.update_scoreboard() #calling update_scoreboard

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=self.left_score, align='center',font=('Comic Sans MS', 60, 'bold'))
        self.goto(100, 200)
        self.write(arg=self.right_score, align='center',font=('Comic Sans MS', 60, 'bold'))

    def left_point(self):
        self.left_score += 1
        self.update_scoreboard()

    def right_point(self):
        self.right_score += 1
        self.update_scoreboard()