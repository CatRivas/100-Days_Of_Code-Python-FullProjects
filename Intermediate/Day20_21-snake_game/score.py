import turtle
ALIGNMENT = 'Center'
FONT = ('Comic Sans MS', 20, 'normal')

class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0

        #using data.txt
        with open('data.txt') as f:
            contents = f.read()

        self.high_score = int(contents)
        self.hideturtle()
        self.color('white')
        self.teleport(x=0, y= 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', align= ALIGNMENT, font=FONT)
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

            #RECORDING the highest score in data.txt (overwrite it)
            with open('data.txt', mode= 'w') as f:
                f.write(str(self.score))
        
        self.score = 0 #reseting the new score
        self.update_score()  #next round

    def increase_score(self):
        self.score += 1
        self.update_score()


    # def game_over(self):
    #     self.teleport(0, 0)
    #     self.write(f'GAME OVER', align= ALIGNMENT, font=FONT)