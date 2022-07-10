#main file
import outputtext
import gridobject
import p_input

player = nameP, numP = "the player", 0
ia = nameI, numI = "the IA", 1
players = [player, ia]

print("""this programm is an impossible tic tac toe that uses the minmax algorithm""")


outputtext.start(outputtext.coinflip(players))