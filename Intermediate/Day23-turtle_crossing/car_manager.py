from turtle import Turtle
import random
 
COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []
        self.current_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        # This condition helps to avoid creating too many cars at once
        if random_chance == 1 :
            new_car = Turtle()
            new_car.shape('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            #positioning the new car
            new_car.penup()
            #the 'y' position must be random
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            #Adding a new car to the cars list
            self.cars.append(new_car)


    def car_move(self):
        """Move all cars in the cars list backwards."""
        for car in self.cars:
            car.backward(self.current_speed)

    def car_move_incremeant(self):
        """Increase the speed of the cars."""
        self.current_speed += MOVE_INCREMENT
