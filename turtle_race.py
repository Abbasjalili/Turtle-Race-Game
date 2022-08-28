# Created by AB Jalili
# This is part of the 100 projects 100Days Campaign.


from turtle import Turtle, Screen
import random
from game_result import Result


is_race_on = False
screen = Screen()
screen.setup(width = 500, height= 400)
screen.title('Turtale Race')
result = Result()
user_bet = screen.textinput(title = "Make your bet", prompt= "which turtle will win the race? Enter a color: \n red / black /purple / gree / orange / blue ")
color_list = ["red", "black", "purple", "green", "orange", "blue"]
y_pos = [-70, -40, -10, 20, 50, 80]



turtles = []
for i in range(0, 6):
    t = Turtle(shape = "turtle")
    t.penup()
    t.color(color_list[i])
    t.goto(x = -230, y = y_pos[i])
    turtles.append(t)

if user_bet:
    is_race_on = True            


 
        
while is_race_on:    
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            win_color = turtle.pencolor()

            if win_color == user_bet:
                result.win(win_color)       
            else:
                result.game_over(win_color)

                           
                
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
        






screen.exitonclick()