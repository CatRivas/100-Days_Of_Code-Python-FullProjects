import turtle

X_POSITIONS = [0, -20, -40]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_parts = []
        self.create_snake()  #calling create_snake()
        self.head = self.snake_parts[0]
    def create_snake(self):
        for position in range(3):
            sub_snake = turtle.Turtle()
            sub_snake.shape('square')
            sub_snake.color('white')
            sub_snake.penup()

            sub_snake.teleport(x= X_POSITIONS[position] , y=0)
            self.snake_parts.append(sub_snake)

    def move(self):
        for part in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[part -1].xcor()
            new_y = self.snake_parts[part -1].ycor()
            
            self.snake_parts[part].teleport(new_x, new_y)

        self.snake_parts[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)