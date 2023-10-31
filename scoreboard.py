from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
FINAL_SCORE_FONT = ("Courier", 40, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("higher_score.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.pencolor("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score}  High score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("higher_score.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
