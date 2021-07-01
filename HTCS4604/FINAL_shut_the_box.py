# Oliver
# 22/06/2021
# Simple shut the box game for assessment

# Imports
import random
import time

# Variables
og = [1, 2, 3, 4, 5, 6, 7, 8, 9]
drop = []
turns = 0
die1 = 0
die2 = 0
w = 0
l = 0
finished = 0
summy = 1
p1_total = 0
p2_total = 0

# What happens to give the ai a score
def ai():
    # Globalize variables
    global og, finished, summy, p1_total, p2_total, drop, die1, die2, turns

    print("AI's turn",  flush = True)
    time.sleep(1)    
    while finished == 0: # WLoop to keep em rolling

        dice_count = random.choice(range(1, 9)) # Choose a random number from 1-9 based on whats left

        if dice_count in range(1,2): # If choice in 1-3, roll 1 dice
            die1 = random.choice(range(1, 6))
            die2 = 0
        elif dice_count in range(3,9): # If choice in 4-9, roll 2 dice
            die1 = random.choice(range(1, 6))
            die2 = random.choice(range(1, 6))
        added = die1 + die2 # Add dice
        summy = 0

        while summy == 0: # Loop to keep em guessing
            if dice_count == 1: # Print if 1 roll
                print("\nAI rolled a", die1)
            elif dice_count == 2 or 3 or 4: # Print if 2 rolls
                print("\nAI rolled", die1, "and", die2, "which is ", added)
            turns += 1 # Add a count to their turn

            possible = list(subset_sum(og, added)) # Check if there are any moves left

            if possible:

                down = random.choice(list(possible))# Random choice based on moves left
                print("AI picked", down)

                # Remove pieces from board
                remaining_og = [x for x in og if x not in down]
                og = remaining_og
                drop.extend(down)
                summy = 1
                print("left down:", remaining_og)

            elif not possible: # If no more moves
                print("all combinations reached")
                print("AI scored", sum(drop), "in", turns, "turns") # Ai score and turns taken

                # Reset all variables
                summy = 1
                finished = 1
                remaining_og = []
                og = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                p2_total += sum(drop)
                drop = []
    # Reset while loop data
    summy = 1
    finished = 0

# What happens when player makes a turn
def turn(p):
    global og, finished, summy, p1_total, p2_total, drop, turns

    print(f"{p}'s turn",  flush = True)
    time.sleep(1)
    while finished == 0: # WLoop to keep em rolling
        dice_count = input(f"\n{p}, roll 1 dice or 2?: ")
        dice_count = dice_count.lower() # Roll check

        if dice_count == "1": # 1 random number 1-6
            die1 = random.choice(range(1, 6))
            die2 = 0
            added = die1 + die2
            summy = 0
        elif dice_count == "2": # 2 random number 1-6
            die1 = random.choice(range(1, 6))
            die2 = random.choice(range(1, 6))
            added = die1 + die2 # Total
            summy = 0

        elif dice_count == "skip" or dice_count == "q": # Quit if skip/q
            if p == "Player 1" or p == "Player": # Clear score for whoever is playing
                p1_total = 0
            elif p == "Player 2":
                p2_total = 0           
            summy = 1 # Reset vairiables
            finished = 1
            remaining_og = []
            og = [1, 2, 3, 4, 5, 6, 7, 8, 9]            
            break

        elif dice_count == "max":
            if p == "Player 1" or p == "Player":
                p1_total = 45
                print("you scored", p1_total, flush = True)
            elif p == "Player 2":
                p2_total = 45
                print("you scored", p2_total, flush = True)
            time.sleep(1)
            summy = 1
            finished = 1
            remaining_og = []
            og = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        while summy == 0:
            if dice_count == "1":
                print("\nYou rolled a", die1)
            elif dice_count == "2":
                print("\nYou rolled", die1, "and", die2, "which is ", added)
            turns += 1
            
            print("Numbers up:", og)

            possible = list(subset_sum(og, added))
            if possible:

                bring = input("Enter numbers with spaces between: ")
                bring = bring.lower()

                if bring == "skip" or bring == "q":
                    if p == "Player 1" or p == "Player":
                        p1_total = 0
                    elif p == "Player 2":
                        p2_total = 0
                    summy = 1
                    finished = 1
                    remaining_og = []
                    og = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    break
        
                elif bring == "max":
                    if p == "Player 1" or p == "Player":
                        p1_total = 45
                        print("you scored", p1_total, flush = True)
                    elif p == "Player 2":
                        p2_total = 45
                        print("you scored", p2_total, flush = True)
                    time.sleep(1)
                    summy = 1
                    finished = 1
                    remaining_og = []
                    og = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    break

                try:
                    li = bring.split() # Split parts of input
                    map_li = map(int, li) # Turn parts into int
                    down = list(map_li) # Convert back into list
                    remaining_og = [x for x in og if x not in down] # make list of remaining items

                    # Check for negative numbers
                    neg = 0
                    for i in down:
                        if i < 0:
                            neg = 1

                    # If down adds to added and no neagitves
                    if sum(down) == added and neg == 0:
                        print("numbers left down:", remaining_og)
                        og = remaining_og # Remaining exchange
                        drop.extend(down) # Add numbers to total score list
                        summy = 1 # Leave loop

                    else: # If bad option
                        print("This does not add up or is unavailable.")
                except: # If cant convert to list
                    print("This is not a valid option.")

            else:
                print("all combinations reached", flush = True)
                time.sleep(1)
                print("you scored", sum(drop), "in", turns, "moves", flush = True)
                turns = 0
                summy = 1
                finished = 1
                remaining_og = []
                og = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                time.sleep(2)

                if p == "Player 1":
                    p1_total = sum(drop)
                    drop = []
                elif p == "Player 2":
                    p2_total = sum(drop)
                    drop = []
    summy = 1
    finished = 0

def game(mui):
    global p1_total, p2_total # Globalize
    if mui == "ai": # Run 1 turn and ai turn, compare results
        turn("Player")
        ai()
        if p1_total > p2_total:
            print("Player wins with", p1_total, "to", p2_total)
        if p2_total > p1_total:
            print("AI wins with", p2_total, "to", p1_total)
        elif p2_total == p1_total:
            print("Its a tie! Both players got", p1_total)  

    elif mui == "1": # Run 1 turn
        turn("player")
        print("Player ended with", p1_total)

    elif mui == "2": # Run both players turns, compare results
        turn("Player 1")
        turn("Player 2")
        if p1_total > p2_total:
            print("Player 1 wins with", p1_total, "to", p2_total)
        if p2_total > p1_total:
            print("Player 2 wins with", p2_total, "to", p1_total)
        elif p2_total == p1_total:
            print("Its a tie! Both players got", p1_total)


def subset_sum(numbers, target, partial=[], partial_sum=0): # Find all combinations
    if partial_sum == target:
        yield partial
    if partial_sum >= target:
        return
    for i, n in enumerate(numbers):
        remain = numbers[i + 1:]
        yield from subset_sum(remain, target, partial + [n], partial_sum + n)

while True:
    welcome = input("Welcome. Use 1, 2 or ai " # Input
                    "to play, q for exit or c for other commands: ")
    welcome = welcome.lower()
    
    if welcome == "1" or welcome == "2" or welcome == "ai": # Run game if 1/2/ai
        game(welcome)

    elif welcome == "c": # Commands if c
        print("1: Starts 1 solo round\n"
              "2: Starts player vs player\n"
              "AI: Starts player vs AI\n"
              "q/skip: Exits the game\n"
              "c: Shows all commands\n"
              "h: Explanation of game\n")

    elif welcome == "h": # Help if h
        print("Hello user. This is a game where you are given numbers 1-9. "
              "You can then roll 1 or 2 dice.\nAdd the result up to get "
              "a total. Use any combination of numbers that add up to\nthe "
              "total repeating untill you cant use any more number"
              "combinatons. \nThen player 2 or the ai will take their turn."
              "\nYou win if you can use more numbers than your opponent. "
              "Good luck and have fun!\n")

    elif welcome == "q": # Quit if q
        print("""
              ★─▄█▀▀█║▄██▄║▄██▄║███▄║──★
              ★─█ █▀█║█──█║█──█║█──█║──★
              ★─▀███▀║▀██▀║▀██▀║███▀║──★
              ★────────────────────────★
              ★───▐█▀▄─ ▀▄─▄▀ █▀▀──█───★
              ★───▐█▀▀▄ ──█── █▀▀──▀───★
              ★───▐█▄▄▀ ──▀── ▀▀▀──▄───★""")

        break
    else:
        print("please enter a command")
