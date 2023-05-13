from src.player.human import Human
EMPTY_CELL = -99
X_CELL = 1
O_CELL = 0
class Game:
    def __init__(self, board, player1, player2):
        self._board = board
        self._player_one = player1
        self._player_two = player2
        self._turn_count = 1
        self.play()
    def play(self):
        while True:
            if self.move(self._player_one, X_CELL):
                break
            if self.move(self._player_two, O_CELL):
                break
    def read_input(self):
        user_input = int(input("> "))-1
        if user_input<0 or user_input>self._board.width-1:
            raise ValueError
        return user_input
    def draw_board(self):
        return self._board.__str__()

    def move(self, player, value):
        row, column = -1, -1
        if type(player) is Human:
            self.draw_board()
            while True:
                try:
                    column = self.read_input()
                    break
                except ValueError:
                    print("Invalid Input! Out of bounds")
            while player.check_column_full(column):
                print("Column already full!")
                column = self.read_input()
        player.move(column, value)
        self._turn_count +=1
        if self.winner():
            self.draw_board()
            print(f"{type(player).__name__} won!")
            return True
        if self._turn_count > self._board.width*self._board.height:
            self.draw_board()
            print("It's a draw!")
            return True
        return False

    def winner(self):
        return self._board.return_winner()

