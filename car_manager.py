import time
from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.traffic = []
        self.car_speed = STARTING_MOVE_DISTANCE
    def create_car(self):
        random_choice = random.randint(1,6)
        if random_choice == 1:
          new_car = Turtle()
          new_car.penup()
          new_car.shape("square")
          new_car.shapesize(stretch_wid=1,stretch_len=2)
          new_car.setpos(270,random.randint(-270,270))
          new_car.color(random.choice(COLORS))
          random_y =random.randint(-250,250)
          new_car.goto(300,random_y)
          self.traffic.append(new_car)



    def move_cars(self):
        for car in self.traffic:
            car.backward(self.car_speed)
    def level_up(self):
        self.car_speed += MOVE_INCREMENT




