#Oliver

import random
import time

og = [1,2,3,4,5,6,7,8,9]
drop = []
die1 = 0
die2 = 0
w = 0
l = 0
finished = 0
summy = 0
p1_total = 0
p2_total = 0.

def ai():
    global og, finished, summy, p1_total, p2_total, drop, die1, die2
    while finished == 0:
        die_count = random.choice(range(1,2))
        
        if die_count == 1:
            die1 = random.choice(range(1,6))
            die2 = 0
        elif die_count == 2:
            die1 = random.choice(range(1,6))
            die2 = random.choice(range(1,6))
        added = die1 + die2
        summy = 0
        while summy == 0:
            print("\nAI rolled", die1, "and", die2, "which is ", added)
            print("Numbers up:", og)
            
            possible = list(subset_sum(og, added))
            if possible:
                
                bring = random.choice(list(possible))
                print(bring)
                
                map_object = map(int, bring)
                down = list(map_object)
                remaining_og = [x for x in og if x not in down]
                
                if sum(down) == added:
                    print("numbers left down:", remaining_og)
                    og = remaining_og
                    drop.extend(down)
                    summy = 1

            elif not possible:
                print("all combinations reached")
                print("AI scored", sum(drop))
                summy = 1
                finished = 1
                remaining_og = []
                og = [1,2,3,4,5,6,7,8,9]
                
                p2_total += sum(drop)
                drop = []
    summy = 0
    finished = 0

def turn(p):
    global og, finished, summy, p1_total, p2_total, drop
    while finished == 0:
        die_count = input(f"Hello {p}, roll 1 dice or 2?: ")
        
        if die_count == "1":
            die1 = random.choice(range(1,6))
            die2 = 0
        elif die_count == "2":
            die1 = random.choice(range(1,6))
            die2 = random.choice(range(1,6))
        added = die1 + die2
        summy = 0
        while summy == 0:
            print("\nYou rolled", die1, "and", die2, "which is ", added)
            print("Numbers up:", og)
            
            possible = list(subset_sum(og, added))
            if possible:
            
                bring = input("Enter each number with a space between: ")
                
                a_list = bring.split()
                map_object = map(int, a_list)
                down = list(map_object)
                remaining_og = [x for x in og if x not in down]
                
                if sum(down) == added:
                    print("numbers left down:", remaining_og)
                    og = remaining_og
                    drop.extend(down)
                    summy = 1
                    
                elif sum(down) != added:
                    print("This does not add up. Please rechose numbers")
                
                elif down not in remaining_og:
                    print("This does not add up. Please rechose numbers")
                
            elif not possible:
                print("all combinations reached")
                print("you scored", sum(drop))
                summy = 1
                finished = 1
                remaining_og = []
                og = [1,2,3,4,5,6,7,8,9]
                
                if p == "Player 1":
                    p1_total += sum(drop)
                    drop = []
                elif p == "Player 2":
                    p2_total += sum(drop)
                    drop = []
    summy = 0
    finished = 0

def game(mui):
    global p1_total, p2_total
    if mui == "1":
        turn("Player 1")
        ai()
        if p1_total > p2_total:
            print("Player 1 wins with", p1_total, "to", p2_total)
        if p2_total > p1_total:
            print("AI wins with", p2_total, "to", p1_total)
            
    elif mui == "2":
        turn("Player 1")
        turn("Player 2")
        if p1_total > p2_total:
            print("Player 1 wins with", p1_total, "to", p2_total)
        if p2_total > p1_total:
            print("Player 2 wins with", p2_total, "to", p1_total)

def subset_sum(numbers, target, partial=[], partial_sum=0):
    if partial_sum == target:
        yield partial
    if partial_sum >= target:
        return
    for i, n in enumerate(numbers):
        remaining = numbers[i + 1:]
        yield from subset_sum(remaining, target, partial + [n], partial_sum + n)

while og == og:
    welcome = input("Welcome. Press 1 for 1 player or 2 for 2 player, x for exit and h for help: ")
    if welcome == "1" or welcome == "2":
        game(welcome)
    elif welcome == "h":
        print("Hello user. This is a game where you are given numbers 1-9. "
              "You can then roll 1 or 2 dice,\n adding the result up to get a total "
              "Use any combination of numbers to add up to\n the dice total repeating "
              "untill you cant make any more combinatons. \nThen player 2 or the ai will take "
              "their turn. \nYou win if you can use more numbers than your opponent"
              "Good luck and have fun!\n")
    elif welcome == "x":
        break
