from turtle import Turtle

class Border:
    def __init__(self):
        self.border = Turtle()
        self.draw_border()

    def draw_border(self):
        self.border.hideturtle()
        self.border.speed(0)
        self.border.up()
        self.border.goto(290,-290)
        self.border.down()
        self.border.color("seagreen1")
        self.border.goto(290,290)
        self.border.goto(-290,290)
        self.border.goto(-290,-290)
        self.border.goto(290,-290)
        
    