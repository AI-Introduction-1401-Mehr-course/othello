from copy import deepcopy
from enum import IntEnum
from itertools import product, filterfalse
from abstracts import StateSpace
from safe_typing import NamedTuple, Self, List


class Cell(IntEnum):
    EMPTY = 0
    DARK_DISK = 1
    LIGHT_DISK = 2


class Side(IntEnum):
    DARK = 1
    LIGHT = 2

    @property
    def other(self):
        return Side(3 ^ self)


class OthelloStateSpace(StateSpace):
    n = 8

    directions = tuple(
        filterfalse(lambda x: x == (0, 0), product(range(-1, 2), range(-1, 2)))
    )

    class Action(NamedTuple):
        x: int
        y: int
        disk_side: Side

    class State(NamedTuple):
        board: List[List[Cell]]
        player_turn: Side

    @classmethod
    def initial_board(cls) -> Self:
        mid = cls.n // 2
        board = [[Cell.EMPTY for __ in range(cls.n)] for _ in range(cls.n)]
        board[mid - 1][mid - 1] = Cell.LIGHT_DISK
        board[mid - 1][mid] = Cell.DARK_DISK
        board[mid][mid - 1] = Cell.DARK_DISK
        board[mid][mid] = Cell.LIGHT_DISK

        return cls(cls.State(board, Side.DARK))

    state: State

    def __init__(self, state: State):
        self.state = state

    def result(self, action: Action) -> Self:
        new_board = deepcopy(self.state.board)
        cell_status = Cell(action.disk_side)

        new_board[action.x][action.y] = cell_status
        for direction in self.directions:
            for i in range(1, self.n):
                x = action.x + direction[0] * i
                y = action.y + direction[1] * i
                if (
                    x >= self.n
                    or y >= self.n
                    or x < 0
                    or y < 0
                    or new_board[x][y] == Cell.EMPTY
                ):
                    break
                if new_board[x][y] == cell_status:
                    for j in range(i, 0, -1):
                        x = action.x + direction[0] * j
                        y = action.y + direction[1] * j
                        new_board[x][y] = cell_status
                    break

        return OthelloStateSpace(self.State(new_board, self.state.player_turn.other))

    def action(self) -> List[Action]:
        board = self.state.board
        player_disk_cell_status = Cell(self.state.player_turn)

        ans = set()
        for cell in (
            (x, y)
            for x in range(self.n)
            for y in range(self.n)
            if board[x][y] == player_disk_cell_status
        ):
            for direction in self.directions:
                if board[cell[0] + direction[0]][cell[1] + direction[1]] == Cell(
                    self.state.player_turn.other
                ):
                    for i in range(2, self.n):
                        x = cell[0] + direction[0] * i
                        y = cell[1] + direction[1] * i
                        if board[x][y] == player_disk_cell_status:
                            break
                        if board[x][y] == Cell.EMPTY:
                            ans.add(self.Action(x, y, self.state.player_turn))
                            break

        return list(ans)

    def cost(self, action: Action) -> int:
        return 1

    def is_goal(self) -> bool:
        return not self.action()
