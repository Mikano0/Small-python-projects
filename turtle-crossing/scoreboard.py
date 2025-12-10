from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-210, 250)
        self.write(f"Level: {self.level}", align = "center", font = FONT)

    def update_scoreboard(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align = "center", font = FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align = "center", font = FONT)
