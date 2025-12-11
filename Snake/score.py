from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.goto(0,270)
        self.penup()
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()
        
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.highscore}" , align = "center", font = ("Arial", 20, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.highscore))

        self.score = 0
        self.update_scoreboard()


    def update_score(self):
        self.score += 1
        self.update_scoreboard()



        
    



