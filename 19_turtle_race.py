import turtle
from turtle import Turtle,Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width=600,height=500)
user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a color (rainbow color"
                                                          " only): ")
color = ['red','blue','green','yellow','orange','purple']
y_position = [-100,-50,0,50,100,150]
all_turtle = []

for each in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x= -270, y= y_position[each])
    new_turtle.color(color[each])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on =True

while is_race_on:

    for turtles in all_turtle:
        if turtles.xcor() > 280:
            is_race_on = False
            winning_turtle = turtles.pencolor()
            if winning_turtle == user_bet:
                print(f"You've Won ! The {winning_turtle} turtle is the Winner !")
            else:
                print(f"You've Lost ! The {winning_turtle} turtle is the Winner !")


        rand_distance = random.randint(0,10)
        turtles.forward(rand_distance)

screen.exitonclick()