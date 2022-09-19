import random

num = random.randint(0, 100)

print(num)

if (num < 20):
    print("Mini")
elif (num < 50):
    print("Medium")
elif (num > 50):
    print("Large")