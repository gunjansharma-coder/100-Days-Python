import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("The Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball=Ball()
score= Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_on=True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #the ball needs to boucne back
        ball.bounce_y()
    # Detect collison with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() >320 or ball.distance(l_paddle) < 50 and ball.xcor() <-320:
        ball.bounce_x()
        
    #If the paddle misses
    if ball.xcor()>380:
        ball.reset()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset()
        score.r_point()
    # To end the game 
    if score.r_score == 5:
        score.game_over("Right Player Wins!")
        game_on = False

    if score.l_score == 5:
        score.game_over("Left Player Wins!")
        game_on = False

screen.exitonclick()
