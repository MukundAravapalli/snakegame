from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from random import Random
import time

r = Random()


screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# game_mode = screen.textinput(title="Choose Game Mode", prompt="Would you like to play in Easy, Normal, Hard, or Super Challenging mode:")
# prompter = screen.textinput(title = "What's up fam", prompt="How's it goin")

game_is_on = True

while game_is_on:
    screen.update()
    # if game_mode == "Easy":
    #     time.sleep(0.1)
    # elif game_mode == "Normal":
    #     time.sleep(0.07)
    # elif game_mode == "Hard":
    #     time.sleep(0.05)
    # elif game_mode == "Super Challenging":
    #     time.sleep(0.03)
    time.sleep(0.07)
    snake.move()
    # Detect colission with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.inc_score()

    # Detect colission with wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with self
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()

