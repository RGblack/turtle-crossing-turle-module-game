from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()
        self.generate_car()
        self.move_distance = STARTING_MOVE_DISTANCE

    def generate_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle(shape="square")
            car.penup()
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            random_y = random.randint(-250, 250)
            car.goto(320, random_y)
            car.setheading(180)
            self.cars.append(car)

    def move_cars(self):
        for car_num in range(len(self.cars) - 1):
            self.cars[car_num].forward(self.move_distance)

    def level_up(self):
        self.move_distance += MOVE_INCREMENT