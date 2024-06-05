from turtle import *

tur = Turtle()
s = Screen()

colorList = ["orange", "cyan", "pink", "blue", "grey", "brown", "voilet", "silver", "yellow", "green"]
shape("triangle")
tur.speed(0)
for i in range(3, 999):
    #color(colorList[i-3])
    for k in range(0, i):
        forward(1)
        right(360/i)

exitonclick()