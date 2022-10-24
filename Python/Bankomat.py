balance = 0

def deposit():
    global balance
    val = int(input("Enter amount to deposit:\n"))
    balance += val
    print(status())


def withdraw():
    global balance
    val = int(input("Enter amount to withdraw:\n"))
    balance -= val
    print(status())

def status():
    return balance

menu = int(input("Menu:\n1.Deposit\n2.Withdraw\n3.Balance\n4.Exit\n"))

if (menu == 1):
    deposit()
elif (menu == 2):
    withdraw()
elif (menu == 3):
    print(status())