import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)


#Player Movements
player = Player()
screen.onkey(fun= player.move , key="Up")

#Scoreboard
scoreboard = Scoreboard()
Cars = []

car_speed = 20

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()


    #Spawning Cars
    if random.randint(1,4) == 1:
        car = CarManager()
        car.X_move = car_speed
        Cars.append(car)

    #Moving Cars
    for car in Cars:
        car.move()
        #Detecing collisions
        if abs(player.xcor() - car.xcor()) < 20 and abs(player.ycor() - car.ycor()) < 20:
            scoreboard.game_over()
            game_is_on = False

    #Increasing level
    if player.ycor() >= 280:
        scoreboard.increase_level()
        car_speed += 10
        player.reset()

screen.exitonclick()