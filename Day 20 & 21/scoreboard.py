from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt",mode="r") as file:
            self.high_score=int(file.read())
            
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"SCORE = {self.score} High Score = {self.high_score} ",align="center",font=("Arial",24,"normal"))

    def increase(self):
        self.score+=1
        self.update()

    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("data.txt",mode="w")as file:
                file.write(f"{self.high_score}")
        self.score=0
        self.update()