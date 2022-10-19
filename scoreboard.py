from turtle import Turtle

FONT = ("Arial", 25, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(0, 250)
        self.write(f"Score: {self.score}", 
                    False, 
                    align="center", 
                    font=FONT
                    )
        

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}",
                   False,
                   align="center",
                   font=FONT
                   )

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", align="center", font=FONT)
