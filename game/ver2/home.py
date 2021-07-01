# Oliver

# Imports
import math
import pickle
import time
import random
import os
import base

# Actual game
def game(Stats):
    start = 1
    while start == 1: # Start Loop
        begin_game = input("p to play, x to quit or c for other commands: ").lower()
        if begin_game == "p": # Play if p
    
            # Varables
            hero = Stats.Hero
            flight_fail = False
            reset_enc = True
            savenquit = 0
    
            # Game loop
            while hero.health > 0:
                
                # Xp/flight check variables
                flight_fail = False
                win = False
    
                # Encounter
                if reset_enc == True:
                    enct = random.choice(Stats.Enemies)
                reset_enc = True
                
                # Call enemy values
                enemy = [enct.level, enct.exp, enct.attack, enct.health]

                print("You Encountered a", enct.name)
                fof = input("stats, savenquit, fight or flight?: ").lower()
    
                if fof == "stats": # Print hero stats
                    print("\nHero level:", hero.level,
                          "\nHero exp:", hero.exp,
                          "\nHero attack:", hero.attack,
                          "\nHero health:", hero.health, "\n", flush = True)
                    reset_enc = False
    
                elif fof == "savenquit": # save and quit game
                    try:
                        with open((save_file + ".pkl"), "wb") as f:
                            pickle.dump(Stats, f)
                            print("game saved")
                            savenquit = 1
                        break
                    except:
                        print("error")
    
                if fof == "flight": # Flight check
                    flight = random.randrange(1,10)
                    if flight < 7:
                        print("you ran!") # Got away
                        flight_fail = False
                    elif flight > 7:
                        print("you couldn't get away!") # Didn't get away, start encounter
                        flight_fail = True
                        
                if fof == "fight" or flight_fail == True: # Start encounter
                    while hero.health > 0 and enemy[3] > 0:
                        print("Hero did", hero.attack, "to Enemys", enemy[3], "hp")
                        enemy[3] = enemy[3] - hero.health # Hero attack
                        print("Enemy did", enemy[2], "to Heros", hero.health, "hp", flush=True)
                        hero.health = hero.health - enemy[2] # Enemy attack
                        time.sleep(1)
                    if enemy[3] <= 0: # Enemy has fallen
                        print("You slayed the enemy!")
                        Stats.slayn.append(enct.name)
                        win = True
                        # Add to list, win true
                    flight_fail = False # Reset flight
                
                if win == True: # Exp / Level up check
                    hero.exp += (enemy[0] * 1.5) # Exp
                    if hero.level <= hero.exp: # Level
                        hero.exp = 0
                        print("level up!")
                        hero.level += 1
                        win = False
                        hero.attack = 10 + hero.level * 0.8
                        hero.health += 20 + hero.level * 0.8
                time.sleep(0.5)

            if savenquit == 0: # Death, check if you quit or died
                print("you died")
            print("you slayed:",Stats.slayn) # Kill count
            
            after = 1
            while after == 1 and savenquit == 0: # Reset/Delete if dead
                rr = input("R to reset or D to delete save?: ").upper()
                if rr == "R": # Reset
                    try:
                        with open((save_file + ".pkl"), "wb") as f:
                            base_game = base.Game()
                            pickle.dump(base_game, f)
                        print("save reset")
                        after = 0
                    except:
                        print("broke")
                        
                elif rr == "D": # Delete
                    try:
                        os.remove(save_file + ".pkl")
                        print("save deleted")   
                        after = 0
                    except:
                        print("broke")
            start == 0
                
    
        elif begin_game == "c": # Cant be bothered finishing
            print("commands todo")
        elif begin_game == "h":
            print("help todo")
        elif begin_game == "x":
            start == 0
            break


ver = 1
while ver != "X": # Menu loop
    print("Welcome to Herterra")
    ver = input("N for new game, L to load, D to delete or X to exit: ").upper()

    if ver == "N": # New game
        saver = 1
        while saver == 1:
            save_file = input("Enter name for save: ").upper() # Name

            if save_file == "X": # Quit if X
                saver == 0
                break

            try: # If we can open a file with that name
                open((save_file + ".pkl"), "rb")
                print(save_file, "is already being used, try a diferent name: ")
            except: # If breaks, create save
                try: # Create save
                    with open((save_file + ".pkl"), "wb") as f:
                        base_game = base.Game()
                        pickle.dump(base_game, f)
                    with open((save_file + ".pkl"), "rb") as f:
                        Stats = pickle.load(f)
                        print("save created")
                    saver = 0
                    game(Stats)
                except: # Bad name
                    print("name not correct")

    elif ver == "L": # Load game
        loader = 1
        while loader == 1:
            save_file = input("Enter save name or X to back: ").upper() # Name

            if save_file == "X": # Quit if X
                loader == 0
                break

            try: # Load save
                with open((save_file + ".pkl"), "rb") as f:
                    Stats = pickle.load(f)
                print("save loaded")
                loader = 2

            except: # Cant load save
                print("The save", save_file, "does not exist.")

            if loader == 2: # Run game if loaded
                game(Stats)
    
    elif ver == "D": # Delete
        deleter = 1
        while deleter == 1:
            save_file = input("Enter save name or X to back: ").upper() # Name

            if save_file == "X": # Qut if X
                deleter == 0
                break

            try: # Delete save
                os.remove(save_file + ".pkl")
                print("save deleted")
                deleter = 0
            except: # Save doesn't exist
                print("The save", save_file, "does not exist.")
