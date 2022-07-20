#dedicated to the grid gestion and updates
from dataclasses import dataclass
from re import X
import outputtext

class tictactoe:
    
    grid = [[" 1 ", " 4 ", " 7 "], [" 2 ", " 5 ", " 8 "], [" 3 ", " 6 ", " 9 "]] 
    win = False
    
    def _init_(self):
        pass
    
    def update(self, where, who):
            symbols = [" X ", " O "]
            self.grid[int(where.split(',')[0]) - 1][int(where.split(',')[1]) - 1] = symbols[who]
            self.checkwin(where)
            if self.win == True:
                outputtext.win(who)

    def checkwin(self, last_play):
        if self.grid[int(last_play.split(',')[0]) - 1][0] == self.grid[int(last_play.split(',')[0]) - 1][1] and self.grid[int(last_play.split(',')[0]) - 1][1] == self.grid[int(last_play.split(',')[0]) - 1][2] or self.grid[0][int(last_play.split(',')[1]) - 1] == self.grid[1][int(last_play.split(',')[1]) - 1] and self.grid[1][int(last_play.split(',')[1]) - 1] == self.grid[2][int(last_play.split(',')[1]) - 1] or self.grid[0][0] == self.grid[1][1] and self.grid[1][1] == self.grid[2][2] or self.grid[0][2] == self.grid[1][1] and self.grid[1][1] == self.grid[2][0]:
            self.win = True
    
    def getgrid(self):
        return self.grid 
    
    def getwin(self):
        return self.win
        

