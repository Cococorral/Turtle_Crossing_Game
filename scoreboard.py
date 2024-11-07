from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.points = 0
        self.penup()
        self.hideturtle()
        self.goto(-370, 280)
        self.write(f"Score: {self.points}", font=("Courier", 17, "normal"))

    def scoring(self):
        self.points += 1
        self.clear()
        self.write(f"Score: {self.points}", font=("Courier", 17, "normal"))

    def lose(self):
        self.goto(-120,-30)
        self.write("GAME OVER", font=("Courier", 30, "normal"))
