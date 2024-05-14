from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.create_food()
        
    
    def create_food(self):
        rand_x=random.randint(-270,270)
        rand_y=random.randint(-270,270)
        self.shape('circle')
        self.color('yellow')
        self.penup()
        self.goto(rand_x,rand_y)
    
