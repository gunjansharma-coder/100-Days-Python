from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.update()

    def update(self):
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Arial", 24, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Arial", 24, "normal"))

    def l_point(self):
        self.l_score+= 1
        self.clear()
        self.update()

    def r_point(self):
        self.r_score+= 1
        self.clear()
        self.update()

    def game_over(self, message):
        self.goto(0, 0)
        self.write(message, align="center", font=("Arial", 24, "normal"))