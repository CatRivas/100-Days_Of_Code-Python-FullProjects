from turtle import Turtle

FONT = ('Comic Sans MS', 24, 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.level = 1

        self.hideturtle()
        self.penup()
        self.color('white')
        self.score_update()

    def score_update(self):
        self.clear()
        self.goto(-210, 250)
        self.write(arg=f'Level: {self.level}', align='center',font=FONT)  
        
    def level_up(self):
        self.level += 1
        self.score_update()

    