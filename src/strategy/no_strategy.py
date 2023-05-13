import random

from src.strategy.strategy import Strategy


class NoStrategy(Strategy):
    def __init__(self, board):
        super().__init__(board)

    def move(self):
        column = random.randint(0,self._board.width-1)
        return column
