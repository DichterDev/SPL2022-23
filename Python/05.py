import random

num = 0
sum = 0

while num != 15:
    if (num == 25):
        sum = sum + num
        break
    sum = sum + num
    num = random.randint(10, 30)

print(sum)