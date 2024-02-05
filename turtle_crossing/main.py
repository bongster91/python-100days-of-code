import time
from turtle import Screen
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

user = Player()

screen.listen()
screen.onkey(user.up, 'Up')


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    