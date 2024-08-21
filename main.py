import turtle
import time
from snake import Snake
from food import Food
from notifications import Notifications
from agent import Agent

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
snake = Snake()
agent = Agent()
food = Food()
notifications = Notifications()
game_on = True


def snake_eats_food(obj_1, obj_2):
    return obj_1.distance(obj_2) < 20


def border_collision(x_pos, y_pos):
    return x_pos > 300 or x_pos < -300 or y_pos > 300 or y_pos < -300


def snake_direction(obj, direct):
    if direct == 'up':
        obj.up()
    elif direct == 'down':
        obj.down()
    elif direct == 'left':
        obj.left()
    elif direct == 'right':
        obj.right()


while game_on:
    screen.update()
    time.sleep(0.02)
    snake.set_heuristic(food)
    _, direction = agent.next_move(snake, food)
    if direction is None:
        notifications.game_over()
        game_on = False
    snake_direction(snake, direction)
    snake.move()
    if snake_eats_food(snake.head, food):
        food.new_position()
        snake.grow()
        notifications.score += 1
        notifications.update_score()

screen.exitonclick()
