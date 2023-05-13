import unittest

from src.board.board import Board
from src.game import Game
from src.player.computer import Computer
from src.player.human import Human
from src.strategy.medium import MediumStrategy


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self._height = 6
        self._width = 7
        self._board = Board(self._height, self._width)

    def test_read_cell(self):
        self.assertEqual(self._board.read_cell(1,1), -99)
    def test_check_column(self):
        self.assertEqual(self._board.check_column_full(1), False)

    def test_place(self):
        self._board.place(1,1)
        self._board.place(3,0)
        self._board.place(2,1)
        self._board.place(3,0)
        self.assertEqual(self._board.read_cell(self._height, 1), 1)

    def test_coordinates_last(self):
        self._board.place(1,1)
        self._board.place(3,0)
        row, column = self._board.coordinates_last
        self.assertEqual(row,6)
        self.assertEqual(column, 3)

    def test_coordinates_second_to_last(self):
        self._board.place(1, 1)
        self._board.place(3, 0)
        row, column = self._board.coordinates_second_to_last
        self.assertEqual(row, 6)
        self.assertEqual(column, 1)

    def test_return_winner(self):
        self._board.place(1,1)
        self._board.place(1,1)
        self._board.place(1,1)
        self._board.place(1,1)
        self.assertEqual(self._board.return_winner(), "Player One")

    def test_look_for_win(self):
        self._computer = Computer(self._board, MediumStrategy(self._board))
        self._board.place(1,1)
        self._board.place(1,1)
        self._board.place(1,1)
        self._computer.move(-1, 1)
        self.assertEqual(self._board.return_winner(), "Player One")

    def test_look_for_block(self):
        self._computer = Computer(self._board, MediumStrategy(self._board))
        self._board.place(1,1)
        self._board.place(1,1)
        self._board.place(1,1)
        self._computer.move(-1, 0)
        self.assertEqual(self._board.return_winner(), None)



if __name__ == '__main__':
    unittest.main()
