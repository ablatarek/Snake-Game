from turtle import Turtle
from random import randrange


class Food(Turtle):
    def __init__(self) ->None:
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("lavender")
        self.speed("fastest")
        self.food_erstellen()

    def food_erstellen(self):
        random_x = randrange(-280, 280, 20)
        random_y = randrange(-280, 280, 20)
        self.goto(random_x, random_y)




