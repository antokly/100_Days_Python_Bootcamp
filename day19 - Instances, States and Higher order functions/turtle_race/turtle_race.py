from turtle import *
import random

# Set up the screen
screen = Screen()
screen.title("Turtle Race!")
screen.setup(width=800, height=400)

# Global variables for turtles and user bet
turtles = []
colors = ["red", "blue", "green"]
user_bet = None

def init_race():
    '''
    race initialization
    '''
    global turtles
    start_x = -350
    start_y = 100
    gap = 60

    turtles.clear()
    for idx, color in enumerate(colors):
        t = Turtle(shape="turtle")
        t.color(color)
        t.penup()
        t.goto(start_x, start_y - idx * gap)
        turtles.append(t)

def race_step():
    for t in turtles:
        t.forward(random.randint(1, 10))

def check_winner():
    finish_line = 350  # x coordinate for finish
    for t in turtles:
        if t.xcor() >= finish_line:
            return t.color()[0]  # Return the color of the winning turtle
    return None

def turtle_race():
    '''
    turtle race process
    '''
    winner_color = None

    while winner_color is None:
        race_step()
        winner_color = check_winner()

    hideturtle()
    penup()
    goto(0, -150)
    color(winner_color)
    write(f"The {winner_color.upper()} turtle wins!", align="center", font=("Arial", 24, "bold"))

    if user_bet == winner_color:
        goto(0, -180)
        write("You guessed right! ", align="center", font=("Arial", 18, "normal"))
    else:
        goto(0, -180)
        write(f"Your bet was {user_bet.upper()}. Better luck next time!", align="center", font=("Arial", 18, "normal"))

if __name__ == "__main__":

    # Pop up to select a turtle color
    user_bet = screen.textinput("Your Bet", f"Which turtle will win? Choose a color: {', '.join(colors)}").strip().lower()

    while user_bet not in colors:
        user_bet = screen.textinput("Your Bet", f"Please choose a valid color: {', '.join(colors)}").strip().lower()

    init_race()

    turtle_race()

    screen.exitonclick()