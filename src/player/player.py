from abc import abstractmethod, ABC

from src.board.cell import Cell


class Player(ABC):
     def __init__(self, board):
         self._board = board

     @abstractmethod
     def move(self, *args) -> Cell:
         pass
     @abstractmethod
     def check_column_full(self, *args):
         pass
