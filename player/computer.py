from src.player.player import Player


class Computer(Player):
    def __init__(self, board,strategy):
        super().__init__(board)
        self._strategy = strategy
    def move(self, column, value):
        column = self._strategy.move()
        while self.check_column_full(column):
            column = self._strategy.move()
        self._board.place(column, value)
    def check_column_full(self, column):
        return self._board.check_column_full(column)
