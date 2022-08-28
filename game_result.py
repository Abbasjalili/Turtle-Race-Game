from turtle import Turtle
ALLIGNMENT = "center"
FONT = ("Courier", 10, "bold")


class Result(Turtle):

    def __init__(self):
        super().__init__()    
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(0,0)
    
    def game_over(self, win_color):
        self.write(f"You have lost! The {win_color} turtle is the winner!", align = ALLIGNMENT, font= FONT)

    def win(self, win_color):
        self.write(f"You win! The {win_color} turtle is the winner!", align = ALLIGNMENT, font= FONT)

    

    
