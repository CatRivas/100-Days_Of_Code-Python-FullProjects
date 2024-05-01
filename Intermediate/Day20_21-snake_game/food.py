import turtle
import random
class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_wid = 0.5 , stretch_len = 0.5)
        self.color('purple')
        self.speed('fastest')
        self.refresh() #calling the method refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.teleport(x=random_x, y=random_y)