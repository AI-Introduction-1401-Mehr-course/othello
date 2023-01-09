from abstracts import Game, InformedSearch
from safe_typing import Callable, Dict, Tuple
import math


class AlphaBetaBeamSearch(InformedSearch):
    def __init__(
        self,
        evaluation: Callable[[Game], Dict[Game.Player, int]],
        beam: int,
        max_depth=math.inf,
        depth=0,
    ) -> None:
        InformedSearch.__init__(self, evaluation)
        self.max_depth = max_depth
        self.depth = depth
        self.beam = beam

    def is_cutoff(self):
        return self.depth > self.max_depth

    def sorted_actions(self, game: Game):
        return list(
            map(
                lambda x: x[0],
                sorted(
                    {
                        action: self.evaluation(game.result(action))
                        for action in game.action()
                    }.items(),
                    key=lambda x: x[1][game.to_move()],
                    reverse=True,
                ),
            )
        )

    def max_value(self, game: Game, a=-math.inf, b=math.inf) -> Tuple[int, Game.Action]:
        self.depth += 1
        if self.is_cutoff():
            return self.evaluation(game)[game.to_move()], game.Pass()
        v = -math.inf
        act = None
        actions = self.sorted_actions(game)[: self.beam]
        for action in actions:
            v2, a2 = self.min_value(game.result(action), a, b)
            if v2 > v:
                v, act = v2, action
                a = max(a, v)
            if v >= b:
                return (v, act)
        return (v, act)

    def min_value(self, game: Game, a=-math.inf, b=math.inf) -> Tuple[int, Game.Action]:
        self.depth += 1
        if self.is_cutoff():
            return self.evaluation(game)[game.to_move()], game.Pass()
        v = math.inf
        act = None

        actions = self.sorted_actions(game)[: self.beam]

        for action in actions:
            v2, a2 = self.max_value(game.result(action), a, b)
            if v2 < v:
                v, act = v2, action
                b = min(b, v)
            if v <= b:
                return (v, act)
        return (v, act)

    def __call__(self, game: Game) -> Dict[Game.Player, int]:
        p1 = self.max_value(game)
        self.depth = 0
        p2 = self.max_value(game.result(p1[1]))
        return {
            Game.Player.PLAYER1: p1,
            Game.Player.PLAYER2: p2,
        }
