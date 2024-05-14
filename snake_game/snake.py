from turtle import Turtle
import random,time
STARTING_POSITION=[(0,0),(-20,0),(-40,0)]
COLORS=['RED','GREEN','ORANGE','BLUE','PURPLE','white']
UP,DOWN,LEFT,RIGHT=90,270,180,0
class Snake:
    def __init__(self) -> None:
        self.Segments=[]
        self.create_snake()
        self.head=self.Segments[0]
        
    def create_snake(self):
        for positions in STARTING_POSITION:
            self.add_segment(positions)
            
    def add_segment(self,positions):
        tim=Turtle('circle')
        tim.color('white')
        tim.penup()
        tim.goto(positions)
        self.Segments.append(tim)
    
    def extend_snake(self):
        self.add_segment(self.Segments[-1].position())
        
    def move_snake(self):
        for segment in range(len(self.Segments)-1,0,-1):
            x_cor=self.Segments[segment-1].xcor()
            y_cor=self.Segments[segment-1].ycor()
            self.Segments[segment].goto(x_cor,y_cor)
        self.head.forward(20)
    
    def hide_old_snake(self):
        for segs in self.Segments:
            segs.goto(1000,1000)
        self.Segments.clear()
        self.create_snake()
        
        self.head=self.Segments[0]
        
        
    def move_up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def move_down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def move_left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    def move_right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)