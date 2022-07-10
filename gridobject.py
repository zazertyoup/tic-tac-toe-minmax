#dedicated to the grid gestion and updates
from dataclasses import dataclass
from re import X
import outputtext

class tictactoe:
    
    def _init_(self):
        self.grid = [["/", "/", "/"], ["/", "/", "/"], ["/", "/", "/"]] 
    
    def update(self, where, who):
            symbols = ["X", "O"]
            self.grid[where[0] - 1][where[1] - 1] = symbols[who]
            if self. checkwin(where) == True:
                outputtext.win(who)

    def checkwin(self, last_play):
        if self.grid[last_play[0]][0] == self.grid[last_play[0]][1] & self.grid[last_play[0]][1] == self.grid[last_play[0]][2] | self.grid[0][last_play[1]] == self.grid[1][last_play[1]] & self.grid[1][last_play[1]] == self.grid[2][last_play[1]] | self.grid[0][0] == self.grid[1][1] & self.grid[1][1] == self.grid[2][2] | self.grid[0][2] == self.grid[1][1] & self.grid[1][1] == self.grid[2][0]:
            return True
        else:
            return False
                    
        

