import time
from turtle import Screen


from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.title("Turtle Cross")
screen.tracer(0)
scoreboard = Scoreboard()
oyuncu = Player()


screen.setup(width=600, height=600)
car_manager1 = CarManager()

screen.listen()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    oyuncu.move()
    screen.update()
    car_manager1.create_car()
    car_manager1.move_cars()

    for car in car_manager1.traffic:
        if car.distance(oyuncu) < 20:
            game_is_on = False
            scoreboard.lose()
    if oyuncu.is_at_finish_line():
        oyuncu.goto(0,-280)
        car_manager1.level_up()
        scoreboard.increase_level()









screen.exitonclick()