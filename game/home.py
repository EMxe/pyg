# Oliver

import math
import pickle
import time

def game(save_file):
    print("Hero is level", Hero)
    print("Evil is level", Enemy)

ver = 1
while ver != "X":
    print("Welcome to Herterra")
    ver = input("N for new game, L to load or X to exit: ")

    if ver == "N":
        saver = 1
        while saver == 1:
            save_file = input("Enter name for save: ")

            if save_file == "X":
                saver == 0
                break

            try:
                open((save_file + ".pkl"), "rb")
                print(save_file, "is already being used, try a diferent name: ")
            except:
                with open((save_file + ".pkl"), "wb") as f:
                    import base
                    pickle.dump([base.Hero, base.Enemy], f)
                with open((save_file + ".pkl"), "rb") as f:
                    pickle.load(f)
                    print("save created")
                saver == 0
                game(save_file)

    elif ver == "L":
        loader = 1
        while loader == 1:
            save_file = input("Enter save name or X to back: ")

            if save_file == "X":
                loader == 0
                break

            try:
                with open((save_file + ".pkl"), "rb") as f:
                    pickle.load(f)
                print("save loaded")
                loader = 0
                game(save_file)
            except:
                print("The save", save_file, "does not exist.")
