from turtle import Screen
from tortuga import Tortuga
from cars import Cars
import random
import time
from scoreboard import Scoreboard

screen = Screen()

screen.screensize(canvwidth=600, canvheight=600)
screen.tracer(0)

my_turtle = Tortuga()

screen.listen()
screen.onkey(fun=my_turtle.move_up, key="Up")
screen.onkey(fun=my_turtle.move_down, key="Down")

my_car = Cars()

score = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    my_car.create_cars()
    my_car.move()

    for car in my_car.all_cars:
        if car.distance(my_turtle) < 21:
            game_is_on = False
            score.lose()

    if my_turtle.ycor() >= 280:
        my_turtle.teleport(0, -280)
        my_car.level_up()
        score.scoring()

screen.exitonclick()
