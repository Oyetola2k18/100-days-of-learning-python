#creating the famous pong game
import turtle
import paddle
import ball
import time
import scoreboard
screen = turtle.Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game")

screen.tracer(0)

right_paddle = paddle.Paddle((350,0))
left_paddle = paddle.Paddle((-350,0))
game_ball = ball.Ball()
score = scoreboard.Scoreboard()
screen.listen()
screen.onkey(key="Up",fun=right_paddle.up)
screen.onkey(key="Down",fun=right_paddle.down)
screen.onkey(key="w",fun=left_paddle.up)
screen.onkey(key="s",fun=left_paddle.down)

game_is_on = True
while game_is_on:
    
    time.sleep(game_ball.move_speed)
    screen.update()
    game_ball.move()
    #detect collision with the walls 
    if game_ball.ycor() > 280 or game_ball.ycor() < -280:
        #then bounce
        game_ball.bounce_y()

    
    #detect collision for the  paddles
    if (game_ball.distance(right_paddle) < 50 and game_ball.xcor() > 320) or (game_ball.distance(left_paddle) < 50 and game_ball.xcor() < -320):
        game_ball.bounce_x()
    # else:
        # game_ball.teleport(0,0)
        # game_ball.x_move *= -1
        # game_ball.y_move *= -1
    
    #right paddle misses
    if game_ball.xcor() > 390:
        game_ball.reset_position()
        score.l_point()
    

    #left paddle misses
    if game_ball.xcor() < -390:
        game_ball.reset_position()
        score.r_point()
screen.exitonclick()