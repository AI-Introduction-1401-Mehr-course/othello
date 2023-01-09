from typing import Callable, Dict

# from othello import OthelloGame
from abstracts import Game
from othello import TranspositionTable, StateUnknown


class TranspositionSearchWrapper:
    def __init__(
        self,
        _search: Callable[[Game], Dict[Game.Player, int]],
        _table: TranspositionTable,
    ):
        self.search = _search
        self.table = _table

    def __call__(self, game: Game):
        try:
            r = self.table.get(game.state)
        except StateUnknown:
            r = self.search(game)
            self.table.update(game, r)

        return r
