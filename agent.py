import queue
import math


def calculate_distance(position, x2, y2):
    """Euclidean distance between two points."""
    x1, y1 = position
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


class Agent:

    def __init__(self):
        self.move_distance = 20
        self.random_probability = 0.3
        self.restricted_moves = {
            'right': 'left',
            'left': 'right',
            'up': 'down',
            'down': 'up'
        }
        self.direction_adjustments = {
            'right': (self.move_distance, 0),
            'left': (-self.move_distance, 0),
            'up': (0, self.move_distance),
            'down': (0, -self.move_distance)
        }

    def next_move(self, snake, food):
        valid_movements = queue.PriorityQueue()
        neighbours = ['right', 'left', 'up', 'down']
        neighbours.remove(self.restricted_moves[snake.direction])
        heuristic = snake.heuristic
        """Greedy Local Search"""
        for neighbour in neighbours:
            dx, dy = self.direction_adjustments[neighbour]
            position = (snake.head.xcor() + dx, snake.head.ycor() + dy)
            new_heuristic = food.distance(position)
            collision = False
            """Check the move is valid"""
            for square in snake.segments[1:]:
                if calculate_distance(position, square.xcor(), square.ycor()) < 10:
                    collision = True
            """Greedy Local Search: Add commented code to if statement"""
            if not collision: # new_heuristic < heuristic and
                valid_movements.put((new_heuristic, neighbour))
        """Terminate if no valid moves"""
        if valid_movements.empty():
            return 0, None
        else:
            return valid_movements.get()

