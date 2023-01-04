from .othello_game import *


def evaluate_by_material(game: OthelloGame):

    light_disks_count = sum(
        1 for cell in game.state.board if cell == Cell.LIGHT_DISK
    )
    dark_disks_count = sum(
        1 for cell in game.state.board if cell == Cell.DARK_DISK
    )
    return dark_disks_count - light_disks_count


def evaluate_by_mobility(game: OthelloGame):
    
    turn = game.state.player_turn
    if turn == 1:
        dark_possible_moves = game.action().count()
        new_state_space = OthelloGame(
            game.State(
                game.State.board, game.state.player_turn.other
            )
        )
        light_possible_moves = new_state_space.action().count()
    else:
        light_possible_moves = game.action().count()
        new_state_space = OthelloGame(
            game.State(
                game.State.board, game.state.player_turn.other
            )
        )
        dark_possible_moves = new_state_space.action().count()

    return dark_possible_moves - light_possible_moves


def evaluate_by_mobility_and_material(state_space: OthelloGame):
    
    return evaluate_by_mobility + evaluate_by_material
