import random

num1 = random.randint(0, 100)
num2 = random.randint(0, 100)

if (num1 < num2 and num1 < 50):
    print("Zahl 1 ist kleiner als Zahl 2 und Mini")

if (num1 < 30 or num2 < 30):
    print("Eine der beiden ist kleiner als 30")

if (num1 < 50 and num2 != 50):
    print("Erste Zahl ist klein, zweite ist kein 50iger")
