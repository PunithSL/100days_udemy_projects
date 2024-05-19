from turtle import Turtle,Screen

timmy_turtle = Turtle()
screen = Screen()

def move_forwards():
    timmy_turtle.forward(10)

def move_backwards():
    timmy_turtle.backward(10)

def rotate_clockwise():
    timmy_turtle.right(10)

def rotate_anticlockwise():
    timmy_turtle.left(10)

def clear():
    timmy_turtle.reset()

screen.listen()
screen.onkey(key="w",fun=move_forwards)
screen.onkey(key="s",fun=move_backwards)
screen.onkey(key="a",fun=rotate_clockwise)
screen.onkey(key="d",fun=rotate_anticlockwise)
screen.onkey(key="c",fun=clear)
screen.exitonclick()