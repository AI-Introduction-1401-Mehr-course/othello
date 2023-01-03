from copy import copy
from datetime import timedelta, datetime
from safe_typing import Dict, Callable, List, Tuple, NamedTuple
from abstracts import Game


class Runner:
    class Context(NamedTuple):
        finished: bool
        history: List[Tuple[Game.Action, timedelta]]

    def __init__(
        self,
        game: Game,
        players: Dict[Game.Player, Callable[[Game, Context], Game.Action]],
    ) -> None:
        self.game = game
        self.players = players
        self.context = Runner.Context(False, [])

    def run(self):
        while not self.game.is_terminal():
            checkpoint = datetime.now()
            action = self.players[self.game.to_move()](self.game, self.context)
            self.game = self.game.result(action)
            self.context.history.append((action, datetime.now() - checkpoint))
        self.context = Runner.Context(True, self.context.history)

        for player in self.players.keys():
            self.players[player](self.game, self.context)
