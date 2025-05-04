import turtle
import colorsys

# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Colorful Spiral Galaxy")

# Create a turtle
galaxy = turtle.Turtle()
galaxy.speed(0)
galaxy.width(2)
galaxy.hideturtle()

# Set up colors
n = 45  # Number of colors
colors = []
for i in range(n):
    colors.append(colorsys.hsv_to_rgb(i/n, 1, 1))

# Draw spiral galaxy
for i in range(360):
    color = colors[i % n]
    galaxy.pencolor(color)
    galaxy.forward(i * 3 / n + i)
    galaxy.right(59)

# Keep the window open until clicked
screen.exitonclick()