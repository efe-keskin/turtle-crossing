from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.setpos(-220,260)
        self.update_scoreboard()


    def lose(self):
        self.setpos(0,0)
        self.write("Game Over",False,"center",("Courier", 24, "normal"))



    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", False, "center", FONT)


    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()


