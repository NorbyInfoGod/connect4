from tabulate import tabulate
from src.board.cell import Cell

EMPTY_CELL = -99
X_CELL = 1
O_CELL = 0

class Board:
    def __init__(self, height, width):
        self._height = height
        self._width = width
        self._cells = []
        self._load_start()
        self._last_placed_cell_coordinates = {"row": -1, "column": -1}
        self._second_to_last_placed_cell_coordinates = {"row": -1, "column": -1}
    @property
    def width(self):
        return self._width
    @property
    def height(self):
        return self._height
    def read_cell(self, row, column):
        return self._cells[row][column].value
    def get_human_last_move_coordinates(self, column):
        i=1
        while self._cells[i][column].value == EMPTY_CELL:
            i+=1
        return i, column
    def check_column_full(self, column):
        sum=0
        for i in range(1,self._height):
            sum+=self._cells[i][column].value
        if sum<0:
            return False
        return True

    def _load_start(self):
        for i in range(self._height+1):
            self._cells.append([])
            for j in range(self._width):
                self._cells[i].append(Cell())

    def possible_solutions(self, row, column):
        if column-3<0: start=0
        else: start = column-3
        if column+3>self.width: fin = self.width-3
        else: fin = column
        for i in range(start, fin):
            possible_solution = [self._cells[row][i].value, self._cells[row][i+1].value,self._cells[row][i+2].value, self._cells[row][i+3].value]
            if (sum(possible_solution) == -96 or sum(possible_solution) == EMPTY_CELL):
                if row == self._height:
                    return i+possible_solution.index(EMPTY_CELL)
                elif self._cells[row + 1][possible_solution.index(EMPTY_CELL)].value != EMPTY_CELL:
                    return i+possible_solution.index(EMPTY_CELL)

        if row<5:
            if sum([self._cells[row][column].value, self._cells[row+1][column].value,self._cells[row+2][column].value]) == 3 or sum([self._cells[row][column].value, self._cells[row+1][column].value,self._cells[row+2][column].value]) == 0:
                return column

        return None

    def __str__(self):
        string_representation = [[]]
        for i in range(1,self._width+1):
            string_representation[0].append(i)
        for i in range(1,self._height+1):
            string_representation.append([])
            for j in range(self._width):
                if i>0:
                    string_representation[i].append(self._cells[i][j].str)
        print(tabulate(string_representation, tablefmt="fancy_grid"))

    @property
    def coordinates_last(self):
        return self._last_placed_cell_coordinates["row"], self._last_placed_cell_coordinates["column"]

    @property
    def coordinates_second_to_last(self):
        return self._second_to_last_placed_cell_coordinates["row"], self._second_to_last_placed_cell_coordinates["column"]
    def place(self,column,value):
        row=1
        while self._cells[row][column].value == EMPTY_CELL and row < self._height:
            row+=1
        if self._cells[row][column].value != EMPTY_CELL:
            row-=1
        self._cells[row][column].value = value
        self._second_to_last_placed_cell_coordinates["row"] = self._last_placed_cell_coordinates["row"]
        self._second_to_last_placed_cell_coordinates["column"] = self._last_placed_cell_coordinates["column"]
        self._last_placed_cell_coordinates["row"] = row
        self._last_placed_cell_coordinates["column"] = column

    def return_winner(self):
        line_values = []
        for i in range(1,self._height+1):
            for j in range(self._width-3):
                line_values.append(self._cells[i][j].value + self._cells[i][j+1].value + self._cells[i][j+2].value + self._cells[i][j+3].value)
        for i in range(1,self._height-2):
            for j in range(self._width):
                line_values.append(self._cells[i][j].value + self._cells[i+1][j].value + self._cells[i+2][j].value + self._cells[i+3][j].value)
        for i in range(1,self._height-2):
            for j in range(self._width-3):
                line_values.append(self._cells[i][j].value + self._cells[i+1][j+1].value + self._cells[i+2][j+2].value + self._cells[i+3][j+3].value)
        for i in range(1,self._height-2):
            for j in reversed(range(self._width-3)):
                line_values.append(self._cells[i][j].value + self._cells[i+1][j-1].value + self._cells[i+2][j-2].value +  self._cells[i+3][j-3].value)

        for value in line_values:
            if value == X_CELL * 4:
                return "Player One"
            elif value == EMPTY_CELL:
                return "Player Two"
        return None


