#main file
import outputtext
import gridobject
import p_input

player = nameP, numP = "le joueur", 1
ia = nameI, numI = "l'IA", 2
players = [player, ia]

print("""ce programme est (encore) un morpion servant à experimenter l'algorithme minmax,
le but est donc de rendre ce jeu impossible en utilisant cet algorithme sur l'ia""")


grid = gridobject.tictactoe()


outputtext.coinflip(players)