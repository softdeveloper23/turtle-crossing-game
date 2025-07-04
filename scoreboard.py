from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-250, 250)
        self.level = 1
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=("Courier", 20, "normal"))

    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align="center", font=("Courier", 60, "normal"))        
