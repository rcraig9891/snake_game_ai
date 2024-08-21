import turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.heuristic = 0
        self.direction = 'right'

    def create_snake(self):
        for index, position in enumerate(START_POSITIONS):
            new_square = turtle.Turtle()
            new_square.shape('square')
            new_square.penup()
            if index == 0:
                new_square.color('green')
            else:
                new_square.color('white')
            new_square.goto(position)
            self.segments.append(new_square)

    def move(self, move_distance=20):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.head.forward(move_distance)

    def grow(self):
        new_square = turtle.Turtle()
        new_square.shape('square')
        new_square.penup()
        new_square.color('white')
        new_square.goto(self.segments[len(self.segments) - 1].xcor(), self.segments[len(self.segments) - 1].ycor())
        self.segments.append(new_square)

    def set_heuristic(self, goal_state):
        self.heuristic = self.head.distance(goal_state)

    def up(self):
        if self.direction != 'down':
            self.head.setheading(90)
            self.direction = 'up'

    def down(self):
        if self.direction != 'up':
            self.head.setheading(270)
            self.direction = 'down'

    def left(self):
        if self.direction != 'right':
            self.head.setheading(180)
            self.direction = 'left'

    def right(self):
        if self.direction != 'left':
            self.head.setheading(0)
            self.direction = 'right'


