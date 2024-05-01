import turtle
ALIGNMENT = 'Center'
FONT = ('Comic Sans MS', 20, 'normal')

class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.hideturtle()
        self.color('white')
        self.teleport(x=0, y= 260)
        self.update_score()

    def update_score(self):
        self.write(f'Score: {self.score}', align= ALIGNMENT, font=FONT)
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.teleport(0, 0)
        self.write(f'GAME OVER', align= ALIGNMENT, font=FONT)