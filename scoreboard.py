from turtle import Turtle
PATH ="data.txt"

class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.highscore = 0
        with open(PATH) as data:
            content = data.read()
            if content:
                self.highscore = int(content)
        self.ht()
        self.up()
        self.goto(0,320)
        self.color("aquamarine2")
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align="center",font=("Verdana", 30 ,"bold"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def save_highscore (self):

        if self.score > self.highscore:
            self.highscore = self.score

        with open(PATH, mode="w") as data:
            data.write(f"{self.highscore}")
        
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align="center",font=("Verdana", 30 ,"bold"))

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER \nHighscore: {self.highscore}\n    Score: {self.score}",align="center",font=("Verdana",30,"bold"))



        

        
        
    