from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.all_cars=[]
        self.car_speed=STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance=random.randint(1,6)
        if random_chance==1:
            new_car=Turtle('square')
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y=random.randint(-260,260)
            new_car.goto(280,random_y)
            
            self.all_cars.append(new_car)
        
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
    
    def speed_increment(self):
        self.car_speed+=10