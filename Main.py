from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score
screen = Screen()
screen.listen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game = True
while game:
    screen.update()
    time.sleep(.1)