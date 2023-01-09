from typing import Dict, Tuple
import pickle
from abstracts import Game


class StateUnknown(Exception):
    pass
class TranspositionTable:
    _table: Dict[Game.State, Tuple[int, Game.Action]]

    def __init__(self, table={}):
        self._table = table

    @staticmethod
    def load(filepath):
        with open(filepath, "rb") as f:
            table = pickle.load(f)
            return TranspositionTable(table)

    def dump(self, filepath: str):
        with open(filepath, "wb") as f:
            pickle.dump(self._table, f)

    def get(self, state: Game.State):
        if state in self._table:
            return self._table[state]
        else:
            raise StateUnknown

    def update(self, state: Game.State, value: Tuple[int, Game.Action]):
        self._table[state] = value
