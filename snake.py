# Simple snake game 
#BY: Richard Cross

from turtle import Turtle, Screen
Screen = Screen()
POS = [(0, 0) (-20, 0), (-40, 0)]
move_distance = 20
up = 90
down = 270
left = 180
right = 0
# creating the snake class
class Snake:
    def __init__(self):
        self.snake_Len = []
        self.create_snake()
        self.head = self.snake_Len[0]