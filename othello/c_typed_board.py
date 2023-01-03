from ctypes import c_short

from safe_typing import Self


class Board:
    Array = c_short * (64 * 10**6)
    array = Array()
    counter = 0

    class Row:
        def __init__(self, array, offset: int, size: int) -> None:
            Board.array = array
            self.offset = offset
            self.size = size

        def __getitem__(self, index: int):
            from .othello_game import Cell

            if index >= self.size:
                raise IndexError
            return Cell(Board.array[self.offset + index])

        def __setitem__(self, index: int, value: int):
            if index >= self.size:
                raise IndexError
            Board.array[self.offset + index] = value

    def __init__(self, n: int) -> None:
        self.offset = self.counter
        type(self).counter += n**2
        self.size = n

    def __getitem__(self, index: int):
        if index >= self.size:
            raise IndexError
        return self.Row(Board.array, self.offset + index * self.size, self.size)

    def copy(self) -> Self:
        new = Board(self.size)
        Board.array[new.offset : new.offset + new.size**2] = Board.array[
            self.offset : self.offset + self.size**2
        ]
        return new
