from random import randint
from .othello_game import OthelloGame, Cell
from operator import xor
from functools import reduce

table = {
    (i, j, k): randint(0, 2**32)
    for i in range(OthelloGame.n)
    for j in range(OthelloGame.n)
    for k in Cell
}


def zobrist_hash(state: OthelloGame.State):
    return reduce(
        xor,
        (
            table[i, j, state.board[i][j]]
            for i in range(OthelloGame.n)
            for j in range(OthelloGame.n)
        ),
    )
