from turtle import Turtle



STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_SPEED = 0
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snakes = []
        # self.create_snake()
        # self.head = self.snakes[0]
        self.stop = True
        self.movement_speed = 0.2

        
    def create_snake(self):
        for position in STARTING_POSITION:
            new_snake = Turtle("square")
            new_snake.color("aquamarine2")
            new_snake.up()
            new_snake.goto(position)
            self.snakes.append(new_snake)
            self.snakes[0].color("aquamarine2")
            self.head = self.snakes[0]
            

    def move(self):
        
        for snake_num in range(len(self.snakes)-1 ,0,-1):
            neue_xcor = self.snakes[snake_num - 1].xcor()
            neue_ycor = self.snakes[snake_num - 1].ycor()
            self.snakes[snake_num].goto(neue_xcor,neue_ycor)
        self.head.forward(20)
        self.snakes[len(self.snakes)-1].showturtle()
            

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def border_collision(self) -> bool:
        if self.head.xcor() >= 300 :
            return True
        elif self.head.ycor() >= 300:
            return True
        elif self.head.xcor() <= -300:
            return True
        elif self.head.ycor() <= -300:
            return True
        else:
            return False

    def add_snake(self):
        self.segment = Turtle("square")
        self.segment.hideturtle()
        self.segment.color("aquamarine2")
        self.segment.up()
        self.snakes.append(self.segment)
    def tail_collision(self):
        for sneak in self.snakes[1:]:
            if self.head.distance(sneak) < 10:
                return True
            
    def growup(self):
        self.add_snake()
        self.movement_speed *= 0.95

            






















