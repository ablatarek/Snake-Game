from turtle import  Screen
from snake import Snake
from border import Border
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800,height=800)
screen.bgcolor("dimgray")
screen.title("Snake Game")
screen.tracer(0)

is_game_on = False
border = Border()
snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()
screen.onkeypress(snake.up,"Up")
screen.onkeypress(snake.down,"Down")
screen.onkeypress(snake.left,"Left")
screen.onkeypress(snake.right,"Right")
snake.create_snake()



# Game Loop
is_game_on = True
while is_game_on :
    screen.update()
    time.sleep(snake.movement_speed)

    #Snake_movement
    snake.move()
    # Food Collision
    if snake.head.distance(food) < 15 :
        snake.growup()
        scoreboard.increase_score()
        

        food.food_erstellen()

    if snake.border_collision():
        scoreboard.save_highscore()
        is_game_on = False
        scoreboard.game_over()
    if snake.tail_collision():
        scoreboard.save_highscore()
        is_game_on = False
        scoreboard.game_over()
    



screen.exitonclick()