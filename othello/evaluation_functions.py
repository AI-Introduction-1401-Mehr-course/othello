from .othello_game import OthelloGame
from safe_typing import Dict

evaluate_by_material = OthelloGame.utility

def evaluate_by_mobility(game: OthelloGame):
    ans = {}
    new_game = game.result(OthelloGame.Pass())
    ans[game.to_move()] = len(game.action()) - len(new_game.action())
    ans[new_game.to_move()] = len(new_game.action()) - len(game.action())
    return ans



def evaluate_by_mobility_and_material(game: OthelloGame):
    material = evaluate_by_material(game)
    mobility = evaluate_by_mobility(game)
    ans:Dict[OthelloGame.Player,int] = {}
    ans[game.to_move()] = material[game.to_move()] + mobility[game.to_move()]
    ans[game.to_move().other] = material[game.to_move().other] + mobility[game.to_move().other]
    return ans

