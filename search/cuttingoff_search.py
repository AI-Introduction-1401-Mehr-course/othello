from abstracts import Search, Game
from safe_typing import Dict, Callable


class CuttingoffSearch(Search):
    def __init__(self,evaluation: Callable[[Game], Dict[Game.Player, int]], depth: int) -> None:
        super().__init__()
        self.evaluation = evaluation
        self.depth = depth
    def __call__(self, game: Game, depth:int |None= None) -> Dict[Game.Player, int]:
        if depth is None:
            depth = self.depth
        if depth == 0 :
            return self.evaluation(game)
        if game.is_terminal():
            return game.utility()
        return max(
            (self(game.result(action),depth-1) for action in game.action()),
            key=lambda x: x[game.to_move()],
        )
