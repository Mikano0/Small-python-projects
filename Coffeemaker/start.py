import turtle
import random
colors = ("red", "blue", "green", "cyan", "pink", "purple", "black", "grey", "orange", "coral", "cyan1")

screen = turtle.Screen()
tur = turtle.Turtle()
tur.shape("turtle")
tur.color(random.choice(colors))

tur.forward(250)
tur.left(90)
tur.color(random.choice(colors))
tur.forward(250)
tur.left(90)
tur.color(random.choice(colors))
tur.forward(250)
tur.left(90)
tur.color(random.choice(colors))
tur.forward(250)
tur.left(90)

print(screen.canvheight)



screen.exitonclick()
