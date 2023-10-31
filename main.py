from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.snake_up, "Up")
screen.onkey(snake.snake_right, "Right")
screen.onkey(snake.snake_down, "Down")
screen.onkey(snake.snake_left, "Left")

game_is_one = True
while game_is_one:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.snake_grow()
        scoreboard.increase_score()

    # detect collision with wall
    if (
        (snake.head.xcor() > 290)
        or (snake.head.xcor() < -290)
        or (snake.head.ycor() > 290)
        or (snake.head.ycor() < -290)
    ):
        scoreboard.reset()
        snake.reset()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
