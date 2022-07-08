#for all the text output needed for the game

from random import *


def coinflip(players):
    randomGen = randint(1,2)
    print("the first player will be " + (players[randomGen - 1])[0])
    return randomGen

def start(firstplayer):
    print("to play when it's your turn, write")

def ask():
    return input("ou veux tu jouer ?").split()

def error(type):
    if type == "O1":
        print("""les valeurs données ne sont pas en bonne quantité
            les as tu bien séparées d'une virgule ?""")
    

