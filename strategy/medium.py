import random

from src.strategy.strategy import Strategy


class MediumStrategy(Strategy):
    def __init__(self, board):
        super().__init__(board)
    def look_for_win(self, row, column):
        return self._board.possible_solutions(row,column)
    def look_for_block(self, row, column):
        return self._board.possible_solutions(row, column)
    def move(self):
        player_row, player_column = self._board.coordinates_last
        own_row, own_column = self._board.coordinates_second_to_last

        own_column = self.look_for_win(own_row,own_column)
        if own_column is not None:
            return own_column
        player_column = self.look_for_block(player_row, player_column)
        if player_column is not None:
            return player_column

        column = random.randint(0, self._board.width - 1)
        return column
