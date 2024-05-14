
from turtle import Turtle
SNAKE_SPEED=10
class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score=0
        with open('high_score.txt') as high_score_in_file:
            self.high_score=int(high_score_in_file.read())
        self.color('white')
        self.penup()
        self.goto(-160,270)
        self.scorecard()
        self.hideturtle()
        self.speed=SNAKE_SPEED
    
    def scorecard(self):
        self.clear()
        self.write(f'Score: {self.score} High Score {self.high_score}',align='center', font=  ('Arial',20,'normal'))
    
    def increase_score(self):
        self.score+=1
        self.scorecard()
        
    def increase_speed(self):
        self.speed+=5
    
    def reset_scorecard(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open('high_score.txt',mode='w') as high_score_in_file:
                high_score_in_file.write(str(self.high_score))
        self.score=0
        self.scorecard()
    
    # def game_end(self):
    #     self.goto(0,0)
    #     self.color('white')
    #     self.write(f'Game Over ... ',align='center', font=  ('Arial',25,'normal'))