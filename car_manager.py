from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 20


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.RANDOM_X = random.randint(320, 380)
        self.RANDOM_Y = random.randint(-260, 260)
        self.shape("square")
        self.shapesize(1,2)
        self.penup()
        self.color(random.choice(COLORS))
        self.goto(self.RANDOM_X , self.RANDOM_Y)
        self.X_move = MOVE_INCREMENT
        self.move()


    def move(self):
        new_x = self.xcor() - self.X_move
        self.goto(new_x , self.ycor())



