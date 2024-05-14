from turtle import Turtle
class Ball(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move=10
        self.y_move=10
        self.ball_speed=0.1
    
    def move_ball(self):
        x_cor=self.xcor()+self.x_move
        y_cor=self.ycor()+self.y_move
        self.goto(x=x_cor,y=y_cor)
    
    def y_bounce_back(self):
        self.y_move*=-1
    def x_bounce_back(self):
        self.x_move*=-1
        self.ball_speed*=0.9
    
    def reset_position(self):
        self.goto(0,0)
        self.ball_speed=0.1
        self.x_bounce_back()