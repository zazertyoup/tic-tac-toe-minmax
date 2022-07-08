#main file
import outputtext
import gridobject
import p_input

player = nameP, numP = "the player", 1
ia = nameI, numI = "the IA", 2
players = [player, ia]

print("""this programm is an impossible tic tac toe that uses the minmax algorithm""")


grid = gridobject.tictactoe()


outputtext.coinflip(players)