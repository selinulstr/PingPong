from turtle import Turtle

MOVING_DISTANCE = 20
POSITIONS = [(350, 0), (-350, 0)]


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def up(self):
        new_y = self.ycor() + MOVING_DISTANCE
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - MOVING_DISTANCE
        self.goto(self.xcor(), new_y)


