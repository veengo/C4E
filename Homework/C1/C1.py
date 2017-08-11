#2.1
response = input("What is your radius? ")
r = float(response)
area = 3.14159 * r**2
print(area)

#2.2
response = input("What is your radius? ")
r = float(response)
area = 3.14159 * r**2
print("area = ", area)

#3.1
Celsius = int(input("Enter a temperature in Celsius: "))
Fahrenheit = 9.0/5.0 * Celsius + 32
print (Fahrenheit)

#3.2
Celsius = int(input("Enter a temperature in Celsius: "))
Fahrenheit = 9.0/5.0 * Celsius + 32
print (Celsius, “(C)”, “ = “, Fahrenheit, " (F)")

#Turtle
#1
from turtle import *
speed(-1)
shape("turtle")
for i in range (4):
    forward(100)
    left(90)
mainloop()

#2
from turtle import *
speed(-1)
shape("turtle")
for i in range (3):
    forward(100)
    left(120)
mainloop()

#3
from turtle import *
speed(-1)
shape("turtle")
circle(100)

#4
from turtle import *
speed(-1)
shape("turtle")
for i in range(6):
    circle(100)
    left(60)
mainloop()

#5
from turtle import *
speed(-1)
shape("turtle")
for i in range(36):
    circle(100)
    left(10)
mainloop()
