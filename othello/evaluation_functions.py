from .othello_game import OthelloGame


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
    pass
    # return evaluate_by_mobility(game) + evaluate_by_material(game)
