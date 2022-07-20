#for all the text output needed for the game

from random import *
import pinput



def coinflip(players):
    randomGen = randint(0,1)
    print("the first player will be " + (players[randomGen])[0])
    return randomGen

def start(firstplayer):
    print('''to play when it's your turn, write "column, row"''')
    p_input = pinput.p_input()
    p_input.who(firstplayer)

def ask():
    return input("where do you want to play ?")

def win(who):
    if who == 0:
        print("wow you won, impressive i guess my algorithm is not that good")
    else:
        print("the IA just won")

def error(type):
    if type == "O1":
        print("""you didn't give the column or the row or you gave to much values,
         are you sure you used comma betwin values ?""")
    if type == "02":
        print("you gave a value over 3, you know a tic tac toe is only 3 x 3")

def show(grid):
    print(grid[0][0] + "|" + grid[1][0] + "|" + grid[2][0] + """
""" + "-----------" + """
""" + grid[0][1] + "|" + grid[1][1] + "|" + grid[2][1] + """
""" + "-----------" + """
""" + grid[0][2] + "|" + grid[1][2] + "|" + grid[2][2])