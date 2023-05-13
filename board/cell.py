
EMPTY_CELL = -99
X_CELL = 1
O_CELL = 0
class Cell:
    def __init__(self):
        self._value = EMPTY_CELL
        self._str = " "
    @property
    def value(self):
        return self._value

    @property
    def str(self):
        return self._str

    @value.setter
    def value(self, newvalue):
        self._value = newvalue
        if self._value == O_CELL:
            self._str = "O"
        elif self._value == X_CELL:
            self._str = "X"
