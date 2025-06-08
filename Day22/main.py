#creating the famous pong game
import turtle
import paddle
import ball
import time
screen = turtle.Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game")

screen.tracer(0)

right_paddle = paddle.Paddle((350,0))
left_paddle = paddle.Paddle((-350,0))
game_ball = ball.Ball()



screen.listen()
screen.onkey(key="Up",fun=right_paddle.up)
screen.onkey(key="Down",fun=right_paddle.down)
screen.onkey(key="w",fun=left_paddle.up)
screen.onkey(key="s",fun=left_paddle.down)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    game_ball.move()
screen.exitonclick()