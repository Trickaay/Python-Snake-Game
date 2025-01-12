from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        self.color("black")
        self.update_score()
        
    def update_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Roboto", 25, "normal"))