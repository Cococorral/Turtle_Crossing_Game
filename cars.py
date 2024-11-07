import random
from turtle import Turtle
from random import randint, choice

COLOR_LIST = ["red", "blue", "orange", "green", "blue"]


class Cars():

    def __init__(self):
        self.all_cars = []
        self.distance = 10

    def create_cars(self):
        chance = randint(1, 3)
        if chance == 2:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(1, 2)
            new_car.color(choice(COLOR_LIST))
            new_car.penup()
            new_car.goto(400, randint(-260, 260))
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.fd(self.distance)

    def level_up(self):
        self.distance += 3






