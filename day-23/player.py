from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.teleport(0,-280)
    
    def move(self):
        self.y=self.ycor()+ MOVE_DISTANCE
        self.goto(self.xcor(),self.y)

    def reset(self):
        self.goto(STARTING_POSITION)

    def finish(self):
        if self.ycor()>280:
            return True
        else:
            return False