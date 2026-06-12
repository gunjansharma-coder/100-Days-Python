from turtle import Turtle

UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake:
    def __init__(self):
        self.segments=[]
        self.create()
        self.head= self.segments[0]

    def create(self):
        segments_pos=[(0,0),(-20,0),(-40,0)]
        for i in range(3):
            t=Turtle(shape="square")
            t.color("white")
            t.penup()
            t.goto(segments_pos[i])
            self.segments.append(t)

    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            x=self.segments[i-1].xcor()
            y=self.segments[i-1].ycor()
            self.segments[i].goto(x,y)

        self.head.forward(20)

    def up (self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    
    def down (self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)

    def left (self):
         if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    
    def right (self):
         if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
    

    