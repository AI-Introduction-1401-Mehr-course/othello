from typing import Dict
import pickle
from othello_state_space import OthelloStateSpace
class TranspositionTable:
    _table: Dict[OthelloStateSpace.State,int]

    def __init__(table = {}):
        self._table = table
    
    @staticmethod
    def load(filepath):
        with open(filepath, 'rb') as f:
            table = pickle.load(f)
            return TranspositionTable(table)
    
    def dump(filepath: str):
        with open(filepath, 'wb') as f:
            pickle.dump(self._table, f)

    def get(state: OthelloStateSpace.State):
        h = -1
        if self._table.has_key(state):
            h = self._table[state]
        return h
    
    def update(state: OthelloStateSpace.State, value: int):
        self._table[state] = value
