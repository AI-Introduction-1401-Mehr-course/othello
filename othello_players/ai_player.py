from abstracts import Search, Game
from runner import Runner


class AIPlayer:
    def __init__(self, search: Search) -> None:
        self.search = search

    def __call__(self, game: Game, context: Runner.Context) -> Game.Action:
        return max(
            game.action(), key=lambda x: self.search(game.result(x))[game.to_move()]
        )
