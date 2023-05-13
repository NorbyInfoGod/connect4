from src.board.board import Board
from src.game import Game
from src.player.computer import Computer
from src.player.human import Human
from src.strategy.medium import MediumStrategy
from src.strategy.no_strategy import NoStrategy

while True:
    board = Board(6, 7)
    match input("1 - Easy\n2 - Medium\n3 - Exit\n> "):
        case '1':
            strategy = NoStrategy(board)
            match input("Do you want to start first?\n1 - Yes\n2 - No\n> "):
                    case '1':
                        Game(board, Human(board), Computer(board, strategy))
                    case '2':
                        Game(board, Computer(board, strategy), Human(board))
                    case _:
                        print("Invalid input!")
        case '2':
            strategy = MediumStrategy(board)
            match input("Do you want to start first?\n1 - Yes\n2 - No\n> "):
                case '1':
                    Game(board, Human(board), Computer(board, strategy))
                case '2':
                    Game(board, Computer(board, strategy), Human(board))
                case _:
                    print("Invalid input!")
        case '3':
            print("bye")
            break
        case _:
            print("Invalid input!")
