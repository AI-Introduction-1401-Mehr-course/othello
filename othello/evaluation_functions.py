from .othello_game import OthelloGame
from safe_typing import Dict

evaluate_by_material = OthelloGame.utility

def evaluate_by_mobility(game: OthelloGame):
    ans = {}
    ans[game.to_move()] = len(game.action())
    new_game = game.result(OthelloGame.Pass())
    ans[new_game.to_move()] = len(new_game.action())
    return ans
    # turn = game.state.player_turn

    # if turn == 1:
    #     dark_possible_moves = len(game.action())
    #     new_game = OthelloGame(
    #         game.State(
    #             game.State.board, game.state.player_turn.other
    #         )
    #     )
    #     # new_game = game.result(OthelloGame.Pass())
    #     light_possible_moves = len(new_game.action())
    # else:
    #     light_possible_moves = len(game.action())
    #     new_game = OthelloGame(
    #         game.State(
    #             game.State.board, game.state.player_turn.other
    #         )
    #     )
    #     dark_possible_moves = list.count(new_game.action())

    # return dark_possible_moves - light_possible_moves


def evaluate_by_mobility_and_material(game: OthelloGame):
    material = evaluate_by_material(game)
    mobility = evaluate_by_mobility(game)
    ans:Dict[OthelloGame.Player,int] = {}
    ans[game.to_move()] = material[game.to_move()] + mobility[game.to_move()]
    ans[game.to_move().other] = material[game.to_move().other] + mobility[game.to_move().other]
    return ans

