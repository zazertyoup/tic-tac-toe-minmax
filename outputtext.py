#for all the text output needed for the game

from random import *
import p_input


def coinflip(players):
    randomGen = randint(0,1)
    print("the first player will be " + (players[randomGen])[0])
    return randomGen

def start(firstplayer):
    print('''to play when it's your turn, write "column, row"''')
    p_input.gridini()
    p_input.who(firstplayer)

def ask():
    return input("where do you want to play ?").split()

def win(who):
    pass

def error(type):
    if type == "O1":
        print("""you didn't give the column or the row or you gave to much values,
         are you sure you used comma betwin values ?""")
    if type == "02":
        print("you gave a value over 3, you know a tic tac toe is only 3 x 3")

