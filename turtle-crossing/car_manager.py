from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.speed = STARTING_MOVE_DISTANCE
        self.hideturtle()
        self.cars = []
        self.counter = 0
    
    def create_car(self):
        self.counter += 1
        if self.counter == 6:
            new_y = random.randint(-250, 250)
            new_car = Turtle("square")
            new_car.penup()
            new_car.setheading(180)
            new_car.shapesize(1,2)
            new_car.color(random.choice(COLORS))
            new_car.goto(280,new_y)
            self.cars.append(new_car)
            self.counter = 0
    
    def move_car(self):
        for car in self.cars:
            car.forward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT


        
