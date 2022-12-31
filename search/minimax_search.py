from abstracts import Search, Game
from safe_typing import Dict


class MinimaxSearch(Search):
    def __call__(self, game: Game) -> Dict[Game.Player, int]:
        if game.is_terminal():
            return game.utility()
        return max(
            (self(game.result(action)) for action in game.action()),
            key=lambda x: x[game.to_move()],
        )
