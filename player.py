import turtle
from turtle import Turtle,Screen

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setposition(STARTING_POSITION)
        self.setheading(90)


    def move(self):
        def move_up():
          self.sety(self.ycor()+MOVE_DISTANCE)
        turtle.onkey(key="space", fun=move_up)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False



