from abstracts import Game, InformedSearch
from safe_typing import Callable, Dict
import math

class AlphaBetaBeamSearch(InformedSearch):

    def __init__(self, evaluation: Callable[[Game], Dict[Game.Player, int]], beam: int, max_depth = math.inf, depth = 0) -> None:
        InformedSearch.__init__(self,evaluation)
        self.max_depth = max_depth
        self.depth = depth
        self.beam = beam

    def max_value(self, game:Game, a=-math.inf, b=math.inf) -> (int, Game.Action):
        self.depth += 1
        if game.is_cutoff(self.max_depth, self.depth):
            return self.evaluation(game)[game.to_move],None
        v = -math.inf
        act = None
        
        # top beam actions based on evaluation function
        actions = list(map(lambda x:x[0],sorted({action:self.evaluation(game.result(action)) for action in game.action()}.items(),key=lambda x:x[1],reverse=True)))[:self.beam]

        for action in actions:
            v2,a2 = min_value(game,game.result(action),a,b)
            if v2 > v:
                v,act = v2,action
                a = max(a,v)
            if v >= b:
                return (v,act)
        return (v,act)


    def min_value(self, game:Game, a=-math.inf, b=math.inf) -> (int, Game.Action):
        self.depth += 1
        if game.is_cutoff(self.max_depth, self.depth):
            return self.evaluation(game)[game.to_move],None
        v = math.inf
        act = None
        
        # top beam actions based on evaluation function
        actions = list(map(lambda x:x[0],sorted({action:self.evaluation(game.result(action)) for action in game.action()}.items(),key=lambda x:x[1],reverse=True)))[:self.beam]

        for action in actions:
            v2,a2 = max_value(game,game.result(action),a,b)
            if v2 < v:
                v,act = v2,action
                b = min(b,v)
            if v <= b:
                return (v,act)
        return (v,act)


    def __call__(self, game: Game) -> Dict[Game.Player, int]:
        return {player:self.max_value(game) for player in Game.Player}

