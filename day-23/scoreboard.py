from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.goto(-270,220)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level +=1
        self.update()
