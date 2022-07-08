#dedicated to receive and understand player's input or false inputs from IA
import outputtext

def who(player):
    if player == 1:
        answer = outputtext.ask()
        confirm(answer)

def confirm(answer):
    confirm = False
    pos = [1,2,3]
    testlong = 0
    testcorrespond = 0
    for i in answer:
        testlong = testlong + 1
        for I in pos:
            if i == I:
                testcorrespond = testcorrespond + 1
    if testlong == 2 & testcorrespond == 2:
        confirm = True
    else:
        if testlong != 2:
            outputtext.error("01")
        if testcorrespond
            
    return confirm