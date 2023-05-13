from abc import ABC, abstractmethod

from src.board.cell import Cell


class Strategy(ABC):
    def __init__(self, board):
        self._board = board
    @abstractmethod
    def move(self, *args):
        pass

