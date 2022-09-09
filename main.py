from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

all_turtles = []
y_position = -100
for i in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[i])
    all_turtles.append(new_turtle)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position)
    y_position += 40

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You've won! the {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! the {winning_color} turtle is the winner!")
        else:
            rand_distance = randint(0, 10)
            turtle.forward(rand_distance)

screen.exitonclick()
