#turtle 1
from turtle import *
color('red')
speed(-1)
left(30)
for i in range(4):
    forward(100)
    right(60)
    forward(100)
    right(120)
    forward(100)
    right(60)
    forward(100)
    right(30)

#turtle2
clearscreen()
from turtle import *
shape("turtle")
speed(-1)
for n in range (3, 7):
    for i in range (n):
        if n % 2 == 1:
            color('blue')
        else:
            color('red')
        forward(100)
        left(360 / n)
