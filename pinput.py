#dedicated to receive and understand player's input or inputs from IA
import outputtext
import gridobject

class p_input:

    grid = gridobject.tictactoe()

    def __init__(self):
        pass

    def who(self, player):
        if player == 0:
            self.playerturn()
            player = 1
        else:
            player = 0
            pass
            #will be IA turn
        if self.grid.getwin() == True:
            pass
        else:
            outputtext.show(self.grid.getgrid())
            self.who(player)


    def playerturn(self):
        while True:
            answer = outputtext.ask()
            confirmation = self.confirm(answer)
            if confirmation:
                self.grid.update(answer, 0)
                break
            

    def confirm(self, answer):
        confirm = False
        pos = [1,2,3]
        testlong = 0
        testcorrespond = 0
        for a in answer.split(','):
            testlong = testlong + 1
            for b in pos:
                if int(a) == b:
                    testcorrespond = testcorrespond + 1
        if testlong == 2 & testcorrespond == 2:
            confirm = True
        else:
            if testlong != 2:
                outputtext.error("01")
            if testcorrespond != 2:
                outputtext.error("02")
        return confirm