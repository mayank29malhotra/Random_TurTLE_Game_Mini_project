from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="Make Your Bet ", prompt="Which Turtle will win the race")
y = [-70, -40, -10, 20, 50, 80]
color = ["red", "orange", "yellow", "green", "blue", "violet"]
all_turtles = []

for i in  range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(color[i])
    tim.penup()
    tim.goto(-230, y[i])
    all_turtles.append(tim)

if user_bet:
    is_race_on = True
screen.bgcolor("black")
while is_race_on:
    for tur in all_turtles:
        if tur.xcor() > 230:
            is_race_on = False
            if tur.pencolor()== user_bet:
                print("You Won !!")
            else:
                print("You Lose  !!")
            print(f"The Winner of the Race is {tur.pencolor()}")
        dis = random.randint(0, 10)
        tur.forward(dis)




screen.exitonclick()
