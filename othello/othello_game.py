from safe_typing import Callable, Dict

from .othello_state_space import OthelloStateSpace, Side


class OthelloGame:
    Player = Callable[[OthelloStateSpace], OthelloStateSpace.Action]

    def __init__(self, players: Dict[Side, Player]):
        self.board_state = OthelloStateSpace.initial_board()
        self.players = players

    def run(self):
        while not self.board_state.is_goal():
            action = self.players[self.board_state.playing_side](self.board_state)
            self.board_state = self.board_state.result(action)
        return self.board_state.value
