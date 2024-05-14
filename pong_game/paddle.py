from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(position)
        self.x_move=10
        self.y_move=10
    
    def move_up(self):
        x_cor=self.xcor()
        y_cor=self.ycor()+self.y_move
        self.goto(x=x_cor,y=y_cor)
    def move_down(self):
        x_cor=self.xcor()
        y_cor=self.ycor()-self.y_move
        self.goto(x=x_cor,y=y_cor)