#dedicated to receive and understand player's input or false inputs from IA
import outputtext
import gridobject


def gridini():
    grid = gridobject.tictactoe()

def who(player):
    if player == 0:
       playerturn()

def playerturn():
    answer = outputtext.ask()
    confirm = confirm(answer)
    if confirm == True:
        grid.update(0)
    else:
        playerturn()

def confirm(answer):
    confirm = False
    pos = [1,2,3]
    testlong = 0
    testcorrespond = 0
    for i in answer:
        testlong = testlong + 1
        for I in pos:
            if int(i) == I:
                testcorrespond = testcorrespond + 1
    if testlong == 2 & testcorrespond == 2:
        confirm = True
    else:
        if testlong != 2:
            outputtext.error("01")
        if testcorrespond != 2:
            outputtext.error("02")
    return confirm