from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet",prompt= "which color turtle do you choose?")
turtle_color = ["green", "red", "orange", "blue", "yellow", "purple"]
turtle_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=turtle_position[turtle_index])
    new_turtle.color(turtle_color[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color== user_bet:
                print(f"you've won! the {winning_color} is the winner")
            else:
                print(f"you lost the {winning_color} is the winner")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)





screen.exitonclick()