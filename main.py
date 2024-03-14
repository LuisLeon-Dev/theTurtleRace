import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt='Which will win the race? Enter a color: ')
colors_list = ['blue', 'orange', 'red', 'purple']
turtles = []

for i in range(4):
    y = i * 50
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors_list[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=(-80+y))
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You've win. the {winning_color} turtle wins!")
            else:
                print(f"You've lost. the {winning_color} turtle wins!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
