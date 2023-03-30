import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Initialize game elements
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Initialize key function
screen.listen()
screen.onkey(key="Up", fun=player.move_up)

game_is_on = True
i = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.generate_car()
    car_manager.move_cars()

    # Detect collision
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect finish line
    if player.ycor() > 280:
        player.level_up()
        car_manager.level_up()
        scoreboard.increase_score()

screen.exitonclick()