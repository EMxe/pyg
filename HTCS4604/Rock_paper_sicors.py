import random

li = ["rock", "paper", "sicors"]
w = 0
d = 0
l = 0

welcome=input("Hi, enter 1 to start the game!: ")

while welcome == "1":
    pick=input("pick (r)ock, (p)aper or (s)icors:")
    if pick == "r" or pick == "p" or pick == "s":
        ai=(random.choice(li))
        if pick == "r":
            if ai == "rock":
                print("draw!")
                d=d+1
            elif ai == "paper":
                print("you loose!")
                l=l+1
            elif ai == "sicors":
                print("you win!")
                w=w+1
        if pick == "p":
            if ai == "rock":
                print("you win!")
                w=w+1
            elif ai == "paper":
                print("draw!")
                d=d+1
            elif ai == "sicors":
                print("you loose!")
                l=l+1
        if pick == "s":
            if ai == "rock":
                print("you loose!")
                l=l+1
            elif ai == "paper":
                print("you win!")
                w=w+1
            elif ai == "sicors":
                print("draw!")
                d=d+1
    print("the score is ",w,"wins, ",d,"draws and ",l,"losses!")
    if w == 3:
        welcome = input("You won! \n enter 1 to play again: ")
    elif l == 3:
        welcome = input("You lost! \n enter 1 to play again: ")
