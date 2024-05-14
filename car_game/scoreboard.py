from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.level=1
        self.hideturtle()
        self.penup()
        self.goto(-200,250)
        self.scorecard()
        
    
    def scorecard(self):
        self.clear()
        self.write(f'Level: {self.level}',align='center',font=FONT)
        
    def update_level(self):
        self.level+=1
        self.scorecard()
    def game_over(self):
        self.goto(0,0)
        self.write(f'Game Over. ',align='center',font=FONT)
