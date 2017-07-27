#Ex1

mass = float(input("What's your weight?"))
height = float(input("What's your height?"))
m = height/100
bmi = mass/(m*m)
print("Yours Body Mass Index is", bmi)
if bmi < 16:
    print("You're severely underweighted")
elif 16 <= bmi <18.5:
    print("You're underweighted")
elif 18.5 <= bmi <25:
    print("You're normal")
elif 25 <= bmi < 30:
    print("You're overweight")
else:
    print("You're obese")

#Ex2
print("Hello", end="")
print(", my name", end="")
print(" is B-max")

#Ex3
#3.1
for i in range(17):
    print("*", end="")
print()

#3.2
for i in range(17):
    print("x*", end="")
print()

#3.3
row = int(input("How many Row?"))
collumn = int(input("How many collumn?"))
for i in range (row):
    for n in range(collumn):
        if i % 2 == 0:
            print("x*", end = '')
        else:
            print("*x", end = '')
    print()
