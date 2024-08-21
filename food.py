from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed('fastest')
        self.new_position()

    def new_position(self):
        x_position = random.randint(-270, 270)
        y_position = random.randint(-270, 270)
        self.goto(x_position, y_position)









