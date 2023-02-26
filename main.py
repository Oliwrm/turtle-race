from turtle import Turtle,Screen
import random
race_on=False
screen=Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a colour: ")
print(user_bet)


colours=["red","orange","yellow","green","blue","purple"]
x=0
all_turt=[]

for turt in colours:
    turt=Turtle(shape="turtle")
    turt.color(colours[x])
    turt.penup()
    turt.goto(x=-230,y=(-80+30*x))
    x+=1
    all_turt.append(turt)

if user_bet:
    race_on=True

while race_on:

    for turtle in all_turt:
        if turtle.xcor()>230:
            winner=turtle.pencolor()
            if winner==user_bet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")
            race_on=False
        random_distance=random.randint(0,10)
        turtle.forward(random_distance)



screen.exitonclick()