from random import randint

player = 0
computer = 0
for count in range(0,6):
    input("Enter to start")
    p = randint(1, 6)
    c = randint(1, 6)
    player += p
    computer += c

    print("Results:")
    print(p)
    print(c)
    
print(f"Player: {player}")
print(f"Computer: {computer}")

if (player > computer):
    print("Player wins")
elif(player < computer):
    print("Computer wins")
else:
    print("DRAW")