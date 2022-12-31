from math import inf
from abstracts import Search, Game
from safe_typing import Dict


class AlphaBetaPruningSearch(Search):
    def __call__(
        self, game: Game, ab: dict[Game.Player, float] = {i: -inf for i in Game.Player}
    ) -> Dict[Game.Player, int]:
        ans = {i: -inf for i in Game.Player}
        if game.is_terminal():
            return game.utility()

        for action in game.action():
            player = game.to_move()
            res = self(
                game.result(action),
                {**ab, player: ans[player]},
            )
            if res[player.other] < ab[player.other]:
                return res
            if res[player] > ans[player]:
                ans = res
        return {i: int(ans[i]) for i in Game.Player}
