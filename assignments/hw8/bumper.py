"""
Name: Gavin Hammersley
bumper.py

Problem: make balls bounce around window and bounce off of each other

Certification of authenticity
I certify that this assignment is entirely my own work.
"""
import math
import random
from random import randint
from graphics import GraphWin, Circle, Rectangle, color_rgb, Point


def randint_2(start, end):
    start = 0
    end = 50
    x_value = random.randint(start, end)
    return x_value


def get_random(move_amount):
    value = random.randint(-move_amount, move_amount)
    # y_value = random.randint(-move_amount, move_amount)
    return value


def did_collide(circle_ball, circle_ball_2):
    x_1 = circle_ball.getCenter().getX()
    x_2 = circle_ball_2.getCenter().getX()
    y_1 = circle_ball.getCenter().getY()
    y_2 = circle_ball_2.getCenter().getY()

    distance = math.sqrt(((x_2 - x_1) ** 2) + ((y_2 - y_1) ** 2))
    if distance <= circle_ball.getRadius():
        return True
    if distance >= circle_ball.getRadius():
        return False
    return None


def hit_horizontal(circle_ball, graphwin_win):
    circle = circle_ball.getCenter().getY()
    if graphwin_win.height - circle <= circle_ball.getRadius() or \
            abs(0 - circle) <= circle_ball.getRadius():
        return True
    if graphwin_win.height - circle >= circle_ball.getRadius() or \
            abs(0 - circle) >= circle_ball.getRadius():
        return False
    return None


def hit_vertical(circle_ball, graphwin_win):
    circle = circle_ball.getCenter().getX()
    if graphwin_win.width - circle <= circle_ball.getRadius() or \
            abs(0 - circle) <= circle_ball.getRadius():
        return True
    if graphwin_win.width - circle >= circle_ball.getRadius() or \
            abs(0 - circle) >= circle_ball.getRadius():
        return False
    return None


def get_random_color():
    color1 = randint(0, 255)
    color2 = randint(0, 255)
    color3 = randint(0, 255)
    return color_rgb(color1, color2, color3)


def main():
    # draw window
    window = GraphWin("Bumper", 400, 400)
    background = Rectangle(Point(0, 0), Point(400, 400))
    background.setFill(get_random_color())
    background.draw(window)

    # draw circles
    point_a = Point(200, 200)
    circle1 = Circle(point_a, 25)
    circle1.setFill(get_random_color())
    circle1.draw(window)

    point_b = Point(100, 50)
    circle2 = Circle(point_b, 25)
    circle2.setFill(get_random_color())
    circle2.draw(window)

    # move circles
    x_variable = get_random(10)
    y_variable = get_random(10)

    x_variable_2 = get_random(10)
    y_variable_2 = get_random(10)

    while True:
        circle1.move(x_variable, y_variable)
        circle2.move(x_variable_2, y_variable_2)

        # Hits horizontal and bounces if true
        if hit_horizontal(circle1, window) is True:
            y_variable *= -1
            circle1.move(x_variable, y_variable)
        if hit_horizontal(circle2, window) is True:
            y_variable_2 *= -1
            circle2.move(x_variable_2, y_variable_2)

        # Hits vertical and bounces if true
        if hit_vertical(circle1, window) is True:
            x_variable *= -1
            circle1.move(x_variable, y_variable)
        if hit_vertical(circle2, window) is True:
            x_variable_2 *= -1
            circle2.move(x_variable_2, y_variable_2)

        # Hits ball and bounces if true
        if did_collide(circle1, circle2) is True:
            # print("collide")
            x_variable *= -1
            x_variable += random.randint(1, 10)
            y_variable *= -1
            y_variable += random.randint(1, 10)
            circle1.move(x_variable, y_variable)

            x_variable_2 *= -1
            x_variable_2 += random.randint(1, 10)
            y_variable_2 *= -1
            y_variable_2 += random.randint(1, 10)
            circle2.move(x_variable_2, y_variable_2)


# main()
# randint('start', 'end')
# get_random_color()
# hit_horizontal('circle', 'window')
