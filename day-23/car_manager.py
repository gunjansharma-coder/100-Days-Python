import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LANES = [-240, -180, -120, -60, 0, 60, 120, 180, 240]


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.car_speed= STARTING_MOVE_DISTANCE
    
    def create(self):
        lane = random.choice(LANES)

        for car in self.all_cars:
            if car.ycor() == lane and car.xcor() > 150:
                return

        new_car = Turtle("square")
        new_car.penup()
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.color(random.choice(COLORS))
        new_car.goto(300, lane)

        self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
    
    def game_over(self):
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
