from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-150,250)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(arg=f"Level {self.level} " , align="center" , font=FONT )

    def increase_level(self):
        self.clear()
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0,0)
        self.clear()
        self.write(arg= "GAME OVER" , align='center' , font=("Courier", 40, "normal"))
        self.goto(0, -100)
        self.write(arg=f"Your Final Level: {self.level}" , align='center' , font=FONT)


