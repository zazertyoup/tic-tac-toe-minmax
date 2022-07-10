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

    def check(self):
        for I in self.grid:
            for i in I:
                if i == "X":


