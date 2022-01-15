import turtle
from turtle import *
import random

"creating the variables that we will work with : "
is_race_on = False
all_turtles = []

# configuring the GI(graphic interface) :
title("Race Game created by Ziraoui Anas")

# configuring the screen , size , and the input
screen = Screen()
screen.setup(width=500, height=400)  # this method allows you to change the width and height of the GUI
user_bet = screen.textinput(title="Make your Bet",
                            prompt="which turtle will win the race , Enter a color ? \n colors=red,orange,yellow,green,blue,purple")  # this method will create a pop op window to ask the user , if you want the user to enter a number use num input instead of text input
print(f"user choice is : {user_bet} turtle")

# let's create 6 turtles based on 6 colors
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
for turtle_index in range(6):
    racing_turtle = Turtle(shape="turtle")
    racing_turtle.color(colors[turtle_index])
    racing_turtle.penup()
    racing_turtle.goto(x=-230, y=y_position[
        turtle_index])  # this method allow you to move your turtle whenever you want to , you have to provide x and y values
    all_turtles.append(racing_turtle)
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"Congratulations ,the {winning_turtle} turtle Won")
            else:
                print(f"Oops You Lost , the {winning_turtle} turtle who won the race")
        turtle.forward(random.randint(0, 10))

screen.mainloop()
