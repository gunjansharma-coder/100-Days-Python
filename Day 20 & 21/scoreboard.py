from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.write(f"SCORE = {self.score} ",align="center",font=("Arial",24,"normal"))
        self.hideturtle()

    def increase(self):
        self.clear()
        self.score+=1
        self.write(f"SCORE = {self.score} ",align="center",font=("Arial",24,"normal"))

    def game_over(self):
        self.goto(0,0)
        self.clear()
        self.write("GAME OVER",align="center",font=("Arial",24,"normal"))
        self.goto(0,-30)
        self.write(f"Your final score: {self.score}",align="center",font=("Arial",24,"normal"))