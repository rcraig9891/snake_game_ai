from turtle import Turtle


class Notifications(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 280)
        self.color('white')
        self.write(f"Score: {self.score}", font=("Arial", 12, "normal"), align="center")
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", font=("Arial", 12, "normal"), align="center")

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", font=("Arial", 12, "normal"), align="center")




