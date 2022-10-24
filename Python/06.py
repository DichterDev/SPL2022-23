import random

rnd = random.Random()

def add(num1, num2):
    return num1 + num2

def randInt():
    return rnd.randint(100, 200)

def randString(str):
    index = rnd.randint(0, len(str) - 1)
    return str[index]

print(add(1, 2))
print(randInt())
print(randString(["String", "Integer", "Float", "Double", "Date"]))