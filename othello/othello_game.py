from enum import IntEnum
from itertools import filterfalse, product
from abstracts import Game
from safe_typing import Self, List, Tuple, Dict


class Side(IntEnum):
    DARK = 1
    LIGHT = 2

    @property
    def other(self):
        return Side(3 ^ self)


class Cell(IntEnum):
    EMPTY = 0
    DARK_DISK = 1
    LIGHT_DISK = 2


class OthelloGame(Game):
    n = 8

    directions = tuple(
        filterfalse(lambda x: x == (0, 0), product(range(-1, 2), range(-1, 2)))
    )

    class Play(Game.Action):
        x: int
        y: int
        disk_side: Side

    class Pass(Game.Action):
        pass

    Action = Play | Pass

    class State(Game.State):
        board: Tuple[Tuple[Cell, ...], ...]
        player_turn: Side

    @classmethod
    def S0(cls) -> State:
        mid = cls.n // 2
        disks: Dict[Tuple[int, int], Cell] = {}
        disks[mid - 1, mid - 1] = Cell.LIGHT_DISK
        disks[mid - 1, mid] = Cell.DARK_DISK
        disks[mid, mid - 1] = Cell.DARK_DISK
        disks[mid, mid] = Cell.LIGHT_DISK

        return cls.State(
            tuple(
                tuple(
                    disks[i, j] if (i, j) in disks.keys() else Cell.EMPTY
                    for i in range(cls.n)
                )
                for j in range(cls.n)
            ),
            Side.DARK,
        )

    @classmethod
    def inbound(cls, cell: Tuple[int, int]) -> bool:
        return cell[0] < cls.n and cell[1] < cls.n and 0 <= cell[0] and 0 <= cell[1]

    state: State

    def __init__(self, state: State):
        self.state = state

    def result(self, action: Action) -> Self:
        if isinstance(action, self.Pass):
            return OthelloGame(
                self.State(self.state.board, self.state.player_turn.other)
            )

        cell_status = Cell(action.disk_side)

        changes: Dict[Tuple[int, int], Cell] = {}
        changes[action.x, action.y] = cell_status
        for direction in self.directions:
            for i in range(1, self.n):
                x = action.x + direction[0] * i
                y = action.y + direction[1] * i
                if not self.inbound((x, y)) or self.state.board[x][y] == Cell.EMPTY:
                    break
                if self.state.board[x][y] == cell_status:
                    for j in range(i, 0, -1):
                        x = action.x + direction[0] * j
                        y = action.y + direction[1] * j
                        changes[x, y] = cell_status
                    break
        new_board = tuple(
            tuple(
                changes[i, j] if (i, j) in changes.keys() else self.state.board[i][j]
                for i in range(self.n)
            )
            for j in range(self.n)
        )
        return OthelloGame(self.State(new_board, self.state.player_turn.other))

    def action(self) -> List[Action]:
        board = self.state.board
        player_disk_cell_status = Cell(self.state.player_turn)

        ans = set()
        for cell in (
            (x, y)
            for x in range(self.n)
            for y in range(self.n)
            if board[x][y] == Cell.EMPTY
        ):
            for direction in self.directions:
                x = cell[0] + direction[0]
                y = cell[1] + direction[1]
                if self.inbound((x, y)) and board[cell[0] + direction[0]][
                    cell[1] + direction[1]
                ] == Cell(self.to_move().other):
                    for i in range(2, self.n):
                        x = cell[0] + direction[0] * i
                        y = cell[1] + direction[1] * i
                        if not self.inbound((x, y)) or board[x][y] == Cell.EMPTY:
                            break
                        if board[x][y] == player_disk_cell_status:
                            ans.add(self.Play(*cell, self.state.player_turn))
                            break

        return list(ans) if ans else [self.Pass()]

    def is_terminal(self) -> bool:
        if self.action() == [self.Pass()]:
            return self.result(self.Pass()).action() == [self.Pass()]
        return False

    def to_move(self) -> Game.Player:
        return Game.Player(self.state.player_turn)

    def utility(self) -> Dict[Game.Player, int]:
        ans = {i: 0 for i in Game.Player}
        for i in range(self.n):
            for j in range(self.n):
                if self.state.board[i][j] != Cell.EMPTY:
                    ans[Game.Player(self.state.board[i][j])] += 1
                    ans[Game.Player(self.state.board[i][j]).other] -= 1
        return ans
