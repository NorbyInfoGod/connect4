from src.player.player import Player


class Human(Player):
    def __init__(self, board):
        super().__init__(board)

    def move(self, column, value):
        self._board.place(column,value)
    def check_column_full(self, column):
        return self._board.check_column_full(column)